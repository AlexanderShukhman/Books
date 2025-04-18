from sqlalchemy import *
from sqlalchemy.orm import declarative_base

# создание экземпляра declarative_base
Base = declarative_base()

# здесь нужно описать классы
class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    author = Column(String(250), nullable=False)
    genre = Column(String(250))

    def __str__(self):
        return f"{self.author} {self.title} {self.genre}"


# создает экземпляр create_engine в конце файла
engine = create_engine('sqlite:///books-collection.db',echo=True)

Base.metadata.create_all(engine)