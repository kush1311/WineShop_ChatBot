from flask import Flask, request, jsonify, send_from_directory
import json
import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

app = Flask(__name__)

# Load the corpus
with open('Sample Question Answers.json', 'r') as f:
    corpus = json.load(f)

# Download NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Initialize NLTK components
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

def preprocess(text):
    tokens = word_tokenize(text.lower())
    tokens = [stemmer.stem(word) for word in tokens if word.isalnum() and word not in stop_words]
    return tokens

@app.route('/')
def index():
    return send_from_directory('', 'index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    user_tokens = preprocess(user_message)
    max_similarity = 0
    best_answer = "Please contact our business directly for more information."

    for qa in corpus:
        question_tokens = preprocess(qa['question'])
        common_tokens = set(user_tokens) & set(question_tokens)
        similarity = len(common_tokens) / len(question_tokens)
        if similarity > max_similarity:
            max_similarity = similarity
            best_answer = qa['answer']

    return jsonify({"answer": best_answer})

if __name__ == '__main__':
    app.run(debug=True)
