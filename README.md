# ✈️ AI Travel Planner

An intelligent AI-based travel planning system that generates personalized trip itineraries based on user preferences, budget, and interests.

---

## 🚀 Features

* 🤖 AI-based trip planning using LLM
* 💰 Smart budget-aware recommendations
* 📍 Location-based suggestions
* 🗺️ Day-wise itinerary generation
* 🔐 Secure API key handling using `.env`

---

## 🛠️ Tech Stack

* Python 🐍
* Streamlit 🌐
* Groq / OpenAI API 🤖
* Pandas 📊

---

## 📂 Project Structure

```
AI_Travel_Planner/
│
├── app.py              # Main Streamlit app
├── planner.py          # Trip planning logic
├── utils.py            # Helper functions
├── requirements.txt    # Dependencies
├── .env                # API keys (not uploaded)
├── .gitignore          # Ignore sensitive files
└── README.md           # Project documentation
```

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/shruti29075/AI_Travel_Planner.git
cd AI_Travel_Planner
```

---

### 2️⃣ Create virtual environment

```bash
python -m venv env
env\Scripts\activate.bat
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Setup environment variables

Create a `.env` file and add:

```
GROQ_API_KEY=your_api_key_here
```

---

### 5️⃣ Run the application

```bash
streamlit run app.py
```

---

## 📸 Output

* Generates smart travel plans
* Provides optimized itinerary
* Interactive UI using Streamlit

---


## ⭐ Future Improvements

* Real-time weather integration
* Hotel & flight booking APIs
* Map visualization
* User authentication system

---
