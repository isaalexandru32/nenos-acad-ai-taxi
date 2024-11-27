from src.db.connection import SQLSesssion
from src.db.models import TaxiClient




def add_client_into_the_db(customer_id: int, customer_location: str, desired_location: str, passenger_count: int, confirmation_message: str) -> None:
    """
    Add an animal into the database
    """
    with SQLSesssion() as session:
        taxiClient = TaxiClient(
            customer_id=customer_id,
            customer_location=customer_location,
            desired_location=desired_location,
            passenger_count=passenger_count,
            confirmation_message=confirmation_message
        )
        session.add(taxiClient)
        session.commit()
