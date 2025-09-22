import streamlit as st
from rag_chatbot import RAGChatbot

st.set_page_config(
    page_title="Neural RAG System",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Refined CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap');

.stApp {
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
    color: #e8e8e8;
}

.main-header {
    font-family: 'Inter', sans-serif;
    text-align: center;
    color: #ffffff;
    font-size: 2.2rem;
    font-weight: 500;
    margin: 2rem 0 1rem 0;
    letter-spacing: 0.05em;
}

.status-line {
    font-family: 'Inter', sans-serif;
    font-size: 0.9rem;
    color: #a0a0a0;
    text-align: center;
    margin-bottom: 2rem;
    font-weight: 300;
}

.chat-message {
    font-family: 'Inter', sans-serif;
    padding: 1.2rem;
    margin: 1rem 0;
    border-radius: 8px;
    border-left: 3px solid #4a5568;
    background: rgba(255, 255, 255, 0.03);
    backdrop-filter: blur(10px);
}

.user-message {
    border-left-color: #4299e1;
    background: rgba(66, 153, 225, 0.05);
}

.bot-message {
    border-left-color: #48bb78;
    background: rgba(72, 187, 120, 0.05);
}

.stSidebar {
    background: linear-gradient(180deg, #1a1a2e 0%, #16213e 100%);
    border-right: 1px solid rgba(255, 255, 255, 0.1);
}

.stButton > button {
    background: linear-gradient(135deg, #4299e1, #48bb78);
    color: #ffffff;
    border: none;
    border-radius: 6px;
    font-weight: 500;
    transition: all 0.3s ease;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.stButton > button:hover {
    transform: translateY(-1px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.source-tag {
    display: inline-block;
    background: rgba(66, 153, 225, 0.1);
    color: #4299e1;
    padding: 0.2rem 0.6rem;
    border-radius: 12px;
    font-size: 0.75rem;
    margin: 0.1rem;
    border: 1px solid rgba(66, 153, 225, 0.2);
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="main-header">⚡ Neural RAG</div>', unsafe_allow_html=True)
st.markdown('<div class="status-line">Powered by Llama 3.1-8B • Vector Search • Real-time Intelligence</div>', unsafe_allow_html=True)

# Initialize chatbot
@st.cache_resource
def load_chatbot():
    return RAGChatbot()

try:
    chatbot = load_chatbot()
    
    # Chat interface
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Chat display
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f'<div class="chat-message user-message"><strong>You:</strong> {message["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="chat-message bot-message"><strong>AI:</strong> {message["content"]}</div>', unsafe_allow_html=True)

    # Input
    if prompt := st.chat_input("💬 Ask me anything about technology, science, or literature..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        with st.spinner("🧠 Processing your query..."):
            response = chatbot.generate_response(prompt)
        
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()

    # Sidebar
    with st.sidebar:
        st.markdown("### 📚 Knowledge Sources")
        sources = ["Literature", "Science", "Technology", "Health", "Environment"]
        for source in sources:
            st.markdown(f'<span class="source-tag">{source}</span>', unsafe_allow_html=True)
        
        st.markdown("### ⚙️ Controls")
        if st.button("🗑️ Clear Chat"):
            st.session_state.messages = []
            st.rerun()
        
        st.markdown("### 📊 Stats")
        st.write(f"Messages: {len(st.session_state.messages)}")
        st.write("Model: Llama 3.1-8B")
        st.write("Vector DB: FAISS")

except Exception as e:
    st.error("Please add your Cerebras API key to .env file")
    st.code("CEREBRAS_API_KEY=your_actual_api_key")