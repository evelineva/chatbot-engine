from fastapi import FastAPI
import requests

app = FastAPI()

RASA_URL = "http://localhost:5005/webhooks/rest/webhook"  # Sesuaikan dengan Rasa server-mu

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI with Rasa!"}

@app.post("/chat/")
def chat_with_rasa(user_message: dict):
    """
    Kirim pesan ke Rasa dan kembalikan responsnya.
    """
    response = requests.post(RASA_URL, json={"sender": "user", "message": user_message["message"]})
    return response.json()

