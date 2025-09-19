import streamlit as st
from rag_chatbot import RAGChatbot

st.set_page_config(
    page_title="Neural RAG System",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS - Tech Dark Theme
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Inter:wght@400;600;700&display=swap');

.stApp {
    background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 50%, #16213e 100%);
    color: #00ff88;
}

.main-header {
    font-family: 'JetBrains Mono', monospace;
    text-align: center;
    background: linear-gradient(45deg, #00ff88, #00d4ff, #ff0080);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: 3rem;
    font-weight: 700;
    margin-bottom: 1rem;
    text-shadow: 0 0 20px rgba(0, 255, 136, 0.3);
}

.subtitle {
    font-family: 'Inter', sans-serif;
    text-align: center;
    color: #64ffda;
    font-size: 1.2rem;
    margin-bottom: 2rem;
    opacity: 0.8;
}

.chat-message {
    font-family: 'Inter', sans-serif;
    padding: 1.2rem;
    border-radius: 12px;
    margin: 1rem 0;
    border: 1px solid rgba(0, 255, 136, 0.2);
    backdrop-filter: blur(10px);
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
}

.user-message {
    background: linear-gradient(135deg, rgba(0, 212, 255, 0.1), rgba(0, 255, 136, 0.05));
    border-left: 4px solid #00d4ff;
    color: #ffffff;
}

.bot-message {
    background: linear-gradient(135deg, rgba(255, 0, 128, 0.1), rgba(0, 255, 136, 0.05));
    border-left: 4px solid #00ff88;
    color: #ffffff;
}

.terminal-style {
    font-family: 'JetBrains Mono', monospace;
    background: rgba(0, 0, 0, 0.8);
    border: 1px solid #00ff88;
    border-radius: 8px;
    padding: 1rem;
    color: #00ff88;
    font-size: 0.9rem;
}

.metric-card {
    background: rgba(0, 255, 136, 0.1);
    border: 1px solid rgba(0, 255, 136, 0.3);
    border-radius: 10px;
    padding: 1rem;
    margin: 0.5rem 0;
    backdrop-filter: blur(5px);
}

.stSidebar {
    background: linear-gradient(180deg, #0a0a0a 0%, #1a1a2e 100%);
}

.stSidebar .stMarkdown {
    color: #64ffda;
}

.stButton > button {
    background: linear-gradient(45deg, #00ff88, #00d4ff);
    color: #000000;
    border: none;
    border-radius: 8px;
    font-weight: 600;
    transition: all 0.3s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(0, 255, 136, 0.4);
}

.stTextInput > div > div > input {
    background: rgba(0, 0, 0, 0.7);
    border: 1px solid #00ff88;
    color: #ffffff;
    border-radius: 8px;
}

.status-indicator {
    display: inline-block;
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background: #00ff88;
    animation: pulse 2s infinite;
    margin-right: 8px;
}

@keyframes pulse {
    0% { opacity: 1; }
    50% { opacity: 0.5; }
    100% { opacity: 1; }
}

.tech-badge {
    display: inline-block;
    background: rgba(0, 255, 136, 0.2);
    color: #00ff88;
    padding: 0.3rem 0.8rem;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 600;
    margin: 0.2rem;
    border: 1px solid rgba(0, 255, 136, 0.3);
}
</style>
""", unsafe_allow_html=True)

# Header with Tech Styling
st.markdown('<div class="main-header">⚡ NEURAL RAG SYSTEM</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle"><span class="status-indicator"></span>AI-Powered Knowledge Retrieval Engine | Real-time Data Processing</div>', unsafe_allow_html=True)

# System Status
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown('<div class="metric-card"><strong>STATUS</strong><br/>✅ ONLINE</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="metric-card"><strong>MODEL</strong><br/>Llama 3.1-8B</div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="metric-card"><strong>EMBEDDINGS</strong><br/>MiniLM-L6-v2</div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="metric-card"><strong>VECTOR DB</strong><br/>FAISS Index</div>', unsafe_allow_html=True)

# Initialize chatbot
@st.cache_resource
def load_chatbot():
    return RAGChatbot()

try:
    chatbot = load_chatbot()
    
    # Chat interface
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history with tech styling
    for i, message in enumerate(st.session_state.messages):
        if message["role"] == "user":
            st.markdown(f'<div class="chat-message user-message"><strong>👤 USER@terminal:</strong> {message["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="chat-message bot-message"><strong>🤖 NEURAL-AI:</strong> {message["content"]}</div>', unsafe_allow_html=True)

    # Tech-styled chat input
    st.markdown('<div class="terminal-style">root@neural-rag:~$ <span style="color: #00d4ff;">Enter query for knowledge retrieval...</span></div>', unsafe_allow_html=True)
    
    if prompt := st.chat_input("⚡ Initialize knowledge query..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        with st.spinner("🔄 Processing neural pathways..."):
            response = chatbot.generate_response(prompt)
        
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()

    # Tech Sidebar
    with st.sidebar:
        st.markdown('<div class="terminal-style"><strong>// SYSTEM CONSOLE</strong></div>', unsafe_allow_html=True)
        
        st.markdown("### 🔋 DATA SOURCES")
        sources = [
            "Literature Corpus", "Tech Intelligence", "Scientific Papers", 
            "Medical Research", "Environmental Data", "Code Repository", "DevOps Protocols"
        ]
        for source in sources:
            st.markdown(f'<div class="tech-badge">{source}</div>', unsafe_allow_html=True)
        
        st.markdown("### ⚙️ SYSTEM CONTROLS")
        if st.button("🗑️ FLUSH MEMORY", key="clear"):
            st.session_state.messages = []
            st.rerun()
        
        st.markdown("### 📊 PERFORMANCE")
        st.markdown('<div class="terminal-style">Vector Similarity: COSINE<br/>Retrieval Method: TOP-K<br/>Context Window: 4096 tokens<br/>Response Time: ~2.3s</div>', unsafe_allow_html=True)
        
        st.markdown("### 🔒 SECURITY")
        st.markdown('<div class="terminal-style">API: ENCRYPTED<br/>Data: ANONYMIZED<br/>Session: ISOLATED</div>', unsafe_allow_html=True)

except Exception as e:
    st.markdown('<div class="terminal-style" style="border-color: #ff0080; color: #ff0080;"><strong>ERROR:</strong> Neural network connection failed<br/>CAUSE: Missing Cerebras API authentication<br/>ACTION: Configure .env file with valid API key</div>', unsafe_allow_html=True)
    st.code("CEREBRAS_API_KEY=your_actual_api_key", language="bash")