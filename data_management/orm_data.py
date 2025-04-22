from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker


Base = declarative_base()


class UserData(Base):

    __tablename__ = "user_data"

    username = Column(String, primary_key=True, autoincrement=False)
    yearly_income = Column(Float)
    account_type = Column(String)
    monthly_spending = Column(Float)


engine = create_engine('sqlite:///user_account_data.db')

Session = sessionmaker(bind=engine)
session = Session()
