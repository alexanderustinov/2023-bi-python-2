from sqlalchemy.orm import Session
from sqlalchemy import select, and_
import uvicorn
from models import engine, GDPPC
from fastapi import FastAPI

api = FastAPI()


@api.get("/")
async def get_gdp_data(city, year):
    with Session(engine) as session:
        query = select(GDPPC).where(and_(GDPPC.city == city, GDPPC.year == year))
        results = session.execute(query).scalars().all()
        return results

if __name__ == "__main__":
     uvicorn.run('server:api', reload=True)
