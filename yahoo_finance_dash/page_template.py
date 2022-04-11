import dash_bootstrap_components as dbc
from dash import dcc, html

from .dashboards import dashboards_config


def get_layout() -> html.Div:
    # Create navigation dropdown menu from dashboard config
    dropdown = dbc.DropdownMenu(
        children=[
            dbc.DropdownMenuItem(dc.page_title, href=f"/{url_name}")
            for url_name, dc in dashboards_config.items()
        ],
        nav=True,
        in_navbar=True,
        label="Explore",
    )
    # Create banner to house title and navigation dropdown
    navbar = dbc.Navbar(
        dbc.Container(
            [
                html.A(
                    # Use row and col to control vertical alignment of logo
                    dbc.Row(
                        [
                            dbc.Col(html.Img(src="/assets/virus.png", height="30px")),
                            dbc.Col(dbc.NavbarBrand("COVID-19 DASH", className="ml-2")),
                        ],
                        align="center",
                        # no_gutters=True,
                    ),
                    href="/",
                ),
                dbc.NavbarToggler(id="navbar-toggler"),
                dbc.Collapse(
                    dbc.Nav(
                        # right align dropdown menu with ml-auto className
                        [dropdown],
                        className="ml-auto",
                        navbar=True,
                    ),
                    id="navbar-collapse",
                    navbar=True,
                ),
            ]
        ),
        color="dark",
        dark=True,
        className="mb-4",
    )

    # Apply the page template
    return html.Div(
        [
            dcc.Location(id="url", refresh=False),
            navbar,
            html.Div(id="page-content"),
        ],
    )
