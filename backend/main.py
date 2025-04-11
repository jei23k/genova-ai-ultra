
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Input(BaseModel):
    texto: str

@app.post("/generar")
def generar_video(input: Input):
    return {"mensaje": f"Video generado para: {input.texto}"}
