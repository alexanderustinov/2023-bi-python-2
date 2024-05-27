from sqlalchemy.orm import Session

from models import Rating


def get_all_table(db: Session):
    return db.query(Rating).all()


def get_country_info(db: Session, country: str, year: str):
    return db.query(Rating).filter(Rating.country == country, Rating.year == year).all()
