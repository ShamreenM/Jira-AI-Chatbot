from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.chat_models import ChatOpenAI
import re

def retrieve_docs(query,apiKey):
    embedding = HuggingFaceEmbeddings(
     model_name="BAAI/bge-base-en-v1.5",
     encode_kwargs={"normalize_embeddings": True})

    # Load existing Chroma DB
    vectorstore = Chroma(
    persist_directory=".\chroma_db_backup",  # your stored folder
    embedding_function=embedding)
    llm = ChatOpenAI(model="gpt-4",api_key=apiKey)
    match = re.search(r"[A-Z]+-\d+", query)
    if match:
        issue_key = match.group()
        retrieve_docs = vectorstore.similarity_search(
            query="",
            filter={"issue_key": issue_key},
            k=5
            )
    else:
        retrieve_docs = vectorstore.similarity_search(
        query,
        k=5
    )

    context = ""

    for doc in retrieve_docs:
        context += f"""
        Issue Key: {doc.metadata.get('issue_key')}
        Issue Type: {doc.metadata.get('issue_type')}
        Status: {doc.metadata.get('status')}
        Project name: {doc.metadata.get('project')}
        Project type: {doc.metadata.get('Project type')}
        Project url: {doc.metadata.get('Project url')}
        Priority: {doc.metadata.get('priority')}
        Resolution: {doc.metadata.get('Resolution')}
        Created: {doc.metadata.get('Created')}
        Updated: {doc.metadata.get('Updated')}
        Last Viewed: {doc.metadata.get('Last Viewed')}
        Resolved: {doc.metadata.get('Resolved')}
        Custom field (Symptom Severity): {doc.metadata.get('Custom field (Symptom Severity)')}

        Description: {doc.page_content}
    """
  
    prompt = f"""
    You are a JIRA structured data assistant.

    Your task is to extract requested fields strictly from the provided context.

    RULES:
    1. Use ONLY the information present in the context.
    2. Do NOT infer, assume, or generate missing values.
    3. If a requested field exists in the context, you MUST return it.
    4. If a requested field does not exist, return: Not Available
    5. Do NOT summarize.
    6. Do NOT explain.
    7. Do NOT add extra text.
    8. If output has repeated issue number , Do not repeat it .

    FIELD EXTRACTION RULE:
    Return ONLY the fields that are explicitly requested in the user question.
    Preserve exact field names and exact values as written in context.
    Do NOT change date formats.

    CONTEXT:
    {context}

    USER QUESTION:
    {query}

    OUTPUT FORMAT:
    <Field Name>: <Exact Value>

    If no matching issue is found in the context, return:
    No issue found.
    """
    response = llm.invoke(prompt)
    return response.content


