import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker
from models import create_tables
import os
from dotenv import load_dotenv

load_dotenv()
DSN = os.getenv('PASSWORD')
engine = sq.create_engine(DSN)
create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

session.close()

