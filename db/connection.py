import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv

load_dotenv()

class DBConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = "{}://{}:{}@{}:{}/{}".format(
            "postgresql+psycopg2", os.getenv("USER"), os.getenv("PASS"), os.getenv("HOST"), os.getenv("PORT"), os.getenv("DB_NAME")
        )

        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        session_maker = sessionmaker(bind=self.__engine)
        self.session = session_maker()

        return self

    def __exit__(self, exec_type, exec_val, exec_tb):
        self.session.close()