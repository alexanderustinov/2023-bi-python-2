import uvicorn

from fastapi import FastAPI

from schemas import Cat
# "models" for ORM

api = FastAPI()

cats = []

@api.get("/")
async def list_cats():
    return cats

@api.put("/add")
async def add_cat(cat: Cat):
    cats.append(cat)

if __name__ == '__main__':
    uvicorn.run('server:api', reload=True)
    # API
