import io
import pandas as pd
import uvicorn
from fastapi import FastAPI, File, HTTPException, UploadFile

from scripts.AI_agent import AIAgent
from scripts.data_cleaning import DataCleaning

app = FastAPI()
ai_agent = AIAgent()
rule_cleaner = DataCleaning()

@app.post("/clean_data")
async def clean_data(file: UploadFile = File(...)):
    if not file.filename or not file.filename.lower().endswith(".csv"):
        raise HTTPException(status_code=400, detail="Please upload a CSV file.")

    contents = await file.read()
    try:
        df = pd.read_csv(io.BytesIO(contents))
    except Exception as exc:
        raise HTTPException(status_code=400, detail=f"Invalid CSV file: {exc}") from exc

    df = rule_cleaner.clean_data(df)
    df = ai_agent.process_data(df)
    return {"rows": df.to_dict(orient="records")}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
