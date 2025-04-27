import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import os

def run_notebook():
    print("Starting notebook execution...")
    
    notebook_path = os.path.join(os.path.dirname(__file__), "movie-recommendation.ipynb")
    
    if not os.path.exists(notebook_path):
        raise FileNotFoundError(f"Notebook not found at: {notebook_path}")
    
    print(f"Loading notebook from: {notebook_path}")
    
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    
    print("Setting up execution environment...")
    
    executor = ExecutePreprocessor(
        timeout=600,
        kernel_name='python3'
    )
    
    print("Executing notebook...")
    
    executor.preprocess(nb, {'metadata': {'path': os.path.dirname(notebook_path)}})
    
    print("Checking for generated files...")
    
    required_files = ['movies.pkl', 'similarity.pkl']
    for file in required_files:
        file_path = os.path.join(os.path.dirname(notebook_path), '..', file)
        if os.path.exists(file_path):
            print(f"Generated file found: {file}")
        else:
            raise FileNotFoundError(f"Expected file not found: {file}")
    
    print("Notebook execution completed successfully!")

if __name__ == "__main__":
    try:
        run_notebook()
    except Exception as e:
        print(f"Error during notebook execution: {e}")
        raise
