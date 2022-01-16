from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.sql.expression import null
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

engine = create_engine('sqlite:///mydb.db')

Base.metadata.create_all(engine)

class Cars(Base):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True)
    make = Column(String(50),nullable=False)
    color = Column(String(50), nullable=False)

class CarOwners(Base):
    __tablename__ = 'carowners'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)
    car_id = Column(Integer, ForeignKey('cars.id'))
    car = relationship(Cars)

DBSession = sessionmaker(bind=engine)
session = DBSession()

car1 = Cars(make='Ford', color='silver')

session.add(car1)
session.commit()

owner1 = CarOwners(
  name="Joe",
  age="99",
  car_id=(car1.id)
)
session.add(owner1)
session.commit()

result = session.query(Cars).first()
print(result[0].color)