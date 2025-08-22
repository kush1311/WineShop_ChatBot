# 🍷 Wine Shop ChatBot

A sophisticated, AI-powered conversational assistant for wine shops that combines Retrieval-Augmented Generation (RAG) with Groq's powerful language models to provide intelligent, contextually relevant responses about wines, services, and business operations.

## ✨ Features

- **🤖 AI-Powered Responses**: Uses Groq's LLM for natural, conversational interactions
- **🔍 RAG Implementation**: Retrieves relevant information from your wine knowledge base
- **🎨 Modern UI**: Beautiful, responsive design with wine-themed aesthetics
- **💬 Real-time Chat**: Interactive chat interface with typing indicators
- **📱 Mobile Responsive**: Optimized for both desktop and mobile devices
- **⚡ Fast Performance**: Quick responses using Groq's optimized models
- **🎯 Smart Suggestions**: Quick-access suggestion chips for common questions

## 🚀 Technology Stack

- **Backend**: Flask (Python)
- **AI/LLM**: Groq API with RAG implementation
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Styling**: Modern CSS with gradients, animations, and glassmorphism
- **Fonts**: Google Fonts (Playfair Display, Inter)
- **Icons**: Font Awesome 6

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.7 or higher
- Groq API key (get one at [console.groq.com](https://console.groq.com/))

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd WineShop_ChatBot-main
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Create a `.env` file in the project root:
```env
GROQ_API_KEY=your_actual_groq_api_key_here
```

### 4. Run the Application
```bash
python app.py
```

The chatbot will be available at `http://localhost:5000`

## 🔧 How It Works

### RAG (Retrieval-Augmented Generation) Process

1. **User Query**: Customer asks a question about wines, services, etc.
2. **Context Retrieval**: System searches your wine knowledge base for relevant information
3. **AI Generation**: Relevant context + user question sent to Groq's LLM
4. **Intelligent Response**: AI generates natural, contextual answer combining your business data with wine expertise

### Architecture Components

- **Knowledge Base**: `Sample Question Answers.json` contains your wine shop's Q&A data
- **Context Engine**: Intelligent keyword matching and relevance scoring
- **AI Integration**: Groq API with llama3-8b-8192 model
- **Web Interface**: Modern, responsive chat UI with real-time interactions

## 🎨 UI Features

- **Wine-Themed Design**: Elegant color scheme with burgundy accents
- **Glassmorphism Effects**: Modern backdrop blur and transparency
- **Smooth Animations**: Message transitions, typing indicators, and hover effects
- **Professional Typography**: Playfair Display for headings, Inter for body text
- **Interactive Elements**: Suggestion chips, typing indicators, and smooth scrolling

## 📊 API Configuration

- **Model**: `llama3-8b-8192` (fast and efficient)
- **Temperature**: 0.7 (balanced creativity and accuracy)
- **Max Tokens**: 500 (concise but informative responses)
- **Context Window**: Top 3 most relevant knowledge base entries

## 🚀 Benefits

- **Enhanced Customer Experience**: Natural, engaging conversations
- **Improved Accuracy**: Contextual responses based on your business data
- **Professional Appearance**: Modern, trustworthy interface
- **Scalable Knowledge**: Easy to update and expand wine information
- **Cost-Effective**: Efficient use of AI tokens with RAG approach

## 📁 Project Structure

```
WineShop_ChatBot-main/
├── app.py                 # Flask backend with Groq API integration
├── index.html            # Modern, responsive chat interface
├── requirements.txt      # Python dependencies
├── SETUP.md             # Detailed setup instructions
├── Sample Question Answers.json  # Wine knowledge base
└── README.md            # This file
```

## 🔒 Security & Best Practices

- API keys stored in environment variables (not hardcoded)
- Input validation and sanitization
- Error handling with graceful fallbacks
- Secure API communication with HTTPS

## 🐛 Troubleshooting

- **API Key Issues**: Ensure `.env` file exists and contains valid Groq API key
- **Dependencies**: Run `pip install -r requirements.txt` to install all packages
- **Knowledge Base**: Verify `Sample Question Answers.json` exists and is properly formatted
- **Port Conflicts**: Change port in `app.py` if 5000 is already in use

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For technical support or questions:
- Check the troubleshooting section above
- Review the SETUP.md file for detailed instructions
- Ensure your Groq API key has sufficient credits

---

**Built with ❤️ for wine enthusiasts and shop owners**

