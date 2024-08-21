from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..database import Base


class Genre(Base):
    __tablename__ = 'genre'

    genre_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name_genre: Mapped[str]
    books = relationship('Book', back_populates='genre')


class Author(Base):
    __tablename__ = 'author'

    author_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name_author: Mapped[str]
    books = relationship('Book', back_populates='author')


class Book(Base):
    __tablename__ = 'book'

    book_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str]
    author_id: Mapped[int] = mapped_column(ForeignKey('author.author_id'))
    genre_id: Mapped[int] = mapped_column(ForeignKey('genre.genre_id'))
    price: Mapped[float]
    amount: Mapped[int]

    genre = relationship('Genre', back_populates='books')
    author = relationship('Author', back_populates='books')

    buy_book_info = relationship('BuyBook', back_populates='book_info')
