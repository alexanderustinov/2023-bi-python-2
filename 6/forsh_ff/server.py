from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import uvicorn
import crud
from models import SqlAlchemyBase, engine, SessionLocal


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/all_table")
async def all_table(db: Session = Depends(get_db)):
    return crud.get_all_table(db)


@app.get("/country_info/{country}/{year}")
async def all_countries(country: str, year: str, db: Session = Depends(get_db)):
    return crud.get_country_info(db, country=country, year=year)


if __name__ == "__main__":
    uvicorn.run('server:app', reload=True)
