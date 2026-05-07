# 🧠 AI Daily Briefing Assistant

An AI-powered dashboard that provides **daily insights in one place** — including Weather 🌤️, Stock Prices 📈, and Cricket News 🏏 — enhanced with intelligent tools like search, calculation, and translation.

---

## 🚀 Features

- 🌤️ **Real-time Weather Updates**  
  Get current weather conditions for any city using Weather API.

- 📈 **Stock Market Tracking**  
  Fetch latest stock prices using yFinance.

- 🏏 **Cricket News Aggregation**  
  Stay updated with latest cricket headlines using News API.

- 🧠 **AI Summary (LangChain + Gemini)**  
  Generates a smart summary combining all inputs.

- ⚡ **Additional AI Tools**
  - 🔍 Web Search (DuckDuckGo)
  - 🧮 Calculator
  - 🌍 Language Translation (English → French)

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit  
- **Backend:** Python  
- **AI Framework:** LangChain  
- **LLM:** Google Gemini API  
- **APIs Used:**
  - Weather API  
  - News API  
  - yFinance  
- **Other Tools:**
  - DuckDuckGo Search (DDGS)
  - Deep Translator

---

## 📸 Demo

<img width="772" height="622" alt="Screenshot 2026-05-07 204308" src="https://github.com/user-attachments/assets/4ced8982-7f7f-4702-8d99-d70a83eda4fb" />
<img width="454" height="698" alt="Screenshot 2026-05-07 204355" src="https://github.com/user-attachments/assets/a71aa37f-bc01-42c3-a519-604d38b59ba2" />


---

## ⚙️ Installation & Setup

```bash
# Clone the repository
git clone https://github.com/TarandeepKaur10/AI-Daily-Briefing-Assistant.git

# Navigate to project folder
cd AI-Daily-Briefing-Assistant

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
