import dash
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/")

from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px


layout = html.Div(
    html.H4('HomePage:'),
    
)


#@callback(Output("heatmaps-graph", "figure"), Input("heatmaps-medals", "value"))

