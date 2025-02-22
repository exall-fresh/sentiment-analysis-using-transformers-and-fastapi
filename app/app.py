from fastapi import UploadFile, File, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import pandas as pd
import io
from . import app, sentiment_pipeline  # Import app instance from __init__.py

# Initialize Jinja2 templates
templates = Jinja2Templates(directory="app/templates")

# Route to serve the frontend page
@app.get("/", response_class=HTMLResponse)
async def serve_ui(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/analyze-csv")
async def analyze_csv(request: Request, file: UploadFile = File(...)):
    # Read the uploaded file
    contents = await file.read()
    df = pd.read_csv(io.BytesIO(contents))
    
    # Check if the 'feedback' column exists
    if 'feedback' not in df.columns:
        return {"error": "CSV must contain a 'feedback' column"}
    
    # Analyze each feedback entry and store results
    results = []
    for feedback in df['feedback']:
        sentiment = sentiment_pipeline(feedback)[0]
        results.append({
            "feedback": feedback,
            "sentiment": sentiment['label']
        })
    
    # Store results in the session or pass them to the template
    return templates.TemplateResponse("results.html", {
        "request": request,
        "results": results
    })

@app.get("/download-csv")
async def download_csv():
    # Generate a CSV file from the results
    results = request.session.get("results", [])
    if not results:
        return {"error": "No results to download"}
    
    # Convert results to a DataFrame
    df = pd.DataFrame(results)
    
    # Convert DataFrame to CSV
    output = io.StringIO()
    df.to_csv(output, index=False)
    output.seek(0)
    
    # Return the CSV file as a downloadable response
    return Response(
        content=output.getvalue(),
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=analyzed_feedback.csv"}
    )