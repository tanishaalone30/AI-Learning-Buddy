import streamlit as st
import google.generativeai as genai

# ─── Page Configuration ───
st.set_page_config(
    page_title="AI Learning Buddy – Tanisha",
    page_icon="🎓",
    layout="centered",
    initial_sidebar_state="expanded",
)

# ─── Custom CSS for Premium Look ───
st.markdown(
    """
    <style>
    /* Google Font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    html, body, [class*="st-"] {
        font-family: 'Inter', sans-serif;
    }

    /* Hero header */
    .hero {
        text-align: center;
        padding: 2rem 1rem 1rem;
    }
    .hero h1 {
        font-size: 2.6rem;
        font-weight: 700;
        background: linear-gradient(135deg, #6C63FF, #E942F5);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
    }
    .hero p {
        font-size: 1.05rem;
        color: #888;
        margin-top: 0;
    }

    /* Activity cards */
    .activity-card {
        background: linear-gradient(135deg, #1e1e2f, #2a2a40);
        border: 1px solid #3a3a5c;
        border-radius: 14px;
        padding: 1.2rem 1.4rem;
        margin-bottom: 0.8rem;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .activity-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 24px rgba(108, 99, 255, 0.25);
    }
    .activity-card h3 {
        margin: 0 0 0.3rem;
        color: #c4b5fd;
        font-size: 1.05rem;
    }
    .activity-card p {
        margin: 0;
        color: #9ca3af;
        font-size: 0.88rem;
    }

    /* Response container */
    .response-box {
        background: #1a1a2e;
        border-left: 4px solid #6C63FF;
        border-radius: 0 12px 12px 0;
        padding: 1.4rem 1.6rem;
        margin-top: 1rem;
        color: #e2e2e2;
        line-height: 1.7;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #555;
        font-size: 0.78rem;
        margin-top: 3rem;
        padding-bottom: 1rem;
    }

    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #6C63FF, #E942F5) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 0.6rem 2rem !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        transition: transform 0.15s ease, box-shadow 0.15s ease !important;
    }
    .stButton > button:hover {
        transform: scale(1.03) !important;
        box-shadow: 0 6px 20px rgba(108, 99, 255, 0.4) !important;
    }

    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background: #12121c;
    }
    section[data-testid="stSidebar"] .stMarkdown h2 {
        color: #c4b5fd;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ─── Gemini API Setup (uses Streamlit Cloud Secrets) ───
@st.cache_resource
def get_model():
    """Initialise and cache the Gemini model."""
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    return genai.GenerativeModel("gemini-2.5-flash")


try:
    model = get_model()
except Exception as e:
    st.error(
        "⚠️ Could not initialise Gemini. "
        "Make sure you have added `GEMINI_API_KEY` in **Settings → Secrets** on Streamlit Cloud."
    )
    st.stop()


# ─── Session State ───
if "history" not in st.session_state:
    st.session_state.history = []


# ─── Sidebar ───
with st.sidebar:
    st.markdown("## ⚙️ Settings")

    difficulty = st.selectbox(
        "Difficulty Level",
        ["Beginner 🟢", "Intermediate 🟡", "Advanced 🔴"],
        index=0,
    )

    language = st.selectbox(
        "Response Language",
        ["English", "Hindi", "Hinglish"],
        index=0,
    )

    st.divider()
    st.markdown("## 📜 History")

    if st.session_state.history:
        for i, item in enumerate(reversed(st.session_state.history[-10:])):
            with st.expander(f"{'📖' if item['activity']=='Explain Concept' else '🌍' if item['activity']=='Real-Life Example' else '📝' if item['activity']=='Generate Quiz' else '💬'} {item['topic'][:30]}"):
                st.caption(f"**Activity:** {item['activity']}")
                st.markdown(item["response"][:300] + ("…" if len(item["response"]) > 300 else ""))
    else:
        st.caption("Your learning history will appear here.")

    st.divider()
    if st.button("🗑️ Clear History"):
        st.session_state.history = []
        st.rerun()


# ─── Hero Section ───
st.markdown(
    """
    <div class="hero">
        <h1>🎓 AI Learning Buddy</h1>
        <p>Your personal AI tutor — powered by Google Gemini</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ─── Activity Descriptions ───
ACTIVITIES = {
    "Explain Concept": {
        "icon": "📖",
        "desc": "Get a clear, simple explanation of any topic.",
        "prompt": "Explain {topic} in simple language for a {level} learner. Respond in {lang}.",
    },
    "Real-Life Example": {
        "icon": "🌍",
        "desc": "See how a concept applies in the real world.",
        "prompt": "Give two engaging real-life examples of {topic} that a {level} learner can relate to. Respond in {lang}.",
    },
    "Generate Quiz": {
        "icon": "📝",
        "desc": "Test yourself with auto-generated MCQs.",
        "prompt": "Create 5 multiple-choice questions on {topic} for a {level} learner. Include the correct answer after each question. Respond in {lang}.",
    },
    "Ask Anything": {
        "icon": "💬",
        "desc": "Free-form question — ask whatever you want!",
        "prompt": "{topic}. Adjust your answer for a {level} learner. Respond in {lang}.",
    },
}

# ─── Show activity cards ───
cols = st.columns(4)
for idx, (name, info) in enumerate(ACTIVITIES.items()):
    with cols[idx]:
        st.markdown(
            f"""
            <div class="activity-card">
                <h3>{info['icon']} {name}</h3>
                <p>{info['desc']}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.write("")

# ─── Input Area ───
col_input, col_select = st.columns([3, 1.5])

with col_input:
    topic = st.text_input(
        "📖 Enter a Topic or Question",
        placeholder="e.g. Photosynthesis, Newton's Laws, Python loops …",
    )

with col_select:
    option = st.selectbox(
        "🎯 Activity",
        list(ACTIVITIES.keys()),
    )

# ─── Generate ───
generate_btn = st.button("🪄 Generate", use_container_width=True)

if generate_btn:
    if not topic.strip():
        st.warning("⚠️ Please enter a topic or question first.")
    else:
        level = difficulty.split()[0]  # e.g. "Beginner"

        prompt = ACTIVITIES[option]["prompt"].format(
            topic=topic, level=level, lang=language
        )

        with st.spinner("✨ Generating your response …"):
            try:
                response = model.generate_content(prompt)
                answer = response.text

                # Save to history
                st.session_state.history.append(
                    {
                        "topic": topic,
                        "activity": option,
                        "response": answer,
                    }
                )

                st.markdown(
                    f'<div class="response-box">{answer}</div>',
                    unsafe_allow_html=True,
                )

                # Also render with st.markdown for proper markdown formatting
                with st.expander("📄 View formatted response", expanded=True):
                    st.markdown(answer)

            except Exception as exc:
                st.error(f"❌ Something went wrong: {exc}")

# ─── Show last response if page re-renders ───
elif st.session_state.history:
    last = st.session_state.history[-1]
    st.markdown("#### 🕘 Last Response")
    st.caption(f"**Topic:** {last['topic']}  •  **Activity:** {last['activity']}")
    with st.expander("📄 View response", expanded=False):
        st.markdown(last["response"])



