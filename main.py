import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker
from models import  Base
import os
from dotenv import load_dotenv # Библиотека для работы с переменным окружением.(.env)

load_dotenv()
DSN = os.getenv('PASSWORD')
engine = sq.create_engine(DSN)  #echo=True

Session = sessionmaker(bind=engine)
session = Session()

def create_tables(engine):
    Base.metadata.create_all(engine)

def drop_tables(engine):
    Base.metadata.drop_all(engine)

session.close()

if __name__ == '__main__':
    create_tables(engine)



