import sqlalchemy
import sqlalchemy.ext.declarative as dec


SqlAlchemyBase = dec.declarative_base()
engine = sqlalchemy.create_engine("sqlite:///data.db", echo=False)


class Rating(SqlAlchemyBase):

    __tablename__ = 'happiness_report'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    country = sqlalchemy.Column(sqlalchemy.String(30))
    year = sqlalchemy.Column(sqlalchemy.String(4))
    rating = sqlalchemy.Column(sqlalchemy.Float)

    def __repr__(self):
        return f'{self.id} --- {self.country} --- {self.year}'


SqlAlchemyBase.metadata.create_all(engine)
