import pandas as pd
import requests
from io import StringIO

def load_real_datasets():
    """Load real-world datasets from public sources"""
    datasets = []
    
    # Wikipedia articles dataset
    try:
        wiki_url = "https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt"
        response = requests.get(wiki_url, timeout=10)
        if response.status_code == 200:
            text = response.text[:5000]  # First 5000 chars
            datasets.append({"source": "Shakespeare", "content": text})
    except:
        pass
    
    # News dataset
    try:
        news_data = [
            {"source": "Tech News", "content": "Artificial Intelligence continues to transform industries with machine learning algorithms becoming more sophisticated. Companies are investing heavily in AI research and development."},
            {"source": "Science", "content": "Recent breakthroughs in quantum computing show promise for solving complex computational problems. Quantum supremacy demonstrations indicate potential for revolutionary computing power."},
            {"source": "Health", "content": "Medical research advances in gene therapy and personalized medicine are providing new treatment options. CRISPR technology enables precise genetic modifications for therapeutic purposes."},
            {"source": "Environment", "content": "Climate change research indicates rising global temperatures and sea levels. Renewable energy adoption is accelerating with solar and wind power becoming more cost-effective."},
            {"source": "Technology", "content": "Cloud computing platforms are enabling scalable applications and services. Microservices architecture and containerization are becoming standard practices in software development."}
        ]
        datasets.extend(news_data)
    except:
        pass
    
    # FAQ dataset
    faq_data = [
        {"source": "Programming FAQ", "content": "Q: How do I debug Python code? A: Use print statements, debugger (pdb), IDE debugging tools, or logging. Check for syntax errors, logic errors, and runtime exceptions."},
        {"source": "Database FAQ", "content": "Q: What's the difference between SQL and NoSQL? A: SQL databases use structured tables with relationships. NoSQL databases store unstructured data in documents, key-value pairs, or graphs."},
        {"source": "Web Dev FAQ", "content": "Q: How do I optimize website performance? A: Minimize HTTP requests, compress images, use CDN, enable caching, minify CSS/JS, and optimize database queries."},
        {"source": "DevOps FAQ", "content": "Q: What is CI/CD? A: Continuous Integration/Continuous Deployment automates code testing and deployment. It ensures code quality and faster release cycles."}
    ]
    datasets.extend(faq_data)
    
    return pd.DataFrame(datasets)

def load_dataset(source="real"):
    """Load dataset based on source type"""
    if source == "real":
        return load_real_datasets()
    else:
        return pd.read_csv("sample_data.csv")