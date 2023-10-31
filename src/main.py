from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel
import os
from dotenv import load_dotenv

#  take environment variables from .env
load_dotenv('config.env')
# collect environment variable
workspace = os.environ['WORKSPACE']

pipe = pipeline("translation", model=f"Helsinki-NLP/opus-mt-tc-big-en-{workspace}")

class Input(BaseModel):
    text: str

class Output(BaseModel):
    predictions: dict

app = FastAPI()

@app.get("/")
async def root():
    return {"message": f"Hi, you are collecting predictions from {workspace}."}

@app.post("/predict", response_model=Output)
async def predict(input: Input):
    response = pipe(input.text)
    prediction = response[0]['translation_text']
    output = Output(predictions={'text': prediction})
    return output
