import uvicorn
from fastapi import FastAPI
from classes import name_and_element

api = FastAPI()

genshin = []


@api.get("/")
async def list_genshin():
    return genshin


@api.put("/add")
async def add_genshin(human: name_and_element):
    genshin.append(human)
    return (f"New here: {human.name}")


@api.get("/{character_name}")
async def character_by_name(character_name: str):
    for g in genshin:
        if g.name == character_name:
            return (f"{g.element}")

@api.get("/{character_name}/archon")
async def archon_by_name(character_name: str):
    for g in genshin:
        if g.name == character_name:
            arch = g.archon_name()
            return (f"{arch}")

if __name__ == '__main__':
    uvicorn.run('server:api', reload=True)

