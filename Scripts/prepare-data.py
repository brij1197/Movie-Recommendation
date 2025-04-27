import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import os

def run_notebook():
    print("Starting notebook execution...")
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    notebook_path = os.path.join(script_dir, "movie-recommendation.ipynb")
    
    if not os.path.exists(notebook_path):
        raise FileNotFoundError(f"Notebook not found at: {notebook_path}")
    
    print(f"Loading notebook from: {notebook_path}")
    
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    
    print("Setting up execution environment...")
    
    output_dir = os.path.join(script_dir, '')
    os.makedirs(output_dir, exist_ok=True)
    print(f"Output directory: {output_dir}")
    
    executor = ExecutePreprocessor(
        timeout=600,
        kernel_name='python3'
    )
    
    print("Executing notebook...")
    
    executor.preprocess(nb, {'metadata': {'path': os.path.dirname(notebook_path)}})
    
    print("Checking for generated files...")
    
    required_files = ['movies.pkl', 'similarity.pkl']
    for file in required_files:
        file_path = os.path.join(output_dir, file)
        print(f"Checking for file at: {file_path}")
        if os.path.exists(file_path):
            print(f"Generated file found: {file}")
            file_size = os.path.getsize(file_path)
            print(f"File size: {file_size} bytes")
        else:
            print(f"Contents of {output_dir}:")
            for item in os.listdir(output_dir):
                print(f"- {item}")
            raise FileNotFoundError(f"Expected file not found: {file}")
    
    print("Notebook execution completed successfully!")

if __name__ == "__main__":
    try:
         run_notebook()
    except Exception as e:
        print(f"Error during notebook execution: {e}")
        import traceback
        print("Detailed error:")
        print(traceback.format_exc())
        raise
