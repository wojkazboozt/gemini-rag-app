import google.generativeai as genai
from fastapi import FastAPI
import os

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

app = FastAPI()

@app.get("/generate/")
def generate_response(prompt: str):
    model = genai.GenerativeModel(model_name="models/gemini-2.0-flash")
    response = model.generate_content(prompt)
    return {"response": response.text}
