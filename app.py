from flask import Flask, request, jsonify, send_from_directory
import json
import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Groq API configuration
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_MODEL = "llama3-8b-8192"  # Fast and efficient model

# Load the wine knowledge base
with open('Sample Question Answers.json', 'r') as f:
    wine_knowledge = json.load(f)

def create_context_from_knowledge(user_question):
    """Create context from wine knowledge base for RAG"""
    # Extract relevant information from knowledge base
    relevant_info = []
    for qa in wine_knowledge:
        # Simple keyword matching to find relevant context
        question_lower = qa['question'].lower()
        answer_lower = qa['answer'].lower()
        user_lower = user_question.lower()
        
        # Check if any keywords match
        keywords = user_lower.split()
        relevance_score = 0
        for keyword in keywords:
            if len(keyword) > 3:  # Only consider meaningful keywords
                if keyword in question_lower or keyword in answer_lower:
                    relevance_score += 1
        
        if relevance_score > 0:
            relevant_info.append({
                'question': qa['question'],
                'answer': qa['answer'],
                'score': relevance_score
            })
    
    # Sort by relevance and take top 3 most relevant pieces
    relevant_info.sort(key=lambda x: x['score'], reverse=True)
    top_context = relevant_info[:3]
    
    # Format context for the prompt
    context = "Based on the following wine shop information:\n\n"
    for item in top_context:
        context += f"Q: {item['question']}\nA: {item['answer']}\n\n"
    
    return context

def get_groq_response(user_question, context):
    """Get response from Groq API using RAG approach"""
    if not GROQ_API_KEY:
        return "API key not configured. Please contact support."
    
    # Create the system prompt with RAG context
    system_prompt = f"""You are a knowledgeable wine shop assistant. Use the following information to answer customer questions accurately and helpfully. If the information provided doesn't fully answer the question, use your general wine knowledge to provide additional helpful insights.

{context}

Always be friendly, professional, and wine-enthusiast oriented. If you're not sure about something specific to this wine shop, suggest contacting the business directly for the most accurate information."""

    # Prepare the request payload
    payload = {
        "model": GROQ_MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_question}
        ],
        "temperature": 0.7,
        "max_tokens": 500,
        "top_p": 1,
        "stream": False
    }

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(GROQ_API_URL, json=payload, headers=headers)
        response.raise_for_status()
        
        result = response.json()
        if 'choices' in result and len(result['choices']) > 0:
            return result['choices'][0]['message']['content'].strip()
        else:
            return "I apologize, but I'm having trouble processing your request right now. Please try again or contact our business directly."
            
    except requests.exceptions.RequestException as e:
        print(f"Groq API error: {e}")
        return "I'm experiencing technical difficulties. Please contact our business directly for assistance."

@app.route('/')
def index():
    return send_from_directory('', 'index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_message = request.json['message']
        
        if not user_message or user_message.strip() == '':
            return jsonify({"answer": "Please provide a question or message."})
        
        # Create context from wine knowledge base (RAG)
        context = create_context_from_knowledge(user_message)
        
        # Get response from Groq API
        bot_response = get_groq_response(user_message, context)
        
        return jsonify({"answer": bot_response})
        
    except Exception as e:
        print(f"Error in chat endpoint: {e}")
        return jsonify({"answer": "I apologize, but I'm experiencing technical difficulties. Please try again or contact our business directly."})

if __name__ == '__main__':
    if not GROQ_API_KEY:
        print("Warning: GROQ_API_KEY not found in environment variables.")
        print("Please create a .env file with your Groq API key.")
    
    app.run(debug=True)
