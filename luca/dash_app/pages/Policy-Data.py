import dash
from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import dash_bootstrap_components as dbc

dash.register_page(__name__, name='Policy Information')




## ------ Graph 1 ------- ##

file_path_11 = 'cleaned_data/top-cntr-shares.csv'
df_11 = pd.read_csv(file_path_11)

regions_11 = sorted(df_11['region'].unique().tolist())

## ------- GRAPH 2 ------ ##
file_path_6 = 'cleaned_data/countries_ev_data(IEA).csv'
df_6 = pd.read_csv(file_path_6)

## --------- GRAPH 3 ---------- ##
file_path_12 = 'cleaned_data/choropleth_cntry.csv'
df_12 = pd.read_csv(file_path_12)

years_12 = sorted(df_12['year'].unique().tolist(),reverse=True)


## ------ Page Layout 1 ------- ##
layout = html.Div([
    html.H4('Policy Information'),

    html.Br(),

    dcc.Dropdown(id="slct_country_11",
                 options=regions_11, # Defined above
                 multi=True,
                 value=regions_11,
                 style={'width': "40%"},
                 searchable=False
                 ),
    dcc.Graph(id="graph_11"),

    html.Br(),


    dbc.Row([
        
    dbc.Col(
        dcc.Dropdown(id="slct_country_6",
                 options=sorted(df_6['region'].unique().tolist()), # Defined above
                 multi=False,
                 value=sorted(df_6['region'].unique().tolist())[0],
                 style={'width': "40%"},
                 clearable=False
                 )), dbc.Col(
        dcc.Dropdown(id="slct_type_6",
                 options=['Sales', 'Sales Share'], # Defined above
                 multi=False,
                 value='Sales',
                 style={'width': "40%"},
                 clearable=False
                 ) ) ] ),
    dcc.Graph(id="graph_6"),

    html.Br(),

    dcc.Dropdown(id="slct_year_12",
                 options=years_12, # Defined above
                 multi=False,
                 value=years_12[0],
                 style={'width': "40%"},
                 searchable=False
                 ),
    dcc.Graph(id="graph_12"),

    
])


@callback(
    Output("graph_6", "figure"),
    Output("graph_11", "figure"),
    Output("graph_12", "figure"),

    Input("slct_country_11", "value"),

    Input("slct_country_6", "value"),
    Input("slct_type_6", "value"),
    
    Input("slct_year_12", "value"))

def update_line_chart(regions_11, continents_6, d_var_6, year_12):

    mask_11 = df_11.region.isin(regions_11)

    fig_11 = px.line(df_11[mask_11], 
            x="year", y="share", color='region')
    
    fig_11.update_layout(
    title='Countries with Highest Adoption rates',
    xaxis_title='Year',
    yaxis_title='EV Car Sales Share',
    legend_title='Country'
    )


    ## --- Graph 2 --- ##
    dff_6 = df_6.copy()
    mask_6 = dff_6[df_6['region']==continents_6]

    #make plot
    fig_6 = go.Figure()
    #plots ev data
    fig_6.add_trace(go.Scatter(x=dff_6['year'], y=mask_6['ev_'+d_var_6.split(' ')[-1].lower()],
                    mode='lines',
                    name='EV Car ' + d_var_6))
    # plots ICE data
    fig_6.add_trace(go.Scatter(x=dff_6['year'], y=mask_6['fossil_'+d_var_6.split(' ')[-1].lower()],
                    mode='lines',
                    name='ICE Car ' + d_var_6))
    
    fig_6.update_layout(
    title='Country Comparison',
    xaxis_title='Year',
    )


    ## --- GRAPH 3 --- ##
    dff_12 = df_12.copy()

    dff_12 = dff_12[dff_12['year']==year_12]
    fig_12 = px.choropleth(dff_12, locations="alpha",
                    color="ev_share", # lifeExp is a column of gapminder
                    hover_name="region", # column to add to hover information
                    color_continuous_scale=px.colors.sequential.Plasma)
    

    return fig_6, fig_11, fig_12