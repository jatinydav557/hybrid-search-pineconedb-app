import os
import streamlit as st
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec
from langchain_community.vectorstores import Pinecone as LangchainPinecone
from langchain_huggingface import HuggingFaceEmbeddings
from pinecone_text.sparse import BM25Encoder
from langchain_community.retrievers import PineconeHybridSearchRetriever
from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

# Load environment variables
load_dotenv()

# Environment Variables
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_REGION = os.getenv("PINECONE_REGION", "us-east-1")
HF_TOKEN = os.getenv("HF_TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Streamlit Config
st.set_page_config(page_title="🤖 RAG Chatbot", layout="centered")
st.title("🤖 RAG Chatbot with Hybrid Pinecone Search")

# Validate env
if not PINECONE_API_KEY or not HF_TOKEN or not GROQ_API_KEY:
    st.error(" Missing API keys. Check your `.env` file.")
    st.stop()

# Constants
INDEX_NAME = "hybrid-search-index"
DIMENSION = 384
METRIC = "dotproduct"

# Initialize Pinecone
@st.cache_resource
def init_pinecone():
    pc = Pinecone(api_key=PINECONE_API_KEY)
    if INDEX_NAME not in pc.list_indexes().names():
        pc.create_index(
            name=INDEX_NAME,
            dimension=DIMENSION,
            metric=METRIC,
            spec=ServerlessSpec(cloud="aws", region=PINECONE_REGION),
        )
    return pc.Index(INDEX_NAME)

# Initialize Embeddings, BM25, Corpus
@st.cache_resource
def init_models():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    bm25 = BM25Encoder()
    corpus = [
        "Artificial Intelligence (AI) is a field of computer science focused on building smart machines capable of performing tasks that typically require human intelligence.",
        "Machine learning is a subset of AI that involves training algorithms on data so they can make predictions or decisions without being explicitly programmed.",
        "Deep learning is a type of machine learning that uses neural networks with many layers.",
        "Large Language Models (LLMs) are deep learning models that can understand and generate human language.",
        "Retrieval-Augmented Generation (RAG) combines document retrieval with generation for accurate and grounded responses.",
        "Pinecone is a vector database for storing and searching large collections of embeddings efficiently."
    ]
    bm25.fit(corpus)
    return embeddings, bm25, corpus

# Initialize Hybrid Retriever
@st.cache_resource
def init_retriever(_index, _embeddings, _bm25):
    return PineconeHybridSearchRetriever(
        embeddings=_embeddings,
        sparse_encoder=_bm25,
        index=_index
    )

# Initialize LLM and RetrievalQA chain
@st.cache_resource
def init_rag(_retriever):
    llm = ChatGroq(api_key=GROQ_API_KEY, model="llama3-8b-8192")
    prompt_template = PromptTemplate(
        input_variables=["context", "question"],
        template="""
You are an intelligent assistant. Use the following context to answer the user's question.
---
{context}
---
Question: {question}
Answer:"""
    )
    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=_retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt_template}
    )

# --- Initialization ---
try:
    index = init_pinecone()
    embeddings, bm25_encoder, corpus = init_models()
    retriever = init_retriever(index, embeddings, bm25_encoder)
    rag_chain = init_rag(retriever)
except Exception as e:
    st.error(f"Initialization error: {e}")
    st.stop()

# --- Ingest Corpus into Pinecone ---
if "docs_ingested" not in st.session_state:
    try:
        retriever.add_texts(corpus)
        st.session_state.docs_ingested = True
        st.success("✅ AI documents indexed into Pinecone.")
    except Exception as e:
        st.warning(f"Ingestion failed: {e}")

# --- Chat UI ---
st.subheader("💬 Ask a question about AI concepts")
query = st.text_input("Your question:", "What is RAG in AI?")
if st.button("Get Answer"):
    if query.strip():
        with st.spinner("Thinking..."):
            try:
                result = rag_chain.invoke({"query": query})
                st.subheader("🤖 Answer")
                st.markdown(result["result"])

                with st.expander("📄 Source Documents"):
                    for doc in result["source_documents"]:
                        st.markdown(f"- {doc.page_content}")
            except Exception as e:
                st.error(f"RAG error: {e}")
    else:
        st.warning("Please enter a valid question.")
