from typing import Optional

import pandas as pd
from dash import dcc


def make_line_graph(
    title: str,
    x: Optional[pd.Series],
    y: Optional[pd.Series],
) -> dcc.Graph:
    if not x or not y:
        x = y = []
        title += " - DATA RETRIEVAL FAILED."
    graph = dcc.Graph(
        figure={
            "data": [
                {
                    "x": x,
                    "y": y,
                    "type": "lines",
                },
            ],
            "layout": {
                "title": title,
            },
        },
    )
    return graph
