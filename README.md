# 🧠 AI Smart Search Engine

AI Smart Search is an intelligent search application that combines multiple data sources to give complete information about any topic in one place.

Instead of just showing links like a normal search engine, this app provides a **summary, latest news, related links, and images** using AI and APIs.

---

## 🌟 Overview

This project is designed to enhance the traditional search experience by integrating AI with real-time data.

When a user searches for a topic, the system:

• Generates a simple AI-based summary  
• Fetches latest news articles  
• Retrieves related web links  
• Displays relevant images  

Everything is shown in a clean and interactive UI.

---

## 💼 Features

### 🧠 AI Summary
Uses Google Gemini API to generate a simple and easy-to-understand explanation of the topic.

### 📰 Latest News
Fetches real-time news using NewsAPI and displays top articles.

### 🔗 Related Links
Uses SerpAPI to show relevant search results with descriptions.

### 🖼️ Image Results
Displays related images for better understanding of the topic.

### 🎨 Modern UI
Built with Streamlit and custom CSS for a clean, tech-style interface.

---

## 🛠️ Technologies Used

• Python  
• Streamlit  
• Google Gemini API  
• NewsAPI  
• SerpAPI  
• Requests  
• dotenv  

---

## 📁 Project Structure

ai_smart_search/

app.py → Main Streamlit application  
requirements.txt → Dependencies  
.env → API keys (not uploaded)  

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
git clone https://github.com/Venkatesh-Daggu/ai_smart_search.git  
cd ai_smart_search  

---

### 2️⃣ Create virtual environment
python -m venv venv  
venv\Scripts\activate  

---

### 3️⃣ Install dependencies
pip install -r requirements.txt  

---

### 4️⃣ Add API keys

Create a `.env` file and add:

GEMINI_API_KEY=your_gemini_key  
NEWS_API_KEY=your_newsapi_key  
SERPAPI_KEY=your_serpapi_key  

---

### 5️⃣ Run the application
streamlit run app.py  

---

## ⚠️ Important Notes

• Gemini API has free usage limits (429 error may occur)  
• NewsAPI has request limits  
• SerpAPI may require API credits  

---

## 🚀 Future Improvements

• Voice search support  
• Dark/light theme toggle  
• Personalized search results  
• Search history feature  
• Better ranking of results  

---

## 💡 How it works

1. User enters a search query  
2. Gemini generates summary  
3. NewsAPI fetches latest articles  
4. SerpAPI provides links and images  
5. Results are displayed in structured format  

---

## 🎯 Use Case

This project is useful for:

• Students for quick topic understanding  
• Researchers for gathering information  
• Anyone who wants all search data in one place  
