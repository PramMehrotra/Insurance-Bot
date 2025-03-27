# 🏦 GenAI Insurance Bot with Ollama API

## 🚀 Overview
This **GenAI-powered Insurance Bot** utilizes the **Ollama API** to process user queries related to insurance policies, claims, and FAQs. The bot integrates NLP capabilities to provide accurate, context-aware responses in real time, enhancing customer support and automating insurance-related tasks.

## 🛠️ Features
- **Policy Recommendations**: Suggests insurance plans based on user needs.
- **Claims Assistance**: Guides users through claim filing and status checks.
- **FAQ Automation**: Answers common insurance-related questions.
- **Document Analysis**: Extracts key details from uploaded policy documents.
- **Conversational AI**: Provides human-like, context-aware interactions.

## 📌 Tech Stack

- **Python** (FastAPI / Flask)
- **Ollama API** (LLM processing)
- **LangChain** (Conversational memory & RAG)
- **Vector Database** (FAISS / Pinecone) for efficient retrieval
- **PostgreSQL / MongoDB** (Data storage)

## 🔧 Setup & Installation
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/yourusername/genai-insurance-bot.git
cd genai-insurance-bot
```

### 2️⃣ Set Up Virtual Environment
```sh
conda create -p ./venv python=3.10 -y
conda activate ./venv
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables
Create a `.env` file in the root directory and add:
```ini
OPENAI_API_KEY=your_openai_api_key
LANGCHAIN_API_KEY=your_langchain_api_key
OLLAMA_API_KEY=your_ollama_api_key
LANGCHAIN_PROJECT=your_project_name
```

### 5️⃣ Run the Backend Server
```sh
python app.py
```

### 6️⃣ Run the Frontend (if applicable)
```sh
cd frontend
npm install
npm run dev
```

## 📡 API Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/chat` | POST | Process user queries |
| `/policy-recommendation` | GET | Suggests insurance policies |
| `/claims-status` | GET | Fetches claim status |
| `/upload-doc` | POST | Analyzes policy documents |

## 🏗️ Future Enhancements
- Multi-language support 🌍
- Voice-enabled interactions 🎙️
- Integration with CRM & insurance databases 📊
- AI-powered fraud detection 🔍

## 🤝 Contributing
Feel free to fork the repo, raise issues, and submit PRs. Let’s build the future of AI-driven insurance together! 🚀


---
📩 **Need Help?** Reach out via [email@example.com](mailto:email@example.com)

