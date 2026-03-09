# 🤖 JIRA AI Chatbot (RAG + OpenAI + Streamlit)

Built an AI-powered JIRA chatbot using Retrieval-Augmented Generation (RAG) architecture to enable natural language querying of JIRA tickets.
Integrated semantic search with metadata filtering using ChromaDB and OpenAI embeddings to retrieve issue details such as status, priority, creation date, and resolution.
Designed structured prompt engineering to ensure accurate extraction of JIRA metadata fields and prevent hallucinations.

An AI-powered JIRA assistant built using:
- Pandas (Preprocessing)
- LangChain Orchestration Framework
- Sentence Transformer for embediing vector (Hugging Face)
- Open AI
- ChromaDB (Vector Database)
- Streamlit (Frontend)
- Refer Jira_API_Chatbot.ipynb for above steps perfomed
But model ready code is available in JiraAIChatbot.py
---
## Architecture
<img width="1192" height="670" alt="image" src="https://github.com/user-attachments/assets/76cc0281-f2c2-4ba3-9ad5-045bff4466ca" />

---
## 🚀 Features

- Retrieval-Augmented Generation (RAG)
- JIRA metadata extraction
- Clean Streamlit UI
- Natural language querying of JIRA tickets
- Sentence transformer + OpenAI LLM integration
- Semantic Vector search using ChromaDB with meta data filtering
- Issue key detection using regex-based intent routing
- Deterministic field extraction via structured prompt engineering
- Hallucination prevention using strict context grounding

---

# 🛠️ Setup Instructions

Follow these steps to run the project locally:

---

Chroma (Vector DB) for embeddings are available here - https://drive.google.com/file/d/1QYxliFEJbuowOrCZWKq09_GLPdsfYI7Y/view?usp=sharing. Download and keep it in same folder as below.

1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

4️⃣ Create .env File
```bash
OPENAPI_API_KEY=your_api_key_here
```

5️⃣ Run the Application
```bash
streamlit run app.py
```

App will open in your browser at:

http://localhost:8501

# Sample Questions to ask bot

1. Any issue asking to Please upload the image to Google Drive and share the link?
2. Give me the list of issues which were commented on 25/May/2023 ?
3. What is the current status of issue SRCTREEWIN-14037
4. Is this issue Displaying all changes between hash1 and hash2 doesn't raised?'
