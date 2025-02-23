🎯 **Sentiment Analysis Web Application**

A production-ready sentiment analysis web application powered by FastAPI and Hugging Face Transformers. This application provides real-time sentiment analysis through an intuitive web interface, supporting both direct text input and batch processing via CSV files.
✨ Features
- Dual Input Methods
- Interactive text analysis in real-time
- Batch processing through CSV file upload

Advanced NLP Processing

- Sentiment analysis using state-of-the-art transformer models
- Fast and accurate classification of text sentiment

User-Friendly Interface

- Clean, responsive web interface
- Real-time results visualization

Data Export Capabilities

- Download analysis results in CSV format
- Structured output for further analysis

🚀 Quick Start
Prerequisites
bashCopyPython 3.8+
Git
Installation

Clone the repository

bashCopygit clone https://github.com/exall-fresh/sentiment-analysis-using-transformers-and-fastapi.git
cd sentiment-analysis-using-transformers-and-fastapi

Set up the environment

bashCopycd app
pip install -r requirements.txt
Core Dependencies
pythonCopyfastapi>=0.68.0
uvicorn>=0.15.0
pandas>=1.3.0
transformers>=4.11.0
jinja2>=3.0.1
Running the Application

Navigate to the root directory

bashCopycd ../

Launch the application

bashCopyuvicorn app.app:app --reload

Access the application at:

Copyhttp://127.0.0.1:8000
🔌 API Endpoints
EndpointMethodDescription/GETMain web interface/analyze-csvPOSTProcess CSV files for sentiment analysis/download-csvGETExport analysis results
For interactive API documentation, visit:
Copyhttp://127.0.0.1:8000/docs
💻 Usage Guide
Text Analysis

Navigate to the web interface
Enter your text in the input field
Click "Analyze" to receive instant sentiment analysis

Batch Processing

Prepare a CSV file with a 'feedback' column
Upload through the web interface
Process multiple entries simultaneously
Download the complete analysis report

📸 Interface Preview
Show Image
🛠️ Technical Architecture
mermaidCopygraph LR
    A[Web UI] --> B[FastAPI Backend]
    B --> C[Transformer Model]
    C --> D[Sentiment Analysis]
    D --> E[Results Processing]
    E --> F[CSV Export]
📜 License
This project is licensed under the MIT License - see the LICENSE file for details.
👨‍💻 Author
Patrick Exall Nyasulu

Data Scientist and Machine Learning Engineer
