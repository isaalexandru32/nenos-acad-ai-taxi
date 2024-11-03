from pydantic import BaseModel

class Car(BaseModel):
    id: str
    current_location: str
    fuel: int
    availability: bool
    passenger_count: int

