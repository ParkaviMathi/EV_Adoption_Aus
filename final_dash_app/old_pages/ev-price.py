import dash
from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import dash_bootstrap_components as dbc

dash.register_page(__name__, name='EV Price Information')


## ------ Graph 3_1 ------- ##
in_file_path_3_1 = "cleaned_data/electric_vehicle_ranges_ev_database.csv"
df_3_1 = pd.read_csv(in_file_path_3_1)

df_3_1 = df_3_1.sort_values(by='Range (km)', ascending=False) 
df_3_1 = df_3_1[:10][::-1] # A hacky solution. [::-1] reverses order. In horizontal bar chart i would like best range to be at top.

fig_3_1 = px.bar(
    df_3_1,
    y='Vehicle',
    x='Range (km)',
    orientation='h'
)

## ------ Graph 3_2 ------- ##
in_file_path_3_2 = "cleaned_data/electric_vehicle_energy_consumption_ev_database.csv"
df_3_2 = pd.read_csv(in_file_path_3_2)

df_3_2 = df_3_2.sort_values(by='Consumption (Wh/km)', ascending=True) # Lowest consumption first 
df_3_2 = df_3_2[:10][::-1] # A hacky solution. [::-1] reverses order. In horizontal bar chart i would like best range to be at top.

fig_3_2 = px.bar(
    df_3_2,
    y='Vehicle',
    x='Consumption (Wh/km)',
    orientation='h'
)

## ------ GRAPH 7 ------ ##


in_file_path_7 = "cleaned_data/cleaned_ev_prices_comparison(cleaned).csv"
df_7 = pd.read_csv(in_file_path_7)

fig_7 = px.bar(
    df_7,
    x='Model',
    y='Price',
    color='Country',
    title='Price Comparison of Car Models by Country',
    labels={'Model': 'EV Model', 'Price': 'Price (Australian Dollar)'},
    barmode='group'
)

# Update layout for better readability
fig_7.update_layout(
    xaxis_title='EV Model',
    yaxis_title='Price (Australian Dollar)',
    legend_title='Country',
    bargap=0.15,
    bargroupgap=0.1
)


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

# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------

# String defined for testing purpose -> content to be filled in later
very_long_string = "Lorem ipsum dolor sit amet, \
    consectetur adipisicing elit, sed do eiusmod \
        tempor incididunt ut labore et dolore magna \
            aliqua. Ut enim ad minim veniam, quis \
                nostrud exercitation ullamco laboris \
                    nisi ut aliquip ex ea commodo consequat."


page_content = html.Div(className='graph-page-type', children=[
    html.Div(id='test-loc'), # Specify location with this
    html.Div("EV Price Information", className='graph-title'),

    # Graph
    html.Div([
        dcc.Graph(className='graph-container-1 graph-grow',figure=fig_7),
    ]),
    
    # Collapsible content:
    html.Details([
        html.Summary('Analysis'),
        html.Div(
            className="collapsible-content",
            children=[
                html.P(very_long_string),
                html.P(very_long_string),
                html.P(very_long_string),
                html.P(very_long_string),
                html.P(very_long_string),
                html.P(very_long_string),
            ])
    ]),
   
    html.Div([
        dcc.Graph(className='graph-container-1 graph-grow',figure=fig_3_1),
    ]),
    
    # Collapsible content:
    html.Details([
        html.Summary('Analysis'),
        html.Div(
            className="collapsible-content",
            children=[
                html.P(very_long_string),
                html.P(very_long_string),
                html.P(very_long_string),
                html.P(very_long_string),
                html.P(very_long_string),
                html.P(very_long_string),
            ])
    ]),

    html.Div(id='test-loc-2'), # Specify location with this
    html.Div("Another title :O", className='graph-title'),

    html.Div([
        dcc.Graph(className='graph-container-1 graph-grow',figure=fig_3_2),
    ]),

    # Collapsible content:
    html.Details([
        html.Summary('Analysis'),
        html.Div(
            className="collapsible-content",
            children=[
                html.P(very_long_string),
                html.P(very_long_string),
                html.P(very_long_string),
                html.P(very_long_string),
                html.P(very_long_string),
                html.P(very_long_string),
            ])
    ]),

    html.Div([
        dcc.Graph(className='graph-container-1 graph-grow', figure=fig_14)
    ]),

    # Collapsible content:
    html.Details([
        html.Summary('Analysis'),
        html.Div(
            className="collapsible-content",
            children=[
                html.P(very_long_string),
                html.P(very_long_string),
                html.P(very_long_string),
                html.P(very_long_string),
                html.P(very_long_string),
                html.P(very_long_string),
            ])
    ]),
    

])

sidebar = html.Div(className='sidebar', children=[
    "Sidebar Menu",
    html.A(href='#test-loc', children=[
        html.Div('Test!', className='sidebar-selection-box'),
    ]),
    html.A(href='#test-loc-2', children=[
        html.Div('Test 2!',className='sidebar-selection-box')
    ]),
])

layout = html.Div(className='content-page', children=[
    sidebar,
    page_content,
])


