import dash_mantine_components as dmc

from src.web.components.base import DashAppBaseComponent


class AddClientComponent(DashAppBaseComponent):

    def __init__(self):
        pass

    def render(self):
        return dmc.Stack(
            children=[
                dmc.TextInput(
                    id="add-customer-id",
                    label="Customer ID:",
                    w=200
                ),
                dmc.TextInput(
                    id="add-customer-location",
                    label="Customer Location:",
                    w=200
                ),
                dmc.TextInput(
                    id="add-customer-desired-location",
                    label="Desired location:",
                    w=200
                ),
                dmc.TextInput(
                    id="add-passenger-count",
                    label="How many passengers?",
                    w=200
                ),
                dmc.Button(
                    id="add-client-button",
                    children="Add client",
                    w=200,
                ),
            ],
        )
