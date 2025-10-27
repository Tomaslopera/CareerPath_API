from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification

# --- CREACIÓN ENTORNO ---
MODEL_NAME = "fazni/distilbert-base-uncased-career-path-prediction"

app = FastAPI(title="Career Path Prediction API")

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
clf = pipeline("text-classification", model=model, tokenizer=tokenizer, return_all_scores=True)

# --- MODELOS DE REQUEST Y RESPONSE ---
class PredictRequest(BaseModel):
    text: str

class Prediction(BaseModel):
    label: str

class PredictResponse(BaseModel):
    top_3: list[Prediction]


# --- ENDPOINT PRINCIPAL ---
@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    if not req.text or req.text.strip() == "":
        raise HTTPException(status_code=400, detail="Text must not be empty.")
    
    print(req.text)
    
    try:
        results = clf(req.text)
        label_scores = sorted(results[0], key=lambda x: x["score"], reverse=True)[:3]

        top3 = [Prediction(label=item["label"]) for item in label_scores]
        return PredictResponse(top_3=top3)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Inference error: {e}")