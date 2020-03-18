from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker

class DbConnector():
    __db_connection_string = 'sqlite:///../sochi_athletes.sqlite3'
    __engine: None

    def __init__(self):
        pass

    def connect(self):
        self.engine = create_engine(self.__db_connection_string)
        return self

    def get_session(self):
        Sessions = sessionmaker(bind=self.engine)
        return Sessions()