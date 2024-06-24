import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from flask import Flask, render_template


server = Flask(__name__)

app = dash.Dash(__name__, server=server, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])


navbar = dbc.NavbarSimple(
    dbc.DropdownMenu(
        [
            dbc.DropdownMenuItem(page["name"], href=page["path"])
            for page in dash.page_registry.values()
            if page["module"] != "pages.not_found_404"
        ],
        nav=True,
        label="More Pages",
        className="dropdown-menu-navbar",
    ),
    brand="Rare Earthlings",
    fluid=True,
    id='main-navbar'
)


app.layout = html.Div(children=[
    navbar,
    dash.page_container],) 

if __name__ == '__main__':
    app.run_server(debug=False)