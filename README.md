# Flask Chatbot Application

This is a simple chatbot application built using Flask and NLTK. The chatbot answers user queries based on a predefined set of question-answer pairs.

## Features

- **Natural Language Processing**: Utilizes NLTK for tokenization, stemming, and stop word removal.
- **Chat Interface**: A user-friendly web interface for interacting with the chatbot.
- **Dynamic Response**: Returns the most relevant answer based on token similarity.

## Requirements

- Python 3.6+
- Flask
- NLTK

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Download NLTK data:

    ```python
    import nltk
    nltk.download('punkt')
    nltk.download('stopwords')
    ```

5. Make sure you have a `Sample Question Answers.json` file in the root directory of the project with your question-answer pairs.

## Usage

1. Start the Flask server:

    ```bash
    python app.py
    ```

2. Open your web browser and navigate to `http://127.0.0.1:5000/` to interact with the chatbot.

## Directory Structure

- `app.py`: The main Flask application script.
- `index.html`: The HTML file for the chatbot interface.
- `Sample Question Answers.json`: The JSON file containing predefined question-answer pairs.
- `requirements.txt`: A file listing the required Python packages.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [NLTK](https://www.nltk.org/)

