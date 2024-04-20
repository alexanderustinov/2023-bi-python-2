from sqlalchemy.orm import Session
from sqlalchemy import select
import uvicorn
from models import engine, Population
from fastapi import FastAPI


api = FastAPI()


@api.get("/")
async def get_population(entity):
    with Session(engine) as s:
        res = select(Population).where(Population.entity == entity)
        results = s.execute(res).scalars().all()
        if results:
            return {"entity": results[0].entity, "population": results[0].people}
        return {"message": "Country not found"}

if __name__ == "__main__":
     uvicorn.run('server:api', reload=True)
