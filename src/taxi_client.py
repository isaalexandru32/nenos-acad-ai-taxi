from pylint import BaseModel

class Client(BaseModel):
    current_location: str
    desired_location: str
    customer_id: str
    passenger_count: int
    confirmation_message: str


    def __init__(self, current_locatiion, desired_location, customer_id, passenger_count, confirmation_message) -> None:
        self.current_location = current_locatiion
        self.desired_location = desired_location
        self.customer_id = customer_id
        self.passenger_count = passenger_count
        self.confirmation_message = confirmation_message