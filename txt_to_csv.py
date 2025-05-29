from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
import spacy
import pandas as pd
import io

app = FastAPI()
nlp = spacy.load("en_core_web_sm")

def extract_entities(text: str):
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]

@app.post("/extract-entities/")
async def extract_entities_from_txt(file: UploadFile = File(...)):
    if not file.filename.endswith('.txt'):
        raise HTTPException(status_code=400, detail="Only .txt files are supported.")
    
    content = await file.read()
    text = content.decode("utf-8")
    entities = extract_entities(text)

    if not entities:
        raise HTTPException(status_code=404, detail="No entities found.")

    # Convert to DataFrame
    df = pd.DataFrame(entities, columns=["Entity", "Label"])
    
    # Convert DataFrame to CSV in-memory
    output = io.StringIO()
    df.to_csv(output, index=False)
    output.seek(0)

    return StreamingResponse(
        output,
        media_type="text/csv",
        headers={"Content-Disposition": f"attachment; filename=entities.csv"}
    )
