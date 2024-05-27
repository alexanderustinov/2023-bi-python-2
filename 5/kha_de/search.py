from sqlalchemy import select
from sqlalchemy.orm import Session
from models import engine, Book

with Session(engine) as s:
    search_1 = select(Book).where(Book.percent <= 30)
    search_2 = select(Book).where(Book.country == 'Morocco')

    print("Countries where the percentage of students who could not read was less than 30:")
    for i in s.scalars(search_1):
        print(f"- {i.country} - {i.percent}%")

    print()

    for i in s.scalars(search_2):
        print(f"In Morocco percent of students who could not read was {i.percent}.")
