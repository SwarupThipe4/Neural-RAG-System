import subprocess
import sys
import os

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"Running: {description}")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e.stderr}")
        return False

def deploy_to_github():
    """Deploy project to GitHub"""
    
    # Check if git is initialized
    if not os.path.exists('.git'):
        if not run_command('git init', 'Initialize Git repository'):
            return
    
    # Add all files
    if not run_command('git add .', 'Add files to Git'):
        return
    
    # Commit changes
    commit_message = input("Enter commit message (or press Enter for default): ").strip()
    if not commit_message:
        commit_message = "Initial commit: Neural RAG System with tech UI"
    
    if not run_command(f'git commit -m "{commit_message}"', 'Commit changes'):
        return
    
    # Get GitHub repository URL
    repo_url = input("Enter your GitHub repository URL (https://github.com/username/repo.git): ").strip()
    if repo_url:
        if not run_command(f'git remote add origin {repo_url}', 'Add remote origin'):
            # If remote already exists, try to set URL
            run_command(f'git remote set-url origin {repo_url}', 'Update remote origin')
        
        if not run_command('git push -u origin main', 'Push to GitHub'):
            # Try master branch if main fails
            run_command('git push -u origin master', 'Push to GitHub (master branch)')
    
    print("\n🚀 Deployment complete!")
    print("Your Neural RAG System is now on GitHub!")

if __name__ == "__main__":
    deploy_to_github()