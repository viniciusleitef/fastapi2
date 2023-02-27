from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random
from typing import List, Optional
from pydantic import BaseModel
from uuid import uuid4

app = FastAPI()

origins =['http://127.0.0.1:5501']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Animais(BaseModel):
    id: Optional[str]
    nome: str
    sexo: str
    idade: int
    cor: str

banco: List[Animais] = []

@app.get("/")
async def root():
    return banco


@app.get("/")
def listar_animais():
    return banco

@app.post("/animais")
def postar_animais(animal:Animais):
    animal.id = random.randint(1000,100000)
    banco.append(animal)
    return animal

@app.get("/animais")
def mostrar_animais():
    return banco

@app.get("/animais/{id_animal}")
def pegar_id(id_animal:str):
    for animal in banco:
        if str(animal.id) == str(id_animal):
            return animal
    return {"messahe":"Animal não encontrado"}
    
@app.delete("/animais/{id_animal}")
def deletar_animal(id_animal:str):
    for index, animal in enumerate(banco):
        posiçao = -1
        if str(animal.id) == str(id_animal):
            posiçao = index
            break
    if posiçao != -1:
        banco.pop(posiçao)
        return {"Animal removido"}
    else:
        return ("Animal não encontrado")
