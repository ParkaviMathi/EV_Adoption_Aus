import dash
from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
import numpy as np
from plotly.subplots import make_subplots
import matplotlib.cm as cm
import matplotlib.colors as mcolors
import dash_daq as daq # This is for cool toggle switch!
from txt_to_html import convert_txt_to_html


pg_title='EV Specs'
dash.register_page(__name__, name=pg_title)


## ------ Graph 3_1 ------- ##
in_file_path_3_1 = "cleaned_data/electric_vehicle_ranges_ev_database.csv"
df_3_1 = pd.read_csv(in_file_path_3_1)
df_3_1 = df_3_1.drop_duplicates(subset='Vehicle') # Remove duplicate entries (there are two)

df_3_1 = df_3_1.sort_values(by='Range (km)', ascending=True) 

fig_3_1 = px.bar(
    df_3_1,
    y='Vehicle',
    x='Range (km)',
    orientation='h'
)


## ------ Graph 3_2 ------- ##
in_file_path_3_2 = "cleaned_data/electric_vehicle_energy_consumption_ev_database.csv"
df_3_2 = pd.read_csv(in_file_path_3_2)
df_3_2 = df_3_2.drop_duplicates(subset='Vehicle') # Remove duplicate entries (there are two)


df_3_2 = df_3_2.sort_values(by='Consumption (Wh/km)', ascending=False) # Lowest consumption first 

fig_3_2 = px.bar(
    df_3_2,
    y='Vehicle',
    x='Consumption (Wh/km)',
    orientation='h'
)

# ===============================

# String defined for testing purpose -> content to be filled in later
very_long_string = "Lorem ipsum dolor sit amet, \
    consectetur adipisicing elit, sed do eiusmod \
        tempor incididunt ut labore et dolore magna \
            aliqua. Ut enim ad minim veniam, quis \
                nostrud exercitation ullamco laboris \
                    nisi ut aliquip ex ea commodo consequat."

analysis_path = 'plot_analysis_txts'

page_content = html.Div(className='graph-page-type', children=[
    
    # Page title:
    html.Div(pg_title, className='page-title'),

    # Title
    html.Div(id='anchor-loc-1'), # Specify location with this
    html.Div("Electric Vehicle Ranges (in KM)", className='graph-title'),

    # Graph 3 - 1
    html.Div([
        dcc.Graph(figure=fig_3_1, style={"height": "10000px", "width":"100%"}),
    ], className='graph-container-1', style={'overflow-y':'auto', 'height':'600px'}),
    
    # Collapsible content:
    html.Details([
        html.Summary('Analysis'),
        html.Div(
            className="collapsible-content",
            children=convert_txt_to_html(f'{analysis_path}/EV Car Range.txt'))
    ]),

    # Title
    html.Div(id='anchor-loc-2'), # Specify location with this
    html.Div("Electric Vehicle Battery Consumption Per KM", className='graph-title'),

    # Graph 3 - 2
    html.Div([
        dcc.Graph(figure=fig_3_2, style={"height": "10000px", "width":"100%"}),
    ], className='graph-container-1', style={'overflow-y':'auto', 'height':'600px'}),

    # Collapsible content:
    html.Details([
        html.Summary('Analysis'),
        html.Div(
            className="collapsible-content",
            children=convert_txt_to_html(f'{analysis_path}/EV Energy Consumption.txt'))
    ]),
    

])

sidebar = html.Div(className='sidebar', children=[
    "Sidebar Menu",
    html.A(href='#anchor-loc-1', children=[
        html.Div('EV Range', className='sidebar-selection-box'),
    ]),
    html.A(href='#anchor-loc-2', children=[
        html.Div('EV Battery Consumption', className='sidebar-selection-box'),
    ]),
])


layout = html.Div(className='content-page',children=[sidebar, page_content])




