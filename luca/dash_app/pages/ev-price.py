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
    width=1000,  # Width of the plot
    height=600,   # Height of the plot
    legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.01
    )
)

# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------

layout = html.Div([
    html.H4('EV Price Information'),
   # dcc = Dash Core Components -> Gives you access to many interactive components including dropdowns, checklists etc
    html.Br(),

    dcc.Graph(figure=fig_7, style={'width': '80vw', 
                                    'height': '70vh',
                                    'margin': '0 auto'}),
   
   
    html.Br(),

    dcc.Graph(figure=fig_3_1, style={'width': '80vw', 
                                    'height': '70vh',
                                    'margin': '0 auto'}),
    

    html.Br(),
    
    dcc.Graph(figure=fig_3_2, style={'width': '80vw', 
                                    'height': '70vh',
                                    'margin': '0 auto'}),

    
    html.Br(),
    
    dcc.Graph(figure=fig_14, style={'width': '80vw', 
                                    'height': '70vh',
                                    'margin': '0 auto'})

])


