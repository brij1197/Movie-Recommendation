# Movie Recommendation System

This project is a Movie Recommendation System that uses Streamlit for the frontend. It allows users to select a movie and get recommendations based on the selected movie.

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/brij1197/Movie-Recommendation.git
    cd movie-recommendation
    ```

2. Create a virtual environment:

    ```sh
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:

        ```sh
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```sh
        source venv/bin/activate
        ```

4. (On macOS/Linux) Move the files from Scripts to the bin folder

5. Install the required libraries:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Ensure you have the necessary API keys and environment variables set up in a `.env` file.

2. Run the Jupyter notebook to generate the pickle files.

3. Run the Streamlit app:

    ```sh
    streamlit run app.py
    ```

3. Open your web browser and go to `http://localhost:8501` to view the app.

## Requirements

- Python 3.6 or higher
- Streamlit
- Pandas
- NLTK
- Scikit-Learn
