import os

def list_files(startpath):
    # Folders to skip to keep the output clean
    exclude = {'.git', '__pycache__', 'dsportfolio_venv', 'vector_db'}
    
    for root, dirs, files in os.walk(startpath):
        # Filter out the excluded directories
        dirs[:] = [d for d in dirs if d not in exclude]
        
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print(f'{indent}{os.path.basename(root)}/')
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print(f'{subindent}{f}')

if __name__ == "__main__":
    # Get current directory
    project_root = os.getcwd()
    print(f"Project Structure for: {project_root}\n")
    list_files(project_root)
