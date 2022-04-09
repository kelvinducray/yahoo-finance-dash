from dash import Dash, dcc, html

app = Dash(__name__)
app_server = app.server  # For running with uvicorn

app.layout = html.Div(
    children=[
        html.H1(
            children="Avocado Analytics",
        ),
        html.P(
            children="Analyze the behavior of avocado prices"
            " and the number of avocados sold in the US"
            " between 2015 and 2018",
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": [1, 2, 3],
                        "y": [1, 2, 3],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Average Price of Avocados"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": [1, 2, 3],
                        "y": [1, 2, 3],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Avocados Sold"},
            },
        ),
    ]
)
