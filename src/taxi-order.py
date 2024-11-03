from pydantic import BaseModel
from src.taxi_car import Car
from src.taxi_client import Client


class Order(BaseModel):
    status: str
    price: int
    client: Client
    car: Car
        