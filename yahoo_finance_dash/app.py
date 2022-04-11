from typing import Optional

import dash_bootstrap_components as dbc
from dash import Dash, html
from dash.dependencies import Input, Output

from .dashboards import dashboards_config, index
from .page_template import get_layout

# Initialise application and apply theme
app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.LUX],
)
app_server = app.server  # For running with gunicorn

# Set the template for the page
app.layout = get_layout()

# Grab the page content after the navigation is changed
@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname"),
)
def display_page(pathname: Optional[str]) -> html.Div:
    """
    This is implemented in this way so that all the page configuration
    is specified in the 'dashboards' directory, and not in the code.

    Here we simply lookup the module name based on the url or just return
    the index page if no dashboard module has that name.
    """
    if pathname:
        page_name = pathname.replace("/", "")
        if page_name in dashboards_config:
            dc = dashboards_config[page_name]
            return dc.page_content

    return index.layout
