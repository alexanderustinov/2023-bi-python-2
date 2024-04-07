import uvicorn
from fastapi import FastAPI, HTTPException
from penguin import Penguin

api = FastAPI()
penguins = []

@api.get("/")
async def list_penguins():
    return penguins

@api.put("/add")
async def add_penguin(penguin: Penguin):
    penguins.append(penguin)
    return (f"New penguin species: {penguin.species}")

@api.get("/penguins/{penguin_species}")
async def get_height_by_penguin(penguin_species: str):
    for penguin in penguins:
        if penguin.species == penguin_species:
            return (f'{penguin.height}')
        raise HTTPException(status_code = 404, detail = "No penguin, unfortunately(")

if __name__ == '__main__':
    uvicorn.run('server:api', reload=True)