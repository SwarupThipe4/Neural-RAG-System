# ⚡ Neural RAG System

> AI-Powered Knowledge Retrieval Engine with Cyberpunk UI

A cutting-edge Retrieval-Augmented Generation chatbot featuring real-world datasets, neural embeddings, and a tech-savvy interface.

![Neural RAG System](https://img.shields.io/badge/AI-Neural%20RAG-00ff88?style=for-the-badge&logo=artificial-intelligence)
![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit)
![Cerebras](https://img.shields.io/badge/Cerebras-AI-purple?style=for-the-badge)

## 🚀 Features

- **🧠 Neural Architecture**: Llama 3.1-8B via Cerebras AI
- **🔍 Vector Search**: FAISS-powered similarity matching
- **📊 Real-World Data**: Literature, tech news, scientific papers
- **🎨 Cyberpunk UI**: Dark theme with neon aesthetics
- **⚡ High Performance**: Optimized inference pipeline
- **🔒 Secure**: Encrypted API calls and isolated sessions

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| **LLM** | Cerebras AI (Llama 3.1-8B) |
| **Embeddings** | Sentence Transformers (MiniLM-L6-v2) |
| **Vector DB** | FAISS |
| **Frontend** | Streamlit |
| **Data Processing** | LangChain, Pandas |

## 📦 Quick Start

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/neural-rag-system.git
cd neural-rag-system
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure API Key
```bash
echo "CEREBRAS_API_KEY=your_api_key_here" > .env
```

### 4. Launch System
```bash
streamlit run app.py
```

## 🎯 Usage

### Web Interface
Access the Neural RAG System at `http://localhost:8501`

### Command Line
```bash
python rag_chatbot.py
```

### API Integration
```python
from rag_chatbot import RAGChatbot

chatbot = RAGChatbot()
response = chatbot.generate_response("Your query here")
```

## 📊 Data Sources

- **Literature**: Shakespeare corpus, classic texts
- **Technology**: AI breakthroughs, programming guides
- **Science**: Research papers, discoveries
- **Health**: Medical advances, gene therapy
- **Environment**: Climate data, sustainability

## 🔧 Configuration

### Environment Variables
```env
CEREBRAS_API_KEY=your_cerebras_api_key
CHUNK_SIZE=500
TOP_K_RESULTS=3
```

### System Requirements
- Python 3.8+
- 4GB RAM minimum
- Internet connection for API calls

## 🚀 Deployment

### Local Development
```bash
python setup.py  # Automated setup
streamlit run app.py
```

### Production
```bash
python deploy.py  # Deploy to GitHub
```

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/neural-enhancement`)
3. Commit changes (`git commit -m 'Add neural enhancement'`)
4. Push to branch (`git push origin feature/neural-enhancement`)
5. Open Pull Request

## 📄 License

MIT License - see [LICENSE](LICENSE) file

## 🔗 Links

- [Cerebras AI](https://cerebras.ai)
- [Streamlit Docs](https://docs.streamlit.io)
- [FAISS Documentation](https://faiss.ai)

---

**Built with ⚡ by Neural Engineers**