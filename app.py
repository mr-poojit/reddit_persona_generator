
import streamlit as st
from reddit_scraper import scrape_user_data
from persona_builder import build_persona
from utils import extract_username, save_output
from streamlit_lottie import st_lottie
import requests

# Load Lottie animations
def load_lottie_url(url: str):
    try:
        res = requests.get(url)
        if res.status_code == 200:
            return res.json()
    except:
        return None

# Load animations once
if "loading_anim" not in st.session_state:
    st.session_state.loading_anim = load_lottie_url("https://assets10.lottiefiles.com/packages/lf20_usmfx6bp.json")
if "success_anim" not in st.session_state:
    st.session_state.success_anim = load_lottie_url("https://assets10.lottiefiles.com/private_files/lf30_m6j5igxb.json")

# Theme state
if "theme" not in st.session_state:
    st.session_state.theme = "light"

# Emoji Theme Button
col1, col2 = st.columns([0.9, 0.1])
with col2:
    theme_emoji = "🌙" if st.session_state.theme == "light" else "🌞"
    if st.button(theme_emoji):
        st.session_state.theme = "dark" if st.session_state.theme == "light" else "light"

# Apply theme styles
def set_theme_css(theme):
    return f"""
    <style>
    body {{
        background-color: {"#0e1117" if theme == "dark" else "#ffffff"};
        color: {"#fff" if theme == "dark" else "#000"};
    }}
    .title {{
        font-size: 40px;
        font-weight: 900;
        text-align: center;
        color: {"#FF4B4B" if theme == "light" else "#FF8686"};
    }}
    .subtitle {{
        text-align: center;
        font-size: 18px;
        color: {"#333" if theme == "light" else "#aaa"};
        margin-bottom: 25px;
    }}
    .stButton>button {{
        background: linear-gradient(to right, #fc466b, #3f5efb);
        color: white;
        font-weight: bold;
        padding: 0.6em 1.5em;
        border-radius: 12px;
        border: none;
    }}
    .stButton>button:hover {{
        background: linear-gradient(to right, #3f5efb, #fc466b);
    }}
    .stDownloadButton>button {{
        background: #00C851;
        color: white;
        font-weight: bold;
        border-radius: 12px;
    }}
    </style>
    """

st.markdown(set_theme_css(st.session_state.theme), unsafe_allow_html=True)

# Title and subtitle
st.markdown('<div class="title">🧠 Reddit Persona Generator</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">🚀 Powered by Gemini 1.5 Flash · Built by '
    '<a href="https://poojit-nagaloti.netlify.app/" target="_blank" style="color:#FF4B4B;font-weight:bold;text-decoration:none;">Poozzitt</a>'
    '</div>',
    unsafe_allow_html=True
)

# Input URL
reddit_url = st.text_input("🔗 Enter a Reddit Profile URL", placeholder="https://www.reddit.com/user/poozzitt/")

# Action
if st.button("✨ Generate Persona"):
    if not reddit_url.strip():
        st.error("❌ Please enter a valid Reddit profile URL.")
    else:
        try:
            username = extract_username(reddit_url)

            with st.spinner(f"🔍 Scraping posts and comments for u/{username}..."):
                st_lottie(st.session_state.loading_anim, height=150, key="loading1")
                posts = scrape_user_data(username)

            with st.spinner("🤖 Generating persona using Gemini..."):
                st_lottie(st.session_state.loading_anim, height=150, key="loading2")
                persona = build_persona(username, posts)
                save_output(username, persona)

            st.success(f"✅ Persona generated for u/{username}!")
            st_lottie(st.session_state.success_anim, height=150, key="success")

            st.subheader("📝 Generated Persona")
            st.markdown(persona)

            st.download_button(
                label="📥 Download Persona (.txt)",
                data=persona,
                file_name=f"{username}_persona.txt",
                mime="text/plain",
            )
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
