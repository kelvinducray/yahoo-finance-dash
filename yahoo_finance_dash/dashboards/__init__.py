from dataclasses import dataclass

from dash import html

# Import the templates here:
from . import dashx, dashy, dashz, index


@dataclass
class DashboardData:
    page_title: str
    page_content: html.Div


# And then specify their config here:
dashboards_config = {
    # NOTE: We must have an index.py!
    "index": DashboardData(
        page_title="Index Page!!!",
        page_content=index.layout,
    ),
    "dashx": DashboardData(
        page_title="DashX!",
        page_content=dashx.layout,
    ),
    "dashy": DashboardData(
        page_title="DashY!",
        page_content=dashy.layout,
    ),
    "dashz": DashboardData(
        page_title="DashZ!",
        page_content=dashz.layout,
    ),
}
