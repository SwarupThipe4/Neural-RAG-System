import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("Dependencies installed successfully!")
    except subprocess.CalledProcessError:
        print("Failed to install dependencies")
        return False
    return True

def check_env_file():
    """Check if .env file exists and has API key"""
    if not os.path.exists(".env"):
        print(".env file not found")
        print("Creating .env template...")
        with open(".env", "w") as f:
            f.write("CEREBRAS_API_KEY=your_cerebras_api_key_here\n")
        print(".env file created. Please add your Cerebras API key.")
        return False
    
    with open(".env", "r") as f:
        content = f.read()
        if "your_cerebras_api_key_here" in content:
            print("Please replace 'your_cerebras_api_key_here' with your actual Cerebras API key in .env")
            return False
    
    print(".env file configured")
    return True

def run_setup():
    """Run complete setup"""
    print("Setting up RAG Chatbot...")
    
    if not install_requirements():
        return
    
    if not check_env_file():
        print("\nNext steps:")
        print("1. Get your Cerebras API key from: https://cerebras.ai")
        print("2. Edit .env file and replace 'your_cerebras_api_key_here' with your actual key")
        print("3. Run: streamlit run app.py")
        return
    
    print("\nSetup complete! Run the chatbot with:")
    print("streamlit run app.py")

if __name__ == "__main__":
    run_setup()