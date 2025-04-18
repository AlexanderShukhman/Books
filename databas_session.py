from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# импортируем классы Book и Base из файла database_setup.py
from database_setup import Book, Base

engine = create_engine('sqlite:///books-collection.db',echo=True)
# Свяжим engine с метаданными класса Base
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# Экземпляр DBSession() отвечает за все обращения к базе данных
# и представляет «промежуточную зону» для всех объектов,
# загруженных в объект сессии базы данных.
session = DBSession()

book1 = Book(author="Л.Н. Толстой", title="Война и мир")

data = {"author": "А.С. Пушкин", "title": "Евгений Онегин", "genre": "Роман в стихах"}

"""
session.add(book1)
session.add(Book(**data))

session.commit()
"""
all_books = session.query(Book).filter_by(author="Л.Н. Толстой").all()
for book in all_books:
    print(book)

editedBook = session.query(Book).filter_by(id=1).one()
editedBook.author = "Лев Толстой"
session.add(editedBook)
session.commit()

# session.query(Book).first() # вернет первый результат или None, если строки нет
