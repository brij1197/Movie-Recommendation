import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import os

def run_notebook():
    notebook_path="movie-recommendation.ipynb"
    
    if not os.path.exists(notebook_path):
        raise FileNotFoundError(f"Notebook {notebook_path} not found")
    print("Running notebook to generate data...")
    
    with open(notebook_path) as f:
        nb=nbformat.read(f,as_version=4)
        
    executor = ExecutePreprocessor(timeout=600, kernel_name='python3')
    
    executor.preprocess(nb, {'metadata': {'path': ''}})
    
if __name__ == "__main__":
    run_notebook()