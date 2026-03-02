# 🤖 JIRA AI Chatbot (RAG + OpenAI + Streamlit)

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

## 🚀 Features

- Retrieval-Augmented Generation (RAG)
- JIRA metadata extraction
- Clean Streamlit UI
- Sentence transformer + OpenAI LLM integration
- Vector search using ChromaDB with meta data filtering 
- Frontend application using Streamlit

---

# 🛠️ Setup Instructions

Follow these steps to run the project locally:

---

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
