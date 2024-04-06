from sqlalchemy.orm import Session
from sqlalchemy import select, and_
import uvicorn
from models import engine, GDPPC
from fastapi import FastAPI
api = FastAPI()
@api.get('/')
async def get_gdp_data(entity):
    with Session(engine) as session:
        query = select(GDPPC).where((GDPPC.entity == entity))
        results = session.execute(query).scalars().all()
    return results

if __name__ == '__main__':
     uvicorn.run('server:api', reload=True)
