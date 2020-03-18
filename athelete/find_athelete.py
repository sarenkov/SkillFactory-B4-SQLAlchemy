from datetime import datetime

from sqlalchemy import Column, Integer, Text, Float, func, desc, asc
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
    session = connector.connect().get_session()

    user = session.query(User).filter(User.id == id_for_search).first()

    if user:
        athlete_with_an_earlier_birthday = session.query(Athelete) \
            .filter(Athelete.birthdate <= user.birthdate) \
            .order_by(desc(Athelete.birthdate)).first()
        later_birthday_athlete = session.query(Athelete) \
            .filter(Athelete.birthdate > user.birthdate) \
            .order_by(asc(Athelete.birthdate)).first()
        athlete_is_shorter = session.query(Athelete) \
            .filter(Athelete.height <= user.height) \
            .order_by(desc(Athelete.height)).first()
        taller_athlete = session.query(Athelete) \
            .filter(Athelete.height > user.height) \
            .order_by(asc(Athelete.height)).first()
    else:
        print('Такого пользователя нет')
        return

    date_diff1 = datetime.fromisoformat(user.birthdate) - datetime.fromisoformat(
        athlete_with_an_earlier_birthday.birthdate)
    date_diff2 = datetime.fromisoformat(later_birthday_athlete.birthdate) - datetime.fromisoformat(user.birthdate)
    height_diff1 = user.height - athlete_is_shorter.height
    height_diff2 = taller_athlete.height - user.height

    if date_diff1 == date_diff2 or date_diff1 < date_diff2:
        print(f'Ближайший по дате рождения атлет по имени {athlete_with_an_earlier_birthday.name} '
              f'родившийся {athlete_with_an_earlier_birthday.birthdate}')
    else:
        print(f'Ближайший по дате рождения атлет по имени {later_birthday_athlete.name} '
              f'родившийся {later_birthday_athlete.birthdate}')

    if height_diff1 == height_diff2 or height_diff1 < height_diff2:
        print(f'Ближайший по росту атлет по имени {athlete_is_shorter.name} '
              f'ростом {athlete_is_shorter.height}')
    else:
        print(f'Ближайший по росту атлет по имени {taller_athlete.name} '
              f'ростом {taller_athlete.height}')


if __name__ == '__main__':
    find_athelete()
