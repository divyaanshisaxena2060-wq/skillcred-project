AI Portfolio Generator

An AI-powered portfolio generator that turns your resume (PDF/TXT) into a professional, downloadable HTML portfolio using Google Gemini.

✨ Features

* 📄 Upload PDF or TXT resume
* 🤖 AI-powered resume information extraction using Gemini
* 🎨 5 standout portfolio themes
* 🌐 Generates a self-contained HTML portfolio
* 📥 Download your portfolio instantly
* 📱 Responsive portfolio designs

🎨 Available Themes

Choose from 5 unique styles:

* Modern — Clean and contemporary
* Minimal — Simple and elegant
* Creative — Bold and visually distinctive
* Professional — Polished and corporate
* Developer — Tech-focused portfolio design

🛠️ How It Works

Resume
   ↓
Text Extraction
   ↓
Google Gemini
   ↓
Structured Portfolio Data
   ↓
Theme Selection
   ↓
Generated HTML Portfolio

📁 Project Structure

.
├── app.py                 # Flask backend
├── extraction.py         # PDF/TXT text extraction
├── gemini_client.py      # Gemini API integration
├── template.py           # Portfolio templates
├── index.html             # Frontend
├── requirements.txt
└── .env                  # Local API configuration

⚙️ Setup

1. Install dependencies

pip install -r requirements.txt

2. Add your Gemini API key

Create a .env file:

GEMINI_API_KEY=your_gemini_api_key_here
PORT=5000
ALLOWED_ORIGINS=*

Get your API key from Google AI Studio.

⚠️ Never commit your .env file or expose your API key publicly.

3. Run the app

python app.py

Then open:

http://localhost:5000

⚠️ Limitations

* Supports PDF and TXT resumes only.
* Scanned/image-only PDFs may not work.
* Generated content should be reviewed before publishing.

🔧 Tech Stack

Python • Flask • Google Gemini API • HTML • CSS • JavaScript