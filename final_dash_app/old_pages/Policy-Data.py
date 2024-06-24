import dash
from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import dash_bootstrap_components as dbc

# dash.register_page(__name__, name='Policy Information')




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


# String defined for testing purpose -> content to be filled in later
very_long_string = "Lorem ipsum dolor sit amet, \
    consectetur adipisicing elit, sed do eiusmod \
        tempor incididunt ut labore et dolore magna \
            aliqua. Ut enim ad minim veniam, quis \
                nostrud exercitation ullamco laboris \
                    nisi ut aliquip ex ea commodo consequat."

## ------ Page Layout 1 ------- ##
page_content = html.Div(className='graph-page-type',children=[

    html.Div(id='test-loc'), # Specify location with this
    html.Div("Policy Information", className='graph-title'),

    # Graph options
    html.Div(className='graph-opts-1' ,children=[
        dcc.Dropdown(id="slct_country_11",
                 options=regions_11, # Defined above
                 multi=True,
                 value=regions_11,
                #  style={'width': "40%"},
                 searchable=False
                 ),
    ]),

    # Graph
    html.Div(className='graph-container-1 graph-grow', children=[
        dcc.Graph(id="graph_11"),
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
    
    # Graph options
    html.Div(className='graph-opts-1', children=[
        # THIS IS SOO BAD
        dbc.Col(
            dcc.Dropdown(id="slct_country_6",
                    options=sorted(df_6['region'].unique().tolist()), # THESE SHOULD BE CACHED
                    multi=False,
                    value=sorted(df_6['region'].unique().tolist())[0],
                    # style={'width': "40%"},
                    clearable=False
                    )), dbc.Col(
            dcc.Dropdown(id="slct_type_6",
                    options=['Sales', 'Sales Share'], # THESE SHOULD BE CACHED
                    multi=False,
                    value='Sales',
                    # style={'width': "40%"},
                    clearable=False
                    )) 
    ]),

    # Graph
    html.Div(className='graph-container-1 graph-growth', children=[
        dcc.Graph(id="graph_6"),
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

    # Graph options
    html.Div(className="graph-opts-1", children=[
        dcc.Dropdown(id="slct_year_12",
            options=years_12, # Defined above
            multi=False,
            value=years_12[0],
            style={'width': "70%", "margin":"0 auto"}, # Hard coded because i cant be bothered
            searchable=False
        ),
    ]),
    
    # Graph
    html.Div(className='graph-container-1 graph-growth', children=[
        dcc.Graph(id="graph_12"),
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

layout = html.Div(className='content-page', children=[sidebar, page_content])


# --------- Callback function graph_6 -------------
@callback(
    [Output("graph_6", "figure")],
    [Input("slct_country_6", "value"),
    Input("slct_type_6", "value")])
def update_line_chart(continents_6, d_var_6):

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
    
    return [fig_6]



# ------------- Callback function for graph_12 --------------
@callback(
    [Output("graph_12", "figure")],
    [Input("slct_year_12", "value")])
def update_line_chart(year_12):

    dff_12 = df_12.copy()

    dff_12 = dff_12[dff_12['year']==year_12]
    fig_12 = px.choropleth(dff_12, locations="alpha",
                    color="ev_share", # lifeExp is a column of gapminder
                    hover_name="region", # column to add to hover information
                    color_continuous_scale=px.colors.sequential.Plasma)
    

    return [fig_12]


# ------------ Callback function for graph_11 -------------------
@callback(
    [Output("graph_11", "figure")],
    [Input("slct_country_11", "value")])
def update_line_chart_11(regions_11):

    mask_11 = df_11.region.isin(regions_11)

    fig_11 = px.line(df_11[mask_11], 
            x="year", y="share", color='region')
    
    fig_11.update_layout(
            title='Countries with Highest Adoption rates',
            xaxis_title='Year',
            yaxis_title='EV Car Sales Share',
            legend_title='Country'
        )
    
    return [fig_11]


