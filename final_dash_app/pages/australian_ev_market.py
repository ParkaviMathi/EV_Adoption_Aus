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


pg_title = 'Australian EV Market'
dash.register_page(__name__, name=pg_title)


# ------- Graph 1 -------------
vehicle_registration_file_path = 'cleaned_data/aaa_geographic_vehicle_distribution_lats_longs.csv'
df_1 = pd.read_csv(vehicle_registration_file_path)
df_1 = df_1[df_1["Registrations as at 31 January 2023"] > 0] # Remove 0 registered sites

# Specify color:
color_dict_1 = {'ICE': '#3C8DFF', 'BEV': '#FFA500', "Hybrid/PHEV":'#32CD32'}
df_1['Color'] = df_1['Fuel Type'].apply(lambda x: color_dict_1.get(x))


selection_fuel_type_options_1 = []

option_dict_1 = {"label": "All", "value": "All"}
selection_fuel_type_options_1.append(option_dict_1) # Have an ALL option

# Iterate through available fuel types and add as option to filter
for fuel_type in df_1["Fuel Type"].unique():
    option_dict_1 = {"label": fuel_type, "value": fuel_type}
    selection_fuel_type_options_1.append(option_dict_1)    


# *** GRAPH 8 *** ----------------------------------------------------------------

File_Path = "cleaned_data/Population_Income_Registration(cleaned).csv"
high_income_low_registration_df = pd.read_csv(File_Path)
# Create a scatter mapbox plot using Plotly
fig_8 = px.scatter_mapbox(high_income_low_registration_df,
    lat='Lat_precise',
    lon='Long_precise',
    opacity=0.7,
    size=None,
    hover_name="Local Government Area",
    hover_data=["Mean Income", "Registrations"]
)

# Update the layout to use an OpenStreetMap tile
fig_8.update_layout(
    mapbox=dict(
        style='open-street-map',
        zoom=3.1,  # Adjust zoom level based on the density of points
        center=dict(lat=-25.2744,
            lon=133.7751)
            
    ),
    title='High Income, Low EV Registrations in Australia',
    autosize=True,
    height=600
)
fig_8.update_layout(margin={"r":0, "t":50, "l":0, "b":10})

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
    html.Div("EV and ICE Vehicle Distribution in Australia", className='graph-title'),

    # Graph options
    html.Div(className='graph-opts-1',children=[
        dcc.Dropdown(id="slct_year_1",
                 options=selection_fuel_type_options_1, # Defined above
                 multi=False,
                 value="All",
                 style={"width": "70%"}
                 ),
    
        # Cool looking toggle switch!
        daq.ToggleSwitch(
            id="toggle_size_1",
            value=True,
            label=["Size Off", "Size On"],
            color="#ffe102",
            style={"color": "#black"},)
    ]),
    
    # Graph 1
    html.Div(children=[
        dcc.Graph(id='graph_1',className='graph-container-1 graph-grow', figure={}),
    ]),

    # Collapsible content:
    html.Details([
        html.Summary('Analysis'),
        html.Div(
            className="collapsible-content",
            children=convert_txt_to_html(f'{analysis_path}/EV and ICE Vehicle Distribution.txt'))
    ]),


    # Title
    html.Div(id='anchor-loc-2'), # Specify location with this
    html.Div("High EV Potential Areas in Australia (High Income - Low EV Registrations)", className='graph-title'),

    # Graph 8
    html.Div([
        dcc.Graph(className='graph-container-1 graph-grow', figure=fig_8),
    ]),

    # Collapsible content:
    html.Details([
        html.Summary('Analysis'),
        html.Div(
            className="collapsible-content",
            children=convert_txt_to_html(f'{analysis_path}/High Income, Low EV Registrations.txt'))
    ]),


    # Title
    html.Div(id='anchor-loc-3'), # Specify location with this
    html.Div("Price Comparison of EV Models with Other Countries", className='graph-title'),

    # Graph 7
    html.Div([
        dcc.Graph(className='graph-container-1 graph-grow',figure=fig_7),
    ]),
    
    # Collapsible content:
    html.Details([
        html.Summary('Analysis'),
        html.Div(
            className="collapsible-content",
            children=convert_txt_to_html(f'{analysis_path}/Price Comparison of Car Models by Country.txt'))
    ]),


    # Title
    html.Div(id='anchor-loc-4'), # Specify location with this
    html.Div("Australian EV Sales vs Global EV Sales", className='graph-title'),

    # Graph options
    html.Div(className='graph-opts-1',children=[
        dbc.Col(  
        dcc.Dropdown(id="slct_comparison_5",
                    options=['Average', 'Top Country'], # Defined above
                    multi=False,
                    value='Average',
                    # style={'width': "40%"},
                    clearable=False
                    )), 
        dbc.Col(
        dcc.Dropdown(id="slct_data_5",
                    options=['Sales', 'Sales Share'], # Defined above
                    multi=False,
                    value='Sales',
                    # style={'width': "40%"},
                    clearable=False
        ))
    ]),
    
    # Graph 5
    html.Div([
        dcc.Graph(id="graph_5", className='graph-container-1 graph-grow', figure={}),
    ]),

    # Collapsible content:
    html.Details([
        html.Summary('Analysis'),
        html.Div(
            className="collapsible-content",
            children=convert_txt_to_html(f'{analysis_path}/Sales of EVs in Australia vs Average of Other Countries.txt'))
    ]),


])

sidebar = html.Div(className='sidebar', children=[
    "Sidebar Menu",
    html.A(href='#anchor-loc-1', children=[
        html.Div('EV & ICE Distribution', className='sidebar-selection-box'),
    ]),
    html.A(href='#anchor-loc-2', children=[
        html.Div('Areas of Potential Expansion', className='sidebar-selection-box'),
    ]),
    html.A(href='#anchor-loc-3', children=[
        html.Div('EV Price Comparison', className='sidebar-selection-box'),
    ]),
    html.A(href='#anchor-loc-4', children=[
        html.Div('EV Sales Australia vs Global', className='sidebar-selection-box'),
    ]),
])


layout = html.Div(className='content-page',children=[sidebar, page_content])



# ----------- Callback function for graph_1
@callback(
    [Output(component_id='graph_1', component_property='figure')], # Takes second part of output
    [Input(component_id='slct_year_1', component_property='value'),
     Input(component_id='toggle_size_1', component_property='value')]
)
def update_graph(option_slctd_1, toggle_size_1):

    dff_1 = df_1.copy()

    if option_slctd_1 != 'All':
        dff_1 = dff_1[dff_1["Fuel Type"] == option_slctd_1]

    if toggle_size_1:
        size_opt_1 = "Registrations as at 31 January 2023"
    else:
        size_opt_1 = None        

    # Plotly Express
    fig_1 = px.scatter_mapbox(dff_1,
        lon = "Longitude",
        lat = "Latitude",
        color="Fuel Type",
        color_discrete_map=color_dict_1,
        hover_data="Fuel Type",
        size=size_opt_1,
        opacity=0.7,
        zoom = 3,
        title = 'EV and ICE Vehicle distribution',)


    fig_1.update_layout(mapbox_style="open-street-map")
    fig_1.update_layout(margin={"r":0, "t":50, "l":0, "b":10}) 
    fig_1.update_layout(mapbox=dict(
        center=go.layout.mapbox.Center(
            lat=-27.2744,
            lon=133.7751),
            zoom=2.8 ),

        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01)
            )# Set margin of plot (right, top, left, bottom)

    fig_1['data'][0]['showlegend']=True

    fig_1.layout.uirevision = True # Stop map resetting

    return [fig_1]


# ------------ Callback function graph_5 -----------
@callback(
    [Output("graph_5", "figure")],

    [Input("slct_comparison_5", "value"),
    Input("slct_data_5", "value")])
def update_line_chart(comp_5, d_var_5):

    # Select top country
    if comp_5 == 'Top Country':
        if d_var_5 == 'Sales':
            comp_5 = 'China'
        else:
            comp_5 = 'Norway'

    df_5 = pd.read_csv('cleaned_data/australia_ev_comp(plotly).csv')
    mask_5 = df_5.region.isin(['Australia', comp_5])
    fig_5 = px.line(df_5[mask_5], 
        x="year", y=d_var_5.split(' ')[-1].lower(), color='region')

    return [fig_5]

