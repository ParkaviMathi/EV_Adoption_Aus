import dash
from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from txt_to_html import convert_txt_to_html

pg_title = 'Charging Information'
dash.register_page(__name__, name=pg_title)



 # *** Graph 2 *** ------------------------------------------------------------------------
in_path = "cleaned_data/ev_charge_stations_australia.csv"
df_2 = pd.read_csv(in_path)

# Plotly Express
fig_2 = px.scatter_mapbox(df_2,
    lon = "Longitude",
    lat = "Latitude",
    color_discrete_sequence=["#FF0000"], # Bright red colour for the ev charge stations
    size=None,
    opacity=0.7,
    zoom = 3,
    title = 'Australian EV charging Stations',)


fig_2.update_layout(mapbox_style="open-street-map")
fig_2.update_layout(margin={"r":0, "t":50, "l":0, "b":10}) # Set margin of plot (right, top, left, bottom)
fig_2.update_layout(mapbox=dict(
        center=go.layout.mapbox.Center(
            lat=-27.2744,
            lon=133.7751),
            zoom=2.8 ) )

## ------ GRAPH 14 ------ ##
df_14 = pd.read_csv("cleaned_data/cleaned_automotive_fuel_and_CPI_Index(clean).csv")

fig_14 = px.line(
    df_14,
    x='Year',
    y='Value',
    color='Index Type',
    title='Automotive Fuel and CPI Index Number, 1972 = 100.0'
)

# Update layout for better readability
fig_14.update_layout(
    xaxis_title='Year',
    yaxis_title='Value',
    xaxis=dict(tickangle=45),  # Rotate x-axis labels for better readability
    legend_title='Index Type',
    # width=1000,  # Width of the plot
    # height=600,   # Height of the plot
    legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.01
    )
)

## --------- Graph on EV cost per 100km -----------

in_file_ev_100km = "cleaned_data/ev_cost_per_100_km.csv"
df_ev_100km = pd.read_csv(in_file_ev_100km)
df_ev_100km = df_ev_100km.sort_values(by='Cost per 100 km', ascending=False)

fig_ev_100km = px.bar(
    df_ev_100km,
    y='Vehicle',
    x='Cost per 100 km',
    orientation='h'
)

## --------- Graph on Gasoline cost per 100km -----------

in_file_gas_100km = "cleaned_data/gasoline_vehicle_cost_per_100_km.csv" 
df_gas_100km = pd.read_csv(in_file_gas_100km)
df_gas_100km = df_gas_100km.sort_values(by='Cost per 100 km', ascending=False)

fig_gas_100km = px.bar(
    df_gas_100km,
    y='Vehicle',
    x='Cost per 100 km',
    orientation='h'
)


# ====================


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
    html.Div("EV Charge Station Locations in Australia", className='graph-title'),

    # Graph 2
    html.Div([
        dcc.Graph(className='graph-container-1 graph-grow', figure=fig_2),
    ]),

    # Collapsible content:
    html.Details([
        html.Summary('Analysis'),
        html.Div(
            className="collapsible-content",
            children=convert_txt_to_html(f'{analysis_path}/Australian EV Charging Stations.txt'))
    ]),

    # Title
    html.Div(id='anchor-loc-3'), # Specify location with this
    html.Div("EV Cost per 100KM", className='graph-title'),

    # Graph EV 100KM
    html.Div([
        dcc.Graph(figure=fig_ev_100km, style={"height": "10000px", "width":"100%"}),
    ], className='graph-container-1', style={'overflow-y':'auto', 'height':'600px'}),

    # Collapsible content:
    html.Details([
        html.Summary('Analysis'),
        html.Div(
            className="collapsible-content",
            children=[])
    ]),
    

    # Title
    html.Div(id='anchor-loc-2'), # Specify location with this
    html.Div("Traditional Fuel Compared against Consumer Price Index (CPI)", className='graph-title'),

    # Graph 14
    html.Div([
        dcc.Graph(className='graph-container-1 graph-grow', figure=fig_14)
    ]),

    # Collapsible content:
    html.Details([
        html.Summary('Analysis'),
        html.Div(
            className="collapsible-content",
            children=convert_txt_to_html(f'{analysis_path}/Automotive Fuel and CPI Index Number.txt'))
    ]),

    # Title
    html.Div(id='anchor-loc-4'), # Specify location with this
    html.Div("Gasoline Vehicle Cost per 100KM", className='graph-title'),

    # Graph Gasoline Vehicle 100KM
    html.Div([
        dcc.Graph(className='graph-container-1 graph-grow', figure=fig_gas_100km)
    ]),

    # Collapsible content:
    html.Details([
        html.Summary('Analysis'),
        html.Div(
            className="collapsible-content",
            children=[])
    ]),
])


sidebar = html.Div(className='sidebar', children=[
    "Sidebar Menu",
    html.A(href='#anchor-loc-1', children=[
        html.Div('Charge Stations in Australia', className='sidebar-selection-box'),
    ]),
    html.A(href='#anchor-loc-3', children=[
        html.Div('EV Cost per 100km', className='sidebar-selection-box'),
    ]),
    html.A(href='#anchor-loc-2', children=[
        html.Div('Fuel vs CPI', className='sidebar-selection-box'),
    ]),
    html.A(href='#anchor-loc-4', children=[
        html.Div('Gasoline Vehicle Cost per 100km', className='sidebar-selection-box'),
    ]),

    
])

layout = html.Div(className='content-page', children=[
    sidebar,
    page_content,
])
