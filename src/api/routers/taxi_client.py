from fastapi import APIRouter, Response

from src.common.data_transfer_objects.taxi_client import Client
from src.db.queries.taxi_client import add_client_into_the_db

router = APIRouter()

# GET -> fetch data
# PUT -> add data
# POST -> functions
# DELETE -> delete add

@router.put("")
def add_client(dto: Client) -> Response:
    """
    Adds an animal to the database
    """

    add_client_into_the_db(
        customer_id=dto.customer_id,
        customer_location=dto.customer_location,
        desired_location=dto.desired_location,
        passenger_count=dto.passenger_count,
        #confirmation_message=dto.confirmation_message
    )
