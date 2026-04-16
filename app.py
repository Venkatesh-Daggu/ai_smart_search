import streamlit as st
import requests
import google.generativeai as genai
import os
from dotenv import load_dotenv

# -------------------------------
# LOAD KEYS
# -------------------------------
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
SERPAPI_KEY = os.getenv("SERPAPI_KEY")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

st.set_page_config(page_title="AI Smart Search", page_icon="🧠", layout="wide")

# --------------------------------------------------
# Custom CSS
# --------------------------------------------------
st.markdown("""
<style>
/* ---------- Tech Background ---------- */
.stApp {
    background:
        linear-gradient(rgba(5, 10, 20, 0.78), rgba(5, 10, 20, 0.82)),
        url("https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=1800&q=80");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
    color: white;
}

/* ---------- Main spacing ---------- */
.block-container {
    max-width: 1380px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* ---------- Hero ---------- */
.hero-box {
    background: rgba(10, 16, 28, 0.78);
    border: 1px solid rgba(255,255,255,0.10);
    border-radius: 28px;
    padding: 34px 32px 26px 32px;
    box-shadow: 0 14px 34px rgba(0,0,0,0.32);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    margin-bottom: 26px;
}

.main-title {
    font-size: 58px;
    font-weight: 800;
    color: white;
    margin-bottom: 10px;
    line-height: 1.1;
}

.sub-title {
    font-size: 20px;
    color: #dbeafe;
    line-height: 1.7;
}

/* ---------- Input ---------- */
.stTextInput label {
    color: white !important;
    font-weight: 700;
    font-size: 17px;
}

.stTextInput > div > div > input {
    background: rgba(255,255,255,0.08) !important;
    color: white !important;
    border: 1px solid rgba(255,255,255,0.14) !important;
    border-radius: 16px !important;
    padding: 14px !important;
    font-size: 17px !important;
}

.stTextInput > div > div > input::placeholder {
    color: #d1d5db !important;
}

/* ---------- Button ---------- */
.stButton > button {
    background: linear-gradient(90deg, #2563eb, #7c3aed);
    color: white !important;
    border: none !important;
    border-radius: 16px !important;
    padding: 12px 28px !important;
    font-size: 18px !important;
    font-weight: 700 !important;
    box-shadow: 0 10px 24px rgba(37, 99, 235, 0.30);
}

.stButton > button:hover {
    background: linear-gradient(90deg, #1d4ed8, #6d28d9);
    color: white !important;
}

/* ---------- Helper ---------- */
.helper-text {
    color: #cbd5e1;
    font-size: 14px;
    margin-top: -4px;
    margin-bottom: 18px;
}

/* ---------- Section title ---------- */
.section-title {
    font-size: 34px;
    font-weight: 800;
    color: white;
    margin-top: 14px;
    margin-bottom: 18px;
}

/* ---------- Summary ---------- */
.summary-card {
    background: rgba(8, 15, 30, 0.78);
    border: 1px solid rgba(255,255,255,0.10);
    border-radius: 24px;
    padding: 24px;
    color: white;
    font-size: 18px;
    line-height: 1.9;
    box-shadow: 0 10px 24px rgba(0,0,0,0.22);
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
    margin-bottom: 18px;
}

/* ---------- News cards ---------- */
.news-card {
    background: rgba(8, 15, 30, 0.82);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 18px;
    padding: 16px 18px;
    margin-bottom: 14px;
    box-shadow: 0 8px 18px rgba(0,0,0,0.18);
}

.news-card a {
    color: #bfdbfe !important;
    text-decoration: none;
    font-weight: 600;
    font-size: 18px;
    line-height: 1.6;
}

.news-card a:hover {
    text-decoration: underline;
}

/* ---------- Links ---------- */
.result-card {
    background: rgba(8, 15, 30, 0.84);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 20px;
    padding: 18px 20px;
    margin-bottom: 16px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.18);
}

.result-card a {
    color: #60a5fa !important;
    text-decoration: none;
    font-size: 22px;
    font-weight: 700;
    line-height: 1.5;
}

.result-card a:hover {
    color: #93c5fd !important;
    text-decoration: underline;
}

.result-snippet {
    color: #e5e7eb;
    font-size: 15px;
    line-height: 1.8;
    margin-top: 10px;
}

/* ---------- Images Panel ---------- */
.images-panel {
    background: rgba(8, 15, 30, 0.86);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 26px;
    padding: 24px;
    box-shadow: 0 14px 34px rgba(0,0,0,0.22);
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
}

/* ---------- Hide Streamlit chrome ---------- */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
hr {display: none !important;}
</style>
""", unsafe_allow_html=True)
# -------------------------------
# FUNCTIONS
# -------------------------------
def get_summary(query):
    try:
        res = model.generate_content(
            f"Explain '{query}' in a simple paragraph."
        )
        if res and hasattr(res, "text"):
            return res.text.strip()
        return "No summary generated"
    except Exception as e:
        print("Gemini Error:", e)
        return f"{query} is a trending topic. Summary not available right now."


def get_news(query):
    try:
        url = f"https://newsapi.org/v2/everything?q={query}&apiKey={NEWS_API_KEY}"
        res = requests.get(url, timeout=20).json()

        articles = res.get("articles", [])[:5]

        return {
            str(i + 1): {
                "title": item.get("title"),
                "url": item.get("url")
            }
            for i, item in enumerate(articles)
        }
    except Exception as e:
        print("News Error:", e)
        return {}


def get_links(query):
    try:
        url = f"https://serpapi.com/search.json?q={query}&api_key={SERPAPI_KEY}"
        res = requests.get(url, timeout=20).json()

        results = res.get("organic_results", [])[:5]

        return {
            str(i + 1): {
                "title": item.get("title"),
                "link": item.get("link"),
                "snippet": item.get("snippet", "No description available")
            }
            for i, item in enumerate(results)
        }
    except Exception as e:
        print("Links Error:", e)
        return {}


def get_images(query):
    try:
        url = f"https://serpapi.com/search.json?q={query}&tbm=isch&api_key={SERPAPI_KEY}"
        res = requests.get(url, timeout=20).json()

        images = res.get("images_results", [])
        output = {}
        count = 1

        for item in images:
            img_url = item.get("original") or item.get("thumbnail")
            if not img_url:
                continue

            lower_url = img_url.lower()
            bad_words = ["logo", "icon", "sprite", "svg"]
            if any(word in lower_url for word in bad_words):
                continue

            output[str(count)] = img_url
            count += 1

            if count > 6:
                break

        return output

    except Exception as e:
        print("Images Error:", e)
        return {}

# --------------------------------------------------
# Header
# --------------------------------------------------
st.markdown("""
<div class="hero-box">
    <div class="main-title">🧠 AI Smart Search Engine</div>
</div>
""", unsafe_allow_html=True)

# -------------------------------
# INPUT
# -------------------------------
query = st.text_input("Enter your topic", placeholder="Search for any topic")

if st.button("🔍 Search"):
    if query.strip():
        with st.spinner("Fetching results..."):
            summary = get_summary(query)
            news = get_news(query)
            links = get_links(query)
            images = get_images(query)

        col1, col2 = st.columns(2, gap="large")
        
        with col1:
            st.markdown('<div class="section-title">🧠 Summary</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="summary-card">{summary}</div>', unsafe_allow_html=True)

            st.markdown('<div class="section-title">📰 News</div>', unsafe_allow_html=True)
            if news:
                for key in news:
                    item = news[key]
                    title = item.get("title", "No title")
                    link = item.get("url", "#")

                    st.markdown(f"""
                    <div class="news-card">
                        🔗 <a href="{link}" target="_blank">{title}</a>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.warning("No news found.")

        with col2:
            st.markdown('<div class="section-title">🔗 Related Links</div>', unsafe_allow_html=True)

            if links:
                for key in links:
                    item = links[key]
                    title = item.get("title", "No title")
                    link = item.get("link", "#")
                    snippet = item.get("snippet", "No description available")

                    st.markdown(f"""
                    <div class="result-card">
                        <a href="{link}" target="_blank">🔗 {title}</a>
                        <div class="result-snippet">{snippet}</div>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.warning("No related links found.")

        st.markdown('<div class="section-title">🖼️ Images</div>', unsafe_allow_html=True)
        if images:
            cols = st.columns(3)
            idx = 0
            shown_any = False

            for key in images:
                img_url = images.get(key)
                if not img_url:
                    continue

                with cols[idx]:
                    st.markdown('<div class="image-tile"><div class="image-stage">', unsafe_allow_html=True)
                    try:
                        st.image(img_url, use_container_width=True)
                        shown_any = True
                    except Exception:
                        st.info("Image could not be loaded")
                    st.markdown('</div></div>', unsafe_allow_html=True)

                idx = (idx + 1) % 3

            if not shown_any:
                st.warning("No images could be displayed.")
        else:
            st.warning("No images found.")

        st.markdown('</div>', unsafe_allow_html=True)