from fastapi import FastAPI
from schemas import StarsTest
import uvicorn

api = FastAPI()
stars = []


@api.put('/add')
async def add_star(star: StarsTest):
    stars.append(star)


@api.get("/")
async def get_stars():
    return stars


@api.get("/stars/{star_name}")
async def get_star_by_name(star_name: str):
    for i in stars:
        if i.name == star_name:
            return f"{i.name}"


@api.get("/stars/{star_name}/dis")
async def get_star_distance(star_name: str):
    for i in stars:
        if i.name == star_name:
            return f"{i.distance}"


if __name__ == '__main__':
    uvicorn.run('server:api', reload=True)
