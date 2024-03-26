from sqlalchemy.orm import Session
from sqlalchemy import select, func
from models import engine, Rating


with Session(engine) as s:

    print('\n')
    # запрос группирует записи по странам и вычисляет среднее значение "Life satisfaction"
    # за все годы измерений для каждой страны в отдельности
    query_1 = s.execute(
        select(Rating.country, func.avg(Rating.rating))
        .group_by(Rating.country))
    print(query_1.all())
    print('\n')

    # запрос выдает все записи для России, которые относятся к 2007 году
    # никто никогда не вернет 2007 год :-(
    # https://www.youtube.com/watch?v=i9Nebj-dVn4
    query_2 = s.execute(
        select(Rating.year, Rating.rating)
        .where(Rating.country == "Russia")
        .order_by(Rating.rating.desc()))
    print(query_2.all())
    print('\n')

    # запрос выдает количество лет, которое в каждой стране проводились измерения
    # (сколько всего представлено измерений у каждой страны за весь период)
    query_3 = s.execute(
        select(Rating.country, func.count(Rating.rating))
        .group_by(Rating.country))
    print(query_3.all())
