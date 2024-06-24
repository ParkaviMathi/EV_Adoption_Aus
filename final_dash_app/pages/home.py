import dash
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/")

from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px

home_page_txt_file = 'assets/home_page_goal.txt'


with open(home_page_txt_file, 'r') as f:
    home_txt = f.readline()

pages_available = []
for page in dash.page_registry.values():
    pages_available.append(page['path'])

layout = html.Div(id="homepage-main-div", className="overlay", children=[
    html.Video(
        id="background-video",
        width="800",
        height="600",
        autoPlay=True,
        loop=True,
        muted=True,
        controls=False,
        children=[
            html.Source(src="/assets/clips/background_footage.mp4", type="video/mp4")
        ],
    ),
    html.Div('EVs in Australia', className="home-page-title"),
    html.Div(className='home-page-content', children=[
        html.Div(home_txt, className='home-page-text'),

        html.A('Begin The Journey →', className="button-74 home-journey-button", href=pages_available[1])
    ]),
    
   
    
 
# <button class="button-74" role="button">Button 74</button>
   
    
])


#@callback(Output("heatmaps-graph", "figure"), Input("heatmaps-medals", "value"))

