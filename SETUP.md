# Wine Shop ChatBot Setup with Groq API

## Prerequisites
- Python 3.7 or higher
- Groq API key (get one at https://console.groq.com/)

## Installation

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up your Groq API key:**
   Create a `.env` file in the project root with:
   ```
   GROQ_API_KEY=your_actual_groq_api_key_here
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```

## How it Works

This chatbot now uses **Retrieval-Augmented Generation (RAG)** with Groq's LLM:

1. **Context Retrieval**: When a user asks a question, the system searches through your wine knowledge base to find relevant information
2. **AI Generation**: The relevant context is sent to Groq's API along with the user's question
3. **Intelligent Response**: Groq generates a natural, contextual response using both your specific wine shop knowledge and general wine expertise

## Benefits of RAG + Groq

- **More Natural Responses**: Unlike simple keyword matching, responses are conversational and contextual
- **Better Understanding**: The AI can handle complex questions and provide nuanced answers
- **Knowledge Expansion**: Combines your specific business data with general wine knowledge
- **Fast Performance**: Groq's API provides quick responses for real-time chat

## API Models Used

- **Model**: `llama3-8b-8192` (fast and efficient)
- **Temperature**: 0.7 (balanced creativity and accuracy)
- **Max Tokens**: 500 (concise but informative responses)

## Troubleshooting

- Ensure your `.env` file is in the project root
- Verify your Groq API key is valid and has sufficient credits
- Check that `Sample Question Answers.json` exists and is properly formatted
