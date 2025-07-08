▶️ YouTube Demo: [Watch Here](https://www.youtube.com/watch?v=eW3zsVGYdKE&ab_channel=Jatin)  
# 🤖 Hybrid Search RAG Chatbot using Pinecone, LangChain & Groq

This is a powerful **Retrieval-Augmented Generation (RAG)** chatbot using **hybrid retrieval**: dense (semantic) + sparse (keyword) search via **Pinecone**, BM25, and **HuggingFace embeddings** — all synthesized using **LangChain** and **Groq's ultra-fast LLaMA3 model**.

Built with ❤️ using **LangChain**, **Groq**, **Streamlit**, **Pinecone**, and **HuggingFace**.

---

## 🚀 Why This Project?

Most RAG systems today rely **only on dense embeddings** or just **BM25-style keyword search**.  
This project combines both to offer:

- **Better recall** for broad queries  
- **Improved precision** for technical or rare terms  
- **Faster inference** with Groq's blazing-fast LLMs  
- **End-to-end visibility** with source-backed answers  

Perfect for:  
📚 AI Q&A apps • 💬 Internal knowledge bots • 🤖 Personal research assistants

---

## 🧠 Features

✅ **Hybrid Retrieval** via Pinecone  
✅ Dense (MiniLM) + Sparse (BM25Encoder) vectorization  
✅ LLM answer synthesis using Groq’s `llama3-8b-8192`  
✅ RAG pipeline using LangChain  
✅ Simple UI with Streamlit  
✅ `.env` for secure API key management  

---

## 🧩 Tech Stack

| Tech            | Role                                    |
|-----------------|------------------------------------------|
| **LangChain**   | RAG logic, tool chaining, prompting     |
| **Pinecone**    | Hybrid vector store with sparse + dense |
| **Groq**        | LLM engine (LLaMA3-8B)                  |
| **BM25Encoder** | Sparse vector encoder (keyword search)  |
| **HuggingFace** | Embeddings (`all-MiniLM-L6-v2`)         |
| **Streamlit**   | Clean chat-based UI                     |

---

## 📁 Project Structure

```bash
hybrid-rag-chatbot/
├── app.py               # Main Streamlit app with RAG + hybrid logic
├── .env                 # API keys (Pinecone, Groq, HF)
├── requirements.txt     # All dependencies
└── README.md            # You're reading it
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone This Repo

```bash
git clone https://github.com/jatinydav557/hybrid-search-pineconedb-app.git
cd hybrid-search-pineconedb-app
```

### 2️⃣ Create Virtual Environment & Install

```bash
uv venv venv
source venv/bin/activate  # Or use venv\Scripts\activate on Windows
uv pip install -r requirements.txt
```

### 3️⃣ Configure API Keys

Create a `.env` file:

```env
PINECONE_API_KEY=your_pinecone_key
PINECONE_REGION=us-east-1
HF_TOKEN=your_huggingface_token
GROQ_API_KEY=your_groq_key
```

---

## 🚀 Run the App

```bash
streamlit run app.py
```

Open in your browser at `http://localhost:8501`

---

## 🧪 How It Works

1. Loads pre-ingested documents on AI/ML/RAG concepts  
2. Hybrid retriever fetches top `k` docs using BM25 + dense embeddings  
3. LangChain uses Groq's LLM to generate an answer  
4. App shows final answer **+ expandable source context**

---

## 💬 Example Query

> **Q:** How does hybrid retrieval work in RAG?  
>  
> **A:** Hybrid retrieval combines both semantic (dense) and keyword (sparse) search. Dense search finds conceptually similar passages, while sparse search matches exact terms, improving the completeness and precision of document retrieval.

---

## 📦 Requirements

```txt
streamlit
langchain
langchain-community
langchain-groq
pinecone-client
python-dotenv
sentence-transformers
huggingface-hub
```

---

## 🎓 About Me

I'm **Jatin**, a final-year MCA student and GenAI enthusiast. I’m building 20+ projects like this one to prove I can:

- ✅ Build production-ready LLM tools  
- ✅ Understand hybrid search at a systems level  
- ✅ Use modern libraries like LangChain, Pinecone, Groq  

📌 Open to:  
🔍 LLM Engineering • 🤖 Search/NLP roles • ⚙️ MLOps • 🧠 GenAI startups

---

## 📬 Let's Connect

- 🔗 [LinkedIn](https://www.linkedin.com/in/jatin557)  
- 🖥️ [GitHub](https://github.com/jatinydav557)  
- 📧 jatinydav557@gmail.com | 📱 +91-7340386035  
- 📹 [YouTube (Projects)](https://www.youtube.com/@jatinML/playlists)

---

## 🔭 Future Work

- ✅ Add PDF and Web link loaders  
- ✅ Streamlit Cloud / GCP Deployment  
- ✅ Chat history memory  
- ✅ Tool usage transparency (debug mode)  
- ✅ Reranking with ColBERT

---

> “Hybrid search is the future of smart information systems — this project is my way of learning and contributing to it.”

⭐ **If this helped or inspired you, drop a star and connect!**
