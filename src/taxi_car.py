from pydantic import BaseModel

class Car(BaseModel):
    id: str
    current_location: str
    fuel: int
    availability: bool
    passenger_count: int

    def __init__(self, id, current_location, fuel, availability, passenger_count):
        self.id = id
        self.current_location = current_location
        self.fuel = fuel
        self.availability = availability
        self.passenger_count = passenger_count