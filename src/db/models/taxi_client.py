from sqlalchemy import Column, Integer, String, Boolean

from src.db.models import SQL_Base


class TaxiClient(SQL_Base):  
    __tablename__ = 'taxi_client'  
    
    customer_id = Column(Integer, primary_key=True)
    customer_location = Column(String(30), nullable=False)
    desired_location = Column(String(30), nullable=False)
    passenger_count = Column(Integer, nullable=True)
    confirmation_message = Column(String(15), nullable=False)
