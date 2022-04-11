import pandas as pd
from dash import html

from ..component_builder import make_line_graph
from ..data_grabber import get_yf_data_grabber

yfdg = get_yf_data_grabber()

second_plot_data = yfdg.spark(["AAPL"])

layout = html.Div(
    children=[
        html.H1(
            children="Avocado Analytics",
        ),
        html.P(
            children="Analyze the behavior of avocado prices"
            " and the number of avocados sold in the US"
            " between 2015 and 2018",
        ),
        make_line_graph(
            "Test Graph",
            x=pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9]),
            y=pd.Series([9, 5, 9, 1, 2, 5, 3, 8, 1]),
        ),
        make_line_graph(
            f"Plot of {second_plot_data['asx_code'][0]}",
            x=second_plot_data["timestamp"],
            y=second_plot_data["close"],
        ),
    ]
)
