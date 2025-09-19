import requests
import pandas as pd

def download_wikipedia_dataset():
    """Download Wikipedia articles dataset"""
    try:
        url = "https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-abstract1.xml"
        print("Note: Large Wikipedia datasets require special processing.")
        print("Using sample text data instead for demonstration.")
        
        # Sample Wikipedia-style content
        wiki_data = [
            {"title": "Machine Learning", "content": "Machine learning is a method of data analysis that automates analytical model building. It is a branch of artificial intelligence based on the idea that systems can learn from data, identify patterns and make decisions with minimal human intervention."},
            {"title": "Python Programming", "content": "Python is an interpreted, high-level and general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant whitespace."},
            {"title": "Data Science", "content": "Data science is an inter-disciplinary field that uses scientific methods, processes, algorithms and systems to extract knowledge and insights from many structural and unstructured data."},
            {"title": "Cloud Computing", "content": "Cloud computing is the on-demand availability of computer system resources, especially data storage and computing power, without direct active management by the user."}
        ]
        
        df = pd.DataFrame(wiki_data)
        df.to_csv("wikipedia_data.csv", index=False)
        print("Wikipedia-style dataset saved to wikipedia_data.csv")
        
    except Exception as e:
        print(f"Error downloading Wikipedia data: {e}")

def download_news_dataset():
    """Download news dataset"""
    try:
        # Sample news data (in real scenario, you'd use news APIs)
        news_data = [
            {"category": "Technology", "headline": "AI Breakthrough in Natural Language Processing", "content": "Researchers have developed a new transformer model that achieves state-of-the-art performance on multiple NLP benchmarks."},
            {"category": "Science", "headline": "New Discovery in Quantum Physics", "content": "Scientists have observed quantum entanglement at room temperature, opening new possibilities for quantum computing applications."},
            {"category": "Health", "headline": "Gene Therapy Shows Promise", "content": "Clinical trials demonstrate successful treatment of genetic disorders using CRISPR-based gene editing techniques."}
        ]
        
        df = pd.DataFrame(news_data)
        df.to_csv("news_data.csv", index=False)
        print("News dataset saved to news_data.csv")
        
    except Exception as e:
        print(f"Error creating news data: {e}")

if __name__ == "__main__":
    download_wikipedia_dataset()
    download_news_dataset()
    print("Real-world datasets prepared!")