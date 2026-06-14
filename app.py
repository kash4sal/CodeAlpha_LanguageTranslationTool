import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(
    page_title="AI Language Translator",
    page_icon="🌍",
    layout="wide"
)

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>

.main {
    background: linear-gradient(135deg,#0f172a,#111827);
}

h1 {
    text-align:center;
    font-size:55px !important;
    background: linear-gradient(90deg,#4f9cff,#c86cff);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

.subtitle{
    text-align:center;
    font-size:20px;
    color:#d1d5db;
    margin-bottom:30px;
}

.block-container{
    padding-top:2rem;
}

.stTextArea textarea{
    border-radius:20px;
    border:2px solid #6d5dfc;
    font-size:18px;
}

.stSelectbox div[data-baseweb="select"]{
    border-radius:15px;
}

.stButton button{
    width:100%;
    height:60px;
    border:none;
    border-radius:15px;
    font-size:22px;
    font-weight:bold;
    background: linear-gradient(90deg,#4f9cff,#c86cff);
    color:white;
}

.stButton button:hover{
    transform:scale(1.02);
    transition:0.3s;
}

.result-box{
    background:rgba(0,255,150,0.1);
    border:1px solid rgba(0,255,150,0.3);
    border-radius:15px;
    padding:20px;
    font-size:26px;
    color:white;
}

.feature-card{
    background:rgba(255,255,255,0.05);
    padding:20px;
    border-radius:20px;
    text-align:center;
    height:180px;
}

.footer{
    text-align:center;
    color:#9ca3af;
    margin-top:40px;
}

</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("<h1>🌍 AI Language Translation Tool</h1>", unsafe_allow_html=True)

st.markdown("""
<div class='subtitle'>
Translate text between multiple languages instantly using AI
</div>
""", unsafe_allow_html=True)

# ---------- LANGUAGES ----------
languages = {
    "English":"en",
    "Hindi":"hi",
    "French":"fr",
    "Spanish":"es",
    "German":"de",
    "Arabic":"ar",
    "Japanese":"ja",
    "Chinese":"zh-CN",
    "Russian":"ru",
    "Urdu":"ur"
}

# ---------- INPUT CARD ----------
st.markdown("### ✍ Enter Text")

text = st.text_area(
    "",
    height=200,
    placeholder="Type your text here..."
)

col1,col2 = st.columns(2)

with col1:
    source_lang = st.selectbox(
        "🌐 Source Language",
        list(languages.keys())
    )

with col2:
    target_lang = st.selectbox(
        "🎯 Target Language",
        list(languages.keys()),
        index=1
    )

# ---------- TRANSLATE ----------
if st.button("🚀 Translate"):

    if text.strip():

        try:

            translated = GoogleTranslator(
                source=languages[source_lang],
                target=languages[target_lang]
            ).translate(text)

            st.markdown("## ✅ Translation Result")

            st.markdown(
                f"""
                <div class='result-box'>
                {translated}
                </div>
                """,
                unsafe_allow_html=True
            )

            st.success("Translation completed successfully!")

        except Exception as e:
            st.error(str(e))

    else:
        st.warning("Please enter text.")

# ---------- FEATURES ----------
st.markdown("<br>", unsafe_allow_html=True)

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class='feature-card'>
    <h2>⚡</h2>
    <h4>Fast</h4>
    <p>Instant translation in seconds</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class='feature-card'>
    <h2>🌎</h2>
    <h4>Multi Language</h4>
    <p>Supports multiple languages</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class='feature-card'>
    <h2>🔒</h2>
    <h4>Secure</h4>
    <p>Your text remains private</p>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class='feature-card'>
    <h2>✨</h2>
    <h4>User Friendly</h4>
    <p>Clean and modern interface</p>
    </div>
    """, unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown("""
<div class='footer'>
Developed by Kashish Salman Ali | CodeAlpha AI Internship
</div>
""", unsafe_allow_html=True)