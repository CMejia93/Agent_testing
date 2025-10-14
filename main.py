from fastapi import FastAPI
from langchain_service import PromptOllamaSbS

app = FastAPI()

@app.post("/chatSbS")
async def root():
    return PromptOllamaSbS()

