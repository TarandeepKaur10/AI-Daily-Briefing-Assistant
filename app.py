import os
import requests
import streamlit as st
import yfinance as yf
from datetime import datetime
from dotenv import load_dotenv

from ddgs import DDGS
from deep_translator import GoogleTranslator

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent, Tool, AgentType
from langchain.memory import ConversationBufferMemory

# ── ENV ─────────────────────────────
load_dotenv(".env1")

gemini_key = os.getenv("GEMINI_API_KEY")
weather_key = os.getenv("WEATHER_API_KEY")
news_api_key = os.getenv("NEWS_API_KEY")

# ── LLM ─────────────────────────────
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=gemini_key,
    temperature=0.7,
)

# ── FUNCTIONS ───────────────────────
def get_weather(city):
    try:
        url = f"http://api.weatherapi.com/v1/current.json?key={weather_key}&q={city}"
        data = requests.get(url).json()
        c = data["current"]
        return f"{city}: {c['condition']['text']}, {c['temp_c']}°C"
    except:
        return "Weather error"

def get_stock_price(ticker):
    try:
        stock = yf.Ticker(ticker)
        price = stock.history(period="1d")["Close"].iloc[-1]
        return f"{ticker}: ₹{price:.2f}"
    except:
        return "Stock error"

def get_cricket_news(team):
    try:
        url = f"https://newsapi.org/v2/everything?q=cricket+{team}&apiKey={news_api_key}"
        articles = requests.get(url).json()["articles"][:3]
        return [(a["title"], a["url"]) for a in articles]
    except:
        return [("News error", "#")]

def ddg_search(query):
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=3))
            return [(r["title"], r["href"]) for r in results]
    except:
        return [("Search error", "#")]

def calculator_tool(exp):
    try:
        return str(eval(exp))
    except:
        return "Error"

def translate(text):
    try:
        return GoogleTranslator(source='auto', target='fr').translate(text)
    except:
        return "Translation error"

# ── AGENT ───────────────────────────
tools = [
    Tool("Weather", get_weather, "Weather info"),
    Tool("Stock", get_stock_price, "Stock price"),
    Tool("News", get_cricket_news, "Cricket news"),
]

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memory,
    verbose=False,
)

# ── UI ──────────────────────────────
st.set_page_config(page_title="AI Daily Briefing", page_icon="🧠")

st.title("🧠 AI Daily Briefing Assistant")
st.caption("Weather 🌤️ | Stocks 📈 | Cricket 🏏 | AI Tools")

# INPUTS
city = st.text_input("Enter City", "Chandigarh")
stock = st.text_input("Enter Stock", "RELIANCE.NS")
team = st.text_input("Enter Cricket Team", "India")

search_q = st.text_input("🔍 Search anything")
math_exp = st.text_input("🧮 Calculation (e.g. 273*42)")
translate_text = st.text_input("🌍 Translate text into French")

if st.button("Generate Report 🚀"):

    # AI summary
    prompt = f"Weather in {city}, stock {stock}, cricket news {team}"
    result = agent.invoke({"input": prompt})
    summary = result["output"]

    st.subheader("🧠 AI Summary")
    st.success(summary)

    # WEATHER
    st.subheader("🌤️ Weather")
    st.info(get_weather(city))

    # STOCK
    st.subheader("📈 Stock")
    st.info(get_stock_price(stock))

    # NEWS
    st.subheader("🏏 Cricket News")
    for title, link in get_cricket_news(team):
        st.markdown(f"• [{title}]({link})")

    # SEARCH
    if search_q:
        st.subheader("🔍 Search Results")
        for title, link in ddg_search(search_q):
            st.markdown(f"• [{title}]({link})")

    # CALCULATOR
    if math_exp:
        st.subheader("🧮 Calculator")
        st.info(f"{math_exp} = {calculator_tool(math_exp)}")

    # TRANSLATION
    if translate_text:
        st.subheader("🇫🇷 Translation")
        st.info(f"'{translate_text}' → {translate(translate_text)}")

    st.success("✅ Report Generated Successfully!")