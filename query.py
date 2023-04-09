from main import Session
from models import Publisher, Book, Shop, Stock, Sale

session = Session()
for v in session.query(Publisher):
    print(v)
    


session.close()