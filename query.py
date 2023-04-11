from main import Session
from models import Publisher, Book, Shop, Stock, Sale

session = Session()

def search(name:None):
    try:
        q = session.query(Publisher.name,Book.title,Stock.count,Shop.\
            name,Sale.price,Sale.date_sale).\
            filter(Book.publisher,Stock.book,Stock.shop,Sale.shop).\
            filter(Publisher.name.like(name))
        for i in q.all():
            print(i)
    except:
        print('Таких данных нет!')
    finally:
        session.close()

if __name__ == "__main__": # Точка входа.
    search(input('Enter the data:'))