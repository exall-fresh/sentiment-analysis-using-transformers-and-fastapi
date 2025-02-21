from fastapi import UploadFile, File, Form
from fastapi.responses import HTMLResponse  # ✅ Import HTMLResponse
from fastapi.templating import Jinja2Templates  # ✅ Import Jinja2Templates
import pandas as pd
import io
from . import app, sentiment_pipeline  # Import app instance from __init__.py


# Route to serve the frontend page
@app.get("/", response_class=HTMLResponse)
async def serve_ui():
    with open("templates/index.html", "r") as file:
        return file.read()
@app.post("/analyze-text")
async def analyze_text(text: str = Form(...)):
    result = sentiment_pipeline(text)
    return {"sentiment": result[0]['label'], "confidence": result[0]['score']}

@app.post("/analyze-csv")
async def analyze_csv(file: UploadFile = File(...)):
    contents = await file.read()
    df = pd.read_csv(io.BytesIO(contents))

    if 'feedback' not in df.columns:
        return {"error": "CSV must contain a 'feedback' column"}

    df['sentiment'] = df['feedback'].apply(lambda text: sentiment_pipeline(text)[0]['label'])

    output = io.BytesIO()
    df.to_csv(output, index=False)
    output.seek(0)

    return {"filename": "analyzed_feedback.csv", "file": output.getvalue().decode('utf-8')}
