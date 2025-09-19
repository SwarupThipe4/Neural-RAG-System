import pandas as pd
import faiss
import numpy as np
import requests
import json
from sentence_transformers import SentenceTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter
from config import CEREBRAS_API_KEY, CEREBRAS_API_URL, CHUNK_SIZE, CHUNK_OVERLAP, TOP_K_RESULTS
from data_loader import load_dataset

class RAGChatbot:
    def __init__(self, data_source="real"):
        self.embeddings = SentenceTransformer('all-MiniLM-L6-v2')
        self.index = None
        self.documents = []
        self.load_knowledge_base(data_source)
        
    def load_knowledge_base(self, data_source):
        df = load_dataset(data_source)
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE, 
            chunk_overlap=CHUNK_OVERLAP
        )
        
        for _, row in df.iterrows():
            if 'source' in df.columns:
                content = f"{row['source']}: {row['content']}"
            elif 'category' in df.columns:
                content = f"{row['category']} - {row['topic']}: {row['content']}"
            else:
                content = row['content']
            chunks = text_splitter.split_text(content)
            self.documents.extend(chunks)
        
        embeddings_matrix = self.embeddings.encode(self.documents)
        
        self.index = faiss.IndexFlatIP(embeddings_matrix.shape[1])
        self.index.add(embeddings_matrix.astype('float32'))
    
    def retrieve_context(self, query):
        query_embedding = self.embeddings.encode([query])
        _, indices = self.index.search(query_embedding.astype('float32'), TOP_K_RESULTS)
        return [self.documents[i] for i in indices[0]]
    
    def generate_response(self, query):
        context = self.retrieve_context(query)
        
        prompt = f"""Based on the following context, answer the question:

Context: {chr(10).join(context)}

Question: {query}

Answer:"""
        
        headers = {
            "Authorization": f"Bearer {CEREBRAS_API_KEY}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": "llama3.1-8b",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7,
            "max_tokens": 500
        }
        
        response = requests.post(CEREBRAS_API_URL, headers=headers, json=data)
        return response.json()["choices"][0]["message"]["content"]

def main():
    chatbot = RAGChatbot()
    
    print("RAG Chatbot initialized. Type 'quit' to exit.")
    
    while True:
        query = input("\nYou: ")
        if query.lower() == 'quit':
            break
        
        response = chatbot.generate_response(query)
        print(f"Bot: {response}")

if __name__ == "__main__":
    main()