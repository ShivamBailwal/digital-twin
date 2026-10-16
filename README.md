# 🤖 AI Digital Twin — Portfolio Chatbot

An AI-powered digital twin that represents my professional profile and interacts with visitors through a conversational chatbot. It answers questions about my background, technical skills, projects, and experience using personalized context and AI-powered tool calling.

## 🚀 Overview

The **AI Digital Twin** acts as a virtual version of my professional portfolio, allowing recruiters, developers, and potential collaborators to learn about my profile through natural conversations.

Instead of browsing a traditional portfolio, visitors can ask questions and receive contextual responses from an AI assistant designed to represent my professional background.

## ✨ Features

- **AI-Powered Conversations:** Answers questions about professional background, skills, projects, and experience.
- **Personalized Context:** Uses profile summaries and LinkedIn information to generate relevant responses.
- **PDF Context Extraction:** Extracts professional information from a LinkedIn PDF using PyPDF.
- **Tool Calling:** Uses AI function calling to perform specific actions during conversations.
- **Contact Collection:** Records email addresses and relevant details from interested visitors.
- **Unknown Question Tracking:** Saves unanswered questions for future improvements.
- **Interactive Chat Interface:** Provides a conversational interface using Gradio.
- **Cloud Deployment Support:** Includes Render configuration for deployment.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Gradio | Interactive chatbot interface |
| Gemini API | Language model for generating responses |
| OpenAI Python SDK | OpenAI-compatible API integration and tool calling |
| PyPDF | Extracting text from PDF documents |
| python-dotenv | Environment variable management |
| Requests | HTTP request support |

## 🏗️ Architecture

```text
                  ┌─────────────────────┐
                  │       Visitor       │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │   Gradio Chat UI    │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │   Chat Handler      │
                  │     (app.py)        │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │   Gemini API        │
                  │  + Tool Calling     │
                  └──────────┬──────────┘
                             │
                   ┌─────────┴─────────┐
                   ▼                   ▼
          ┌────────────────┐  ┌─────────────────┐
          │ Profile Context│  │   Tool Handler  │
          │   context.py   │  │    tools.py     │
          └────────────────┘  └────────┬────────┘
                                       │
                              ┌────────┴─────────┐
                              ▼                  ▼
                       Contact Details     Unknown Questions
```

## 📂 Project Structure

```text
digital-twin/
│
├── app.py             # Main application and chat handler
├── context.py         # Profile context and system prompt
├── tools.py           # Tool definitions and execution
├── styles.py          # Custom interface styling and examples
├── requirements.txt   # Python dependencies
├── render.yaml        # Render deployment configuration
├── .python-version    # Python version configuration
├── .gitignore         # Git ignore rules
│
├── summary.txt        # Optional professional summary
├── linkedin.pdf       # Optional LinkedIn profile PDF
├── details.txt        # Generated contact details
└── unknown_questions.txt # Generated unanswered questions
```

The last three data files are optional or generated at runtime; they may not exist in a fresh clone.

## ⚙️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/ShivamBailwal/digital-twin.git

cd digital-twin
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

On macOS or Linux:

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key

SUMMARY_TEXT="Your professional summary, skills, projects, and experience"

LINKEDIN_TEXT="Your LinkedIn profile information"
```

Get your API key from [Google AI Studio](https://aistudio.google.com/).

**Important:** Keep your API key private. Never commit your `.env` file or expose credentials in your public repository.

You can also provide profile context through `summary.txt` and `linkedin.pdf`. The application reads the environment variables first and falls back to those files when the corresponding variables are not set.

### 5. Run the Application

```bash
python app.py
```

Open the local URL shown in your terminal, typically:

```text
http://localhost:7860
```

## 🔄 How It Works

1. A visitor sends a message through the Gradio chat interface.
2. The application combines the conversation history with the digital twin's system prompt.
3. The Gemini model generates a response using the configured professional context.
4. If the model requests a tool call, the application executes the corresponding Python function.
5. Tool results are returned to the model, which generates the final response.
6. Contact details and unanswered questions are recorded in local text files when the corresponding tools are called.

## 🧰 Available Tools

### `record_user_details`

Records contact information when a visitor wants to get in touch.

- Email address
- Name, when provided
- Notes about the conversation

### `record_unknown_question`

Records questions the digital twin cannot answer, helping identify missing profile information and opportunities to improve the system prompt.

## ☁️ Deployment

The repository includes a `render.yaml` configuration for deployment on Render.

1. Push the project to GitHub.
2. Create a new web service on [Render](https://render.com/).
3. Connect the repository.
4. Configure the required environment variables:
   - `GEMINI_API_KEY`
   - `SUMMARY_TEXT`
   - `LINKEDIN_TEXT`
5. Deploy the application using the configured build and start commands.

**Deployment note:** The application writes contact information and unanswered questions to local text files. On hosting platforms with ephemeral filesystems, these records may not persist across restarts or redeployments. Use persistent storage or a database if durable storage is required.

## 🔮 Future Improvements

- Add persistent storage for conversations and contact details.
- Introduce retrieval-augmented generation (RAG) for larger professional knowledge bases.
- Add conversation memory across sessions.
- Improve error handling and API quota management.
- Add analytics to understand common recruiter questions.
- Improve deployment security and data validation.

## 🎯 Project Goal

To create an interactive AI-powered portfolio that demonstrates practical experience with LLM integration, prompt engineering, tool calling, Python application development, and conversational AI.

## 👨‍💻 Author

**Shivam Bailwal**

- GitHub: [@ShivamBailwal](https://github.com/ShivamBailwal)
- Project Repository: [digital-twin](https://github.com/ShivamBailwal/digital-twin)

---

⭐ If you find this project interesting, consider giving the repository a star!
