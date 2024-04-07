from fastapi import FastAPI, HTTPException
import uvicorn
import crud
from models import Rating
from schemas import RatingSchema


api = FastAPI()

@api.get("/all_table", response_model=RatingSchema)
async def all_table():
    return crud.get_all_table()


@api.get("/avg", response_model=RatingSchema)
async def avg_life_satisfaction(country):
    return crud.get_avg_life_satisfaction(country=country)


@api.get("/country_info", response_model=RatingSchema)
async def all_countries(country, year):
    return crud.get_all_countries(country=country, year=year)


@api.post("/create_rating", response_model=RatingSchema)
async def create_rating(new: RatingSchema):
    return crud.create_rating(add_value=new)


if __name__ == "__main__":
    uvicorn.run('server:api', reload=True)


# @app.post("/users/", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     db_user = crud.get_user_by_email(db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return crud.create_user(db=db, user=user)


# @app.get("/users/", response_model=list[schemas.User])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = crud.get_users(db, skip=skip, limit=limit)
#     return users
