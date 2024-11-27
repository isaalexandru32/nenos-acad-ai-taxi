from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

from src.db.models import SQL_Base


class TaxiCar(SQL_Base):  
    __tablename__ = 'taxi_car'  

    id = Column(Integer, primary_key=True)  # id column (mandatory)
    current_location = Column(String(30), nullable=False)
    fuel = Column(Integer, nullable=True)
    availability = Column(Boolean, nullable=True)
    passenger_count = Column(Integer, nullable=True)
