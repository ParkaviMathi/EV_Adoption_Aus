import pandas as pd
import plotly.express as px  # (version 4.7.0 or higher)
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output  # pip install dash (version 2.0.0 or higher)
import dash_bootstrap_components as dbc # pip install dash-bootstrap-components

app = Dash(__name__)
# ---------------------------------------------
# Load in cleaned data of vehicle registrations with Latitude and Longitude values

vehicle_registration_file_path = 'cleaned_data/aaa_geographic_vehicle_distribution_lats_longs.csv'
df = pd.read_csv(vehicle_registration_file_path)
df = df[df["Registrations as at 31 January 2023"] > 0] # Remove 0 registered sites

# Specify color:
color_dict = {'ICE': '#3C8DFF', 'BEV': '#FFA500', "Hybrid/PHEV":'#32CD32'}
df['Color'] = df['Fuel Type'].apply(lambda x: color_dict.get(x))


print(df.head())


selection_fuel_type_options = []

option_dict = {"label": "All", "value": "All"}
selection_fuel_type_options.append(option_dict) # Have an ALL option

# Iterate through available fuel types and add as option to filter
for fuel_type in df["Fuel Type"].unique():
    option_dict = {"label": fuel_type, "value": fuel_type}
    selection_fuel_type_options.append(option_dict)    



# ------------------------------------------------------------------------------
# App layout
app.layout = html.Div([

    html.H1("Web Application Dashboards with Dash", style={'text-align': 'center'}),

    # dcc = Dash Core Components -> Gives you access to many interactive components including dropdowns, checklists etc
    dcc.Dropdown(id="slct_year",
                 options=selection_fuel_type_options, # Defined above
                 multi=False,
                 value="All",
                 style={'width': "40%"}
                 ),
    
    dcc.Checklist(id="toggle_size",options=['Toggle Size'], value=[]),


    html.Div(id='output_container', children=[]),
    html.Br(),
    

    dcc.Graph(id='my_bee_map', figure={}, style={'width': '90vw', 
                                                 'height': '70vh',
                                                 'margin': '0 auto'})

])



# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
# component_id refers to IDs above!
@app.callback(
    [Output(component_id='output_container', component_property='children'), # Takes first part of output
     Output(component_id='my_bee_map', component_property='figure')], # Takes second part of output
    [Input(component_id='slct_year', component_property='value'),
     Input(component_id='toggle_size', component_property='value')]
)
def update_graph(option_slctd, toggle_size):
    print(option_slctd)
    print(type(option_slctd))

    container = "The type chosen by user was: {}".format(option_slctd)

    print("TOGGLE")
    print(toggle_size)

    dff = df.copy()

    if len(toggle_size) == 0:
        size_opt = None
    else:
        size_opt = "Registrations as at 31 January 2023"
    
    # # Interactive selection - Look into for different fuel types!
    # size_opt = None
    # if toggle_size == None:
    #     size_opt = None
    # else:
    #     print(toggle_size)

    print(f"Selected size opt: {size_opt}")

    if option_slctd != 'All':
        dff = dff[dff["Fuel Type"] == option_slctd]
    # dff = dff[dff["Affected by"] == "Varroa_mites"]

    # Plotly Express
    fig = px.scatter_mapbox(dff,
        lon = dff["Longitude"],
        lat = dff["Latitude"],
        color="Fuel Type",
        color_discrete_map=color_dict,
        hover_data="Fuel Type",
        size=size_opt,
        opacity=0.7,
        zoom = 3,
        title = 'Dash Plotly Test',)


    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r":0, "t":50, "l":0, "b":10}) # Set margin of plot (right, top, left, bottom)

    fig['data'][0]['showlegend']=True
    return container, fig


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)