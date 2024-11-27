from pydantic import BaseModel

class Order(BaseModel):
    orderId: int
    status: str
    price: int
    clientId: int
    carId: int
        