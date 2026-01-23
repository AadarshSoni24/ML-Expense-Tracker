# Personal Finance Tracker

A personal finance tracker that uses **OCR and machine learning** to automate expense analysis and provide insights into spending behavior through a simple user interface.

## Features
- OCR-based extraction of transaction data from statements or receipts
- Machine learning–based **expense categorization**
- **Spending forecast** using historical expense data
- **Anomaly detection** to flag unusual transactions
- Simple UI for interacting with the system

## Tech Stack
- Python
- Machine Learning (scikit-learn)
- OCR (Tesseract or equivalent OCR library)
- Pandas, NumPy
- Tkinter (UI)

## How It Works
1. The user runs the UI application
2. OCR extracts raw transaction text from uploaded documents
3. Data is cleaned and structured
4. ML models categorize expenses, forecast spending, and detect anomalies
5. Results are shown in the UI

## How to Run
1. Clone or download the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
