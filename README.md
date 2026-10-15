# EduTutor AI – Personalized Adaptive Learning Companion

**An AI-powered study assistant built by Team Phoneix**

EduTutor AI is a web-based learning assistant designed to help students study more efficiently using their own learning materials. It brings document upload, AI-assisted question answering, quiz generation, and study summaries together in one simple interface.

## 🎥 Demo Video

https://youtu.be/Gs7R3BBPaI4


## ✨ Features

- **📚 Document Upload:** Upload study materials in PDF, PPTX, DOCX, and TXT formats.
- **🤖 AI Tutor:** Ask questions related to your uploaded learning materials.
- **📝 Practice Quiz Generator:** Generate practice questions with configurable question counts and difficulty levels.
- **📖 Study Summaries:** Create concise summaries to support revision.
- **🔎 Relevant Content Retrieval:** Use text retrieval techniques to find relevant passages from uploaded documents.
- **💻 Simple Web Interface:** Access the learning tools through a Flask-based web application.

*Note: AI-generated features require a correctly configured and running language model.*

## 🛠️ Technologies Used

- Python
- Flask
- HTML
- CSS
- JavaScript
- TF-IDF Vectorization
- Cosine Similarity
- Document Processing Libraries
- Ollama and Llama 3.2 3B (for local AI integration, when configured)

## 🧠 How It Works

1. **Upload:** The student uploads a supported study document.
2. **Extract:** The application extracts text from the document.
3. **Chunk:** The text is divided into smaller passages.
4. **Retrieve:** TF-IDF and cosine similarity help identify passages relevant to a question.
5. **Generate:** The configured language model can use the relevant content to produce answers, quizzes, and summaries.

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.10 or newer
- Git
- Ollama, if using the local language model configuration

### 1. Clone the repository

```bash
git clone https://github.com/Prathapsri/EduTutor-AI.git
cd EduTutor-AI
```

### 2. Create a virtual environment

**Windows:**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use Command Prompt and run:

```bat
venv\Scripts\activate.bat
```

### 3. Install dependencies

If the repository contains a `requirements.txt` file, run:

```bash
pip install -r requirements.txt
```

### 4. Configure the AI model

For a local Ollama setup, install Ollama and download the model:

```bash
ollama pull llama3.2:3b
```

Configure the environment variables according to your application's implementation. For example, if your code uses an OpenAI-compatible Ollama endpoint:

```dotenv
OPENAI_API_KEY=ollama
OPENAI_BASE_URL=http://localhost:11434/v1
OPENAI_MODEL=llama3.2:3b
```

Make sure your Python code reads these variables and passes the base URL to the AI client. Do not commit API keys or other secrets to GitHub.

### 5. Run the application

```bash
python app.py
```

Open the local URL displayed in your terminal, commonly:

`http://127.0.0.1:5000`

## 📂 Supported Document Formats

| Format | Extension |
|---|---|
| PDF | `.pdf` |
| PowerPoint | `.pptx` |
| Word document | `.docx` |
| Plain text | `.txt` |

## 🚀 Future Improvements

- Persistent storage for uploaded study materials
- Semantic search and improved document retrieval
- Answers with source references
- User accounts and personalized learning history
- Multilingual learning support
- Improved quiz evaluation and learning recommendations

## 🎯 Project Goal

Our goal is to make studying more interactive, organized, and accessible by helping students transform their existing learning materials into useful revision resources.

## 👥 Team

**Team Name:** Team Phoneix

**Project:** EduTutor AI – Personalized Adaptive Learning Companion

## 📌 Project Repository

[GitHub – EduTutor-AI](https://github.com/Prathapsri/EduTutor-AI)

---

Built with ❤️ by Team Phoneix.
