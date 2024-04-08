from fastapi import FastAPI
from schemas import Stars
import uvicorn

api = FastAPI()
stars = []

@api.put('/add')
async def add_star(star: Stars):
    stars.append(star)

@api.get("/")
async def get_stars():
    return stars

@api.get("/stars/<name>")
async def get_star_by_name(star_name: str):
    for i in stars:
        if i.stars == star_name:
            return (f"{star_name}")

@api.get("/stars/<distance>")
async def get_star_distance(distance: float):
    for i in stars:
        if i.name == distance:
            dis = i.distance()
            return(f"{dis}")


if __name__ == '__main__':
    uvicorn.run('server:api', reload=True)

