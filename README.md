# Flask Chatbot Application

This is a simple chatbot application built using Flask and NLTK. The chatbot provides responses based on a predefined set of question-answer pairs.

## Features

- **Natural Language Processing**: Utilizes NLTK for tokenization, stemming, and stop word removal.
- **Chat Interface**: Provides a web-based interface for interacting with the chatbot.
- **Dynamic Response**: Uses token similarity to select the most relevant answer.

## Requirements

- Python 3.6+
- Flask
- NLTK

## Setup

1. **Download Files**: Make sure you have the following files in the same folder:
   - `app.py`: Main Flask application script.
   - `index.html`: HTML file for the chatbot interface.
   - `Sample Question Answers.json`: JSON file with question-answer pairs.

2. **Install Dependencies**: Install the required packages using pip:

    ```bash
    pip install flask nltk
    ```

3. **Download NLTK Data**: Download necessary NLTK data by running the following Python commands:

    ```python
    import nltk
    nltk.download('punkt')
    nltk.download('stopwords')
    ```

4. **Run the Application**: Start the Flask server by running:

    ```bash
    python app.py
    ```

5. **Access the Chatbot**: Open your web browser and navigate to `http://127.0.0.1:5000/` to interact with the chatbot.

## Directory Structure

Ensure your directory contains the following files:

- `app.py`: Main Flask application script.
- `index.html`: HTML file for the chatbot interface.
- `Sample Question Answers.json`: JSON file with question-answer pairs.

## Contributing

Feel free to fork this repository and make improvements or report issues.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [NLTK](https://www.nltk.org/)

