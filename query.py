from main import Session
from models import Publisher, Book, Shop, Stock, Sale

session = Session()
# for v in session.query(Publisher):
#     print(v)
    
# with Session() as session:
subq = session.query(Publisher).filter(Publisher.name.like("%Microsoft Press%")).subquery()
# print(subq)
subq = session.query(Book).join(subq, Book.id_publisher == subq.c.id).subquery()
q1 = session.query(Book.title, Stock.count).join(subq, Stock.id_book == subq.c.id)
print(q1)
for v in q1.all():
    print( v)

# for i in session.query(Publisher).join(Book.publisher).all():
#     print(i)
# q = session.query(Publisher).filter(Publisher.name == input("Введите название издателя "))
# for s in q.all():
#     print(s.id, s.name)


# q = session.query(Publisher).filter(Publisher.id == input("Введите идентификатор (id) издателя "))
# for s in q.all():
#     print(s.id, s.name)
# session.query(Publisher).filter(Book.EmployeeName.like("%{0}%".format(request.args.get('Name'))

# with Session() as session:
# 	stmt = session.query(Publisher.user_id, sqlalchemy.func.count('id').label('users_found')).subquery()
	
# 	main_query = session.query(User, stmt.c.users_found).outerjoin(stmt, User.id==stmt.c.user_id).order_by(User.id)
# 	records = main_query.all()
# 	for user, orders in records:
		# execute all you need


session.close()