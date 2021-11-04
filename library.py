from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

engine = create_engine('sqlite:///library.db')
Base = declarative_base()


class Book(Base):
    __tablename__ = "book"
    id = Column(Integer, primary_key=True)
    title = Column("Title", String)
    author = Column("Author", String)
    year = Column("Year", Integer)
    book_instances = relationship("BookInstance")

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return f'ID: {self.id}, "{self.title}", autorius - {self.author}, išleidimo metai: {self.year}'


class BookInstance(Base):
    __tablename__ = "book_instance"
    id = Column(Integer, primary_key=True)
    acquisition_date = Column("Date of acquisition", DateTime, default=datetime.now())
    on_loan = Column("On loan", Boolean, default=False)
    book_id = Column(Integer, ForeignKey("book.id"))
    book = relationship("Book", overlaps="book_instances")

    def __init__(self, book_id):
        self.book_id = book_id

    def __repr__(self):
        return f'ID: {self.id}, įsigijimo data: {self.acquisition_date}", ar knyga paskolinta - {self.author}, ' \
               f'knygos id: {self.book_id}'


Base.metadata.create_all(engine)
