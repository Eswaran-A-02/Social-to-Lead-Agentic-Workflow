#  AutoStream Conversational AI Agent

##  Overview
This project builds a conversational AI agent for a SaaS product (AutoStream) that:
- Answers product-related queries using RAG
- Detects user intent
- Identifies high-intent users
- Captures leads using a mock API

---

##  Features

### 1. Intent Detection
Classifies user input into:
- Greeting
- Product Inquiry
- High-Intent Lead

---

### 2. RAG (Knowledge-Based Answers)
Uses a local JSON file (`Pricing.json`) to answer:
- Pricing
- Features
- Policies

---

### 3. Lead Capture
When high intent is detected:
- Collects Name, Email, Platform
- Calls mock function to simulate API

---

## 🛠️ How to Run

```bash
python app.py
