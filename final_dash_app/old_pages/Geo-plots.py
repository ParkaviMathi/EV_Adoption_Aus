import dash
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
import numpy as np
from plotly.subplots import make_subplots
import matplotlib.cm as cm
import matplotlib.colors as mcolors
import dash_daq as daq # This is for cool toggle switch!


dash.register_page(__name__, name='Geo Plots')

from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px


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


## --------- GRAPH 10 ----------- ## ------------------------------------------

# Read in CSV file

File_Path = "cleaned_data/Population_Income_Registration.csv"
merged_pd_df = pd.read_csv(File_Path)

# Convert relevant columns to numeric types
numeric_columns = [
    'Population in 2021', 'Population in 2022', 'Population in 2023',
    'Median Age of Earners', 'Registrations_2021', 'Registrations_2022', 'Registrations_2023'
]

for column in numeric_columns:
    merged_pd_df[column] = pd.to_numeric(merged_pd_df[column], errors='coerce')

# Ensure there are no null values after conversion (this step can be skipped if data is clean)
merged_pd_df.dropna(subset=numeric_columns, inplace=True)


# Filter data for each fuel type
hybrid_df = merged_pd_df[merged_pd_df['Fuel Type'] == 'Hybrid/PHEV']
bev_df = merged_pd_df[merged_pd_df['Fuel Type'] == 'BEV']
hfcev_df = merged_pd_df[merged_pd_df['Fuel Type'] == 'HFCEV']

# Function to normalize data by population
def normalize_by_population(df, year):
    return df[f'Registrations_{year}'].astype(float) / df[f'Population in {year}'].astype(float)

# Color map for different fuel types
fuel_type_colors = {
    'Hybrid/PHEV': 'blue',
    'BEV': 'green',
    'HFCEV': 'orange'
}

# Create traces for each fuel type and each year
traces = []

for fuel_type, df in [('Hybrid/PHEV', hybrid_df), ('BEV', bev_df), ('HFCEV', hfcev_df)]:
    for year in [2021, 2022, 2023]:
        if not df.empty:  # Check if the DataFrame is not empty
            # Normalize registration data by population
            normalized_registrations = normalize_by_population(df, year)
            
            # Use a colormap for visual differentiation
            norm = mcolors.Normalize(vmin=normalized_registrations.min(), vmax=normalized_registrations.max())
            cmap = cm.viridis
            colors_mapped = [mcolors.rgb2hex(cmap(norm(value))) for value in normalized_registrations]
            
            trace = go.Scattermapbox(
                lat=df['Lat_precise'],
                lon=df['Long_precise'],
                mode='markers',
                marker=dict(
                    size=10,
                    opacity=0.7,
                    color=colors_mapped,
                    colorscale='Viridis',
                    showscale=True,
                    colorbar=dict(title=f'Normalized Registrations {year}')
                ),
                name=f'{fuel_type} {year}',
                hoverinfo='text',
                text=df['Local Government Area'] + '<br>' +
                     f'Population {year}: ' + df[f'Population in {year}'].astype(str) + '<br>' +
                     f'Registrations {year}: ' + df[f'Registrations_{year}'].astype(str)
            )
            traces.append(trace)

# Create the Plotly figure
fig_10 = make_subplots(rows=1, cols=1)

# Add all traces to the figure
for trace in traces:
    fig_10.add_trace(trace)

# Define the layout
fig_10.update_layout(
    title='Effect of Income and Population on Electric Vehicle Registrations (2021-2023)',
    mapbox=dict(
        style='open-street-map',
        center=dict(
            lat=-25.2744,
            lon=133.7751
        ),
        zoom=2.8,
        
    ),
    legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.01),
        
    legend_title="Fuel Type and Year"
)

# String defined for testing purpose -> content to be filled in later
very_long_string = "Lorem ipsum dolor sit amet, \
    consectetur adipisicing elit, sed do eiusmod \
        tempor incididunt ut labore et dolore magna \
            aliqua. Ut enim ad minim veniam, quis \
                nostrud exercitation ullamco laboris \
                    nisi ut aliquip ex ea commodo consequat."


page_content = html.Div(className='graph-page-type', children=[
    html.Div(id='test-loc'), # Specify location with this
    html.Div("Geo Plots", className='graph-title'),

    # Graph options
    html.Div(className='graph-opts-1',children=[
        dcc.Dropdown(id="slct_year_1",
                 options=selection_fuel_type_options_1, # Defined above
                 multi=False,
                 value="All",
                 ),
    
        # Cool looking toggle switch!
        daq.ToggleSwitch(
            id="toggle_size_1",
            value=False,
            label=["Size Off", "Size On"],
            color="#ffe102",
            style={"color": "#black"},)
    ]),
    
    # Graph
    html.Div(children=[
        dcc.Graph(id='graph_1',className='graph-container-1 graph-grow', figure={}),
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

    # Graph
    html.Div([
        dcc.Graph(className='graph-container-1 graph-grow', figure=fig_2),
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
    
    # Graph
    html.Div([
        dcc.Graph(className='graph-container-1 graph-grow', figure=fig_8),
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

    # Graph
    html.Div([
        dcc.Graph(className='graph-container-1 graph-grow', figure=fig_10),
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


