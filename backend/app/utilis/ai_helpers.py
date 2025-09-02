# app/utils/ai_helpers.py
import requests
import os

def summarize_feedback(text):
    url = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
    headers = {"Authorization": f"Bearer " + os.getenv("HUGGINGFACE_API_KEY")}
    response = requests.post(url, headers=headers, json={"inputs": text})
    return response.json()
