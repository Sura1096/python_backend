from db.database import engine, Base
from db.models import book
from db.models import buy_book
from db.models import buy_step
from db.models import client


def main():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    main()
