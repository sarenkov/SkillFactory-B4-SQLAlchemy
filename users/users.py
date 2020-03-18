from sqlalchemy import Column, Integer, Text, Float
from sqlalchemy.ext.declarative import declarative_base
from connector.db_connector import DbConnector

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(Text)
    last_name = Column(Text)
    gender = Column(Text)
    email = Column(Text)
    birthdate = Column(Text)
    height = Column(Float)


def user_register():
    user = User()
    print('Для регистрации нужны ваши данные')
    user.first_name = input('Напишите свое имя: ')
    user.last_name = input('Теперь свою фамилию: ')
    user.gender = input('Вы мужчина или женщина? ')
    user.email = input('Так же нужнен ваш email: ')
    user.birthdate = input('Напишите свою дату рождения: ')
    user.height = input('Ну и рост уже: ')
    print('Данные были учтены. Начинаю регистрацию...')
    return user


if __name__ == '__main__':
    new_user = user_register()
    connector = DbConnector()
    engine = connector.connect().engine
    session = connector.get_session()
    try:
        session.add(new_user)
        session.commit()
        print('Ура! Вы успешно зарегистрировались!')
    except Exception as err:
        print('Что-то пошло не так и пользователь не был зарегистрирован')
        session.rollback()
        print(str(err))
