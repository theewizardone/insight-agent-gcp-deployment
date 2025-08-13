from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.post("/analyze")
def analyze(text_input: TextInput):
    text = text_input.text
    word_count = len(text.split())
    char_count = len(text)
    return {
        "original_text": text,
        "word_count": word_count,
        "character_count": char_count
    }