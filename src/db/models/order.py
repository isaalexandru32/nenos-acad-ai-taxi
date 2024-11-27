from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

from src.db.models import SQL_Base


class TaxiCar(SQL_Base):  
    __tablename__ = 'order'  

    orderId = Column(Integer, primary_key=True)  # id column (mandatory)
    status = Column(String(25), nullable=False)
    price = Column(Integer, nullable=False)
    clientId = Column(Integer, ForeignKey("taxi_client.id"), nullable=False)
    carId = Column(Integer, ForeignKey("taxi_car.id"), nullable=False)
