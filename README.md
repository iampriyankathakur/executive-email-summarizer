# 📧 Executive Email Summarizer & Action Extractor

This project processes **email threads** and produces:  
- ✅ A concise summary  
- ✅ A list of action items (with responsible parties, if possible)

Designed for **executives and busy teams**, it shows how AI can boost productivity in real-world business workflows.


## 🚀 Features
- Summarization of multi-email threads
- Action item extraction using regex + NLP
- JSON export of structured output
- Extensible to Gmail/Outlook API


## ⚙️ Installation
```bash
git clone https://github.com/yourusername/executive-email-summarizer.git
cd executive-email-summarizer
pip install -r requirements.txt
```

▶️ Usage
python src/pipeline.py --file data/sample_emails.json

Output:
{
  "summary": "Team discussed Q1 sales strategy. Budget increase approved.",
  "actions": [
    "John to prepare updated sales forecast",
    "Mary to send budget approval email"
  ]
}

📊 Tech Stack

Python

NLP: Hugging Face transformers (summarization), regex, spaCy

Export: JSON

Testing: pytest

📌 Roadmap

 Add speaker attribution (who said what)

 Integrate with Gmail API

 Build Streamlit chat-style UI

 ## ⚙️ Step 4: `requirements.txt`
```txt
transformers
torch
spacy
regex
pandas
pytest
```
