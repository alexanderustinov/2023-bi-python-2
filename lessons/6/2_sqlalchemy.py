# https://docs.sqlalchemy.org/en/20/orm/quickstart.html

from sqlalchemy import create_engine
from sqlalchemy import String, select, or_
from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column

engine = create_engine("sqlite:///data.db", echo=False)

class Base(DeclarativeBase):
    pass

class Cat(Base):
    __tablename__='cats'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    age: Mapped[int] = mapped_column()

    def __repr__(self): 
        return f"Cat(id={self.id}, name={self.name}, age={self.age})"

Base.metadata.create_all(engine)

with Session(engine) as s:
    c = Cat(name='Vasya', age=2)
    c1 = Cat(name='Vasya', age=3)
    s.add(c)
    s.add(c1)
    s.commit()

with Session(engine) as s:
    results = select(Cat).where(or_(Cat.age==3, Cat.age==2))

    for result in s.scalars(results):
        print(result)

#
# неудачные попытки с пары
#

# 1
with Session(engine) as s:
    results = s.query(Cat.name, Cat.age==3, Cat.age==2)
    # Легаси из 1-й версии алхимии
    # > Note that the _query.Query object is legacy as of SQLAlchemy 2.0
    # 
    # Делает запрос и возвращает поля, не фильтрует данные (на паре возвращал булево
    # значение равен возраст определённому или нет)
    for result in results:
        print(result)

# 2        
with Session(engine) as s:
    results = select(Cat).where(or_(Cat.age==3, Cat.age==2))
    
    # boom
    # for result in s.query(results): # <- неосознанная попытка запихать результаты 
    #                                 #    в качестве запроса через легаси из п.1
    #     print(result)
