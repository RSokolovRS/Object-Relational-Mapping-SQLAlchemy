import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker
from models import  Base
import os
from dotenv import load_dotenv # Библиотека для работы с переменным окружением.(.env)

load_dotenv()
user_name = os.getenv('user_name')		#Получаем имя юзера из окружения и сохраняем в переменную
PASSWORD= os.getenv('PASSWORD')		#Получаем пароль юзера из окружения и сохраняем в переменную
host = os.getenv('host')		#Получаем хост из окружения и сохраняем в переменную
port = os.getenv('port')		#Получаем порт из окружения и сохраняем в переменную
DATABASE = os.getenv('DATABASE')	

DATABASE_URL = f'postgresql://{user_name}:{PASSWORD}@{host}:{port}/{DATABASE}'
# DSN = os.getenv('DATABASE_URL')
engine = sq.create_engine(DATABASE_URL)  #echo=True

Session = sessionmaker(bind=engine)
session = Session()

def create_tables(engine):
    Base.metadata.create_all(engine)

def drop_tables(engine):
    Base.metadata.drop_all(engine)

session.close()

if __name__ == '__main__':
    create_tables(engine)
    # drop_tables(engine)


