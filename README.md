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
```Python 3.8+```
**Project Installation**

**1. Clone the repository**

```git clone https://github.com/exall-fresh/sentiment-analysis-using-transformers-and-fastapi.git```

then get into the project using the command: 

```cd sentiment-analysis-using-transformers-and-fastapi```

**2. Set up the environment**

```cd app```

```pip install -r requirements.txt```

**3. Running the Application**

Navigate to the root directory


```cd ../```

then to launch the project run the following command

```uvicorn app.app:app --reload```

And then ccess the application at:

```http://127.0.0.1:8000```


**4. API Endpoints**

To access all API Endpoints go to the address:

```http://127.0.0.1:8000/docs```

**5. 💻 HOW TO USE IT**

** Case 1: Just want to analyze a piece of text**

Navigate to the web interface ```http:127.0.0.1:8000/**
Enter your text in the input field
Click the  "Analyze" button to receive instant sentiment analysis

** Case 2: Batch Process a series of text from a csv file**

Prepare a CSV file with a 'feedback' column
Upload through the web interface
Process multiple entries simultaneously
Download the complete analysis report


**6. Final Preview**

After successfully following through the steps you will have an interface like this and good luck with sentiment analysis


![Screenshot (8)](https://github.com/user-attachments/assets/8831c1e9-4832-41f2-b7d2-0ae4fb2854c2)

**Contact me for a further chat on AI and Data Science on**

Linkedin: ```https://www.linkedin.com/in/patrick-nyasulu-335935237/```

