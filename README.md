# 🎓 AI Learning Buddy

An AI-powered personal learning assistant built with **Streamlit** and **Google Gemini 2.5 Flash**.  
Ask questions, get crystal-clear explanations, explore real-life examples, and test yourself with auto-generated quizzes — all in one place.

## 🌐 Live App

👉 **[Try AI Learning Buddy Now!](https://ai-learning-buddy-5jwxpcmsetrfvozuynpbwv.streamlit.app/)**

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 📖 **Explain Concept** | Get a clear, simple explanation of any topic |
| 🌍 **Real-Life Example** | See how a concept applies in the real world with engaging examples |
| 📝 **Generate Quiz** | Auto-generated 5-question MCQs to test your understanding |
| 💬 **Ask Anything** | Free-form Q&A — ask whatever you want |
| ⚙️ **Difficulty Levels** | Choose between Beginner 🟢, Intermediate 🟡, or Advanced 🔴 |
| 🌐 **Multi-Language** | Responses in English, Hindi, or Hinglish |

## 🛠️ Tech Stack

- **Frontend / UI** – [Streamlit](https://streamlit.io/) with custom CSS (Inter font, gradient buttons, glassmorphic activity cards)
- **AI Model** – [Google Gemini 2.5 Flash](https://ai.google.dev/) via `google-generativeai` SDK
- **Deployment** – [Streamlit Community Cloud](https://share.streamlit.io)

## 🚀 Deploy on Streamlit Cloud

1. Push this repo to **GitHub**.
2. Go to [share.streamlit.io](https://share.streamlit.io) and connect your repo.
3. Set the **main file** to `app.py`.
4. Under **Settings → Secrets**, add:
   ```toml
   GEMINI_API_KEY = "your-google-gemini-api-key-here"
   ```
5. Click **Deploy** 🎉

## 🔑 Getting a Gemini API Key

1. Visit [Google AI Studio](https://aistudio.google.com/apikey)
2. Click **Create API Key**
3. Copy the key and paste it into Streamlit Secrets

## 🏗️ Run Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Create a secrets file
mkdir -p .streamlit
echo 'GEMINI_API_KEY = "your-key-here"' > .streamlit/secrets.toml

# Launch the app
streamlit run app.py
```

## 📂 Project Structure

```
AI learning buddy/
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies (streamlit, google-generativeai)
├── README.md               # This file
└── .streamlit/
    ├── config.toml         # Theme & server config
    └── secrets.toml        # API key (local only, git-ignored)
```

## 📸 How It Works

1. **Choose settings** — Pick a difficulty level and response language from the sidebar.
2. **Enter a topic** — Type any topic or question in the input field.
3. **Select an activity** — Explain Concept, Real-Life Example, Generate Quiz, or Ask Anything.
4. **Hit Generate** — The AI produces a tailored response instantly.

---

Built with ❤️ by **Tanisha** | Powered by Google Gemini
