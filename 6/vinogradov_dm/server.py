import uvicorn
from fastapi import FastAPI, HTTPException
from classes import B

api = FastAPI()

cats = []

@api.get("/")
async def list_cats():
    return cats

@api.put("/add")
async def add_cat(cat: B):
    cats.append(cat)
    await f(cat.color)

@api.get("/f/")
async def f(color: str):
    global cats
    fil = [fruit for fruit in cats if fruit.color == color]
    cats.extend(fil)
    return fil

if __name__ == '__main__':
    uvicorn.run("server:api", reload=True)
