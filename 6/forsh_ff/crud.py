from sqlalchemy.orm import Session
from sqlalchemy import func, select

from models import Rating
from schemas import RatingSchema


def get_all_table(db: Session):
    return db.query(Rating).all()

def get_avg_life_satisfaction(db: Session, country: str):
    return db.query(Rating).select(Rating.country, func.avg(Rating.rating)).where(Rating.country == country).group_by(Rating.country)


def get_country_info(db: Session, country: str, year: str):
    return db.query(Rating).select(country, year).where(Rating.country == country and Rating.year == year)


def create_rating(db: Session, add_value: RatingSchema):
    db_rating = Rating(country=add_value.country, year=add_value.year, rating=add_value.rating)
    db.add(db_rating)
    db.commit()
    db.refresh(db_rating)
    return db_rating
