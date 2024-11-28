from pydantic import BaseModel

class Client(BaseModel):
    customer_location: str
    desired_location: str
    customer_id: int
    passenger_count: int
    #confirmation_message: str

