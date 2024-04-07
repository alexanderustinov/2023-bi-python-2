from pydantic import BaseModel


class RatingSchema(BaseModel):

    id: int
    country: str
    year: str
    rating: float
