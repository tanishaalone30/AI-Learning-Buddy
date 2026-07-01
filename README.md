# 🎓 AI Learning Buddy – Tanisha

An AI-powered learning assistant built with **Streamlit** and **Google Gemini 2.5 Flash**.  
Ask questions, get explanations, explore real-life examples, and test yourself with auto-generated quizzes.

## ✨ Features

| Feature | Description |
|---------|-------------|
| 📖 **Explain Concept** | Get beginner-friendly explanations of any topic |
| 🌍 **Real-Life Example** | See how concepts apply in everyday life |
| 📝 **Generate Quiz** | Auto-generated MCQs to test your understanding |
| 💬 **Ask Anything** | Free-form Q&A with the AI |
| ⚙️ **Difficulty Levels** | Beginner / Intermediate / Advanced |
| 🌐 **Multi-Language** | English, Hindi, Hinglish support |
| 📜 **History** | Track your recent learning sessions |

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
pip install -r requirements.txt

# Create a secrets file
mkdir -p .streamlit
echo 'GEMINI_API_KEY = "your-key-here"' > .streamlit/secrets.toml

streamlit run app.py
```

## 📂 Project Structure

```
AI learning buddy/
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── README.md               # This file
└── .streamlit/
    ├── config.toml         # Theme & server config
    └── secrets.toml        # API key (local only, git-ignored)
```

---

Built with ❤️ by **Tanisha** | Powered by Google Gemini
