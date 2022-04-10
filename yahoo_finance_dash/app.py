import dash_bootstrap_components as dbc
from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State

from .dashboards import dashx, dashy, dashz, index

app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.LUX],
)
app_server = app.server  # For running with gunicorn

dropdown = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem("Home", href="/index"),
        dbc.DropdownMenuItem("DashX", href="/dashx"),
        dbc.DropdownMenuItem("DashY", href="/dashy"),
        dbc.DropdownMenuItem("DashZ", href="/dashz"),
    ],
    nav=True,
    in_navbar=True,
    label="Explore",
)

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src="/assets/virus.png", height="30px")),
                        dbc.Col(dbc.NavbarBrand("COVID-19 DASH", className="ml-2")),
                    ],
                    align="center",
                    # no_gutters=True,
                ),
                href="/home",
            ),
            dbc.NavbarToggler(id="navbar-toggler2"),
            dbc.Collapse(
                dbc.Nav(
                    # right align dropdown menu with ml-auto className
                    [dropdown],
                    className="ml-auto",
                    navbar=True,
                ),
                id="navbar-collapse2",
                navbar=True,
            ),
        ]
    ),
    color="dark",
    dark=True,
    className="mb-4",
)


def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


for i in [2]:
    app.callback(
        Output(f"navbar-collapse{i}", "is_open"),
        [Input(f"navbar-toggler{i}", "n_clicks")],
        [State(f"navbar-collapse{i}", "is_open")],
    )(toggle_navbar_collapse)

# embedding the navigation bar
app.layout = html.Div([dcc.Location(id="url", refresh=False), navbar, html.Div(id="page-content")])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/dashx":
        return dashx.layout
    elif pathname == "/dashy":
        return dashy.layout
    elif pathname == "/dashz":
        return dashz.layout
    else:
        return index.layout
