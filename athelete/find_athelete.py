from datetime import datetime

from sqlalchemy import Column, Integer, Text, Float
from sqlalchemy.ext.declarative import declarative_base
from connector.db_connector import DbConnector
from users.users import User

Base = declarative_base()

class Athelete(Base):
    __tablename__ = 'athelete'
    id = Column(Integer, primary_key=True, autoincrement=True)
    age = Column(Integer)
    birthdate = Column(Text)
    gender = Column(Text)
    height = Column(Float)
    name = Column(Text)
    weight = Column(Integer)
    gold_medals = Column(Integer)
    silver_medals = Column(Integer)
    bronze_medals = Column(Integer)
    total_medals = Column(Integer)
    sport = Column(Text)
    country = Column(Text)

def find_athelete():
    id_for_search = input('Введите идентификатор пользователя: ')
    connector = DbConnector()
    engine = connector.connect().engine
    session = connector.get_session()

    query_user = session.query(User).filter(User.id == id_for_search)
    if query_user:
        query_athelete = session.query(Athelete).filter(
            (datetime.strftime(Athelete.birthdate, '%Y-%m-%d')) - (datetime.strftime(query_user.first().birthdate), '%Y-%m-%d')).days <= 1)

