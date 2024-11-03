from pylint import BaseModel

class Client(BaseModel):
    current_location: str
    desired_location: str
    customer_id: str
    passenger_count: int
    confirmation_message: str

