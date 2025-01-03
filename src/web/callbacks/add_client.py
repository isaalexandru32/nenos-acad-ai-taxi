import requests
from dash import Dash

from dash import callback_context
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output

from src.config import API_URL
from src.common.data_transfer_objects.taxi_client import Client



def register_add_client_callbacks(app: Dash) -> None:
    """
    Register add client callbacks
    """
    @app.callback(
        Output('webapp-content', "children"),
        [
            Input("add-client-button", "n_clicks"),
            Input("add-customer-id", "value"),
            Input("add-customer-location", "value"),
            Input("add-customer-desired-location", "value"),
            Input("add-passenger-count", "value"),
        ]
    )
    def send_client_info_to_api(_: int, client_id: int, client_location: str, cldesired_location: str, clpassenger_count: int):
        trigger = callback_context.triggered[0]
        if trigger["prop_id"].split('.')[0] == "add-client-button":
            dto = Client(
                customer_id=client_id,
                customer_location=client_location,
                desired_location=cldesired_location,
                passenger_count=clpassenger_count
            )
            response = requests.put(f"{API_URL}/taxi_client", timeout=5, data=dto.json())
            return response.status_code

        raise PreventUpdate
