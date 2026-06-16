from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class LoginRequest(BaseModel):
    email: str
    password: str

@app.get("/")
def home():
    return {
        "message": "CI/CD Working Successfully"
    }

@app.post("/login")
def login(user: LoginRequest):
    return {
        "email": user.email,
        "password": user.password
    }