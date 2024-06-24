import dash
from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from txt_to_html import convert_txt_to_html


pg_title = 'EV Adoption Rates'
dash.register_page(__name__, name=pg_title)


## ------ Graph 11 ------- ##

file_path_11 = 'cleaned_data/top-cntr-shares.csv'
df_11 = pd.read_csv(file_path_11)

regions_11 = sorted(df_11['region'].unique().tolist())

## ------- GRAPH 6 ------ ##
file_path_6 = 'cleaned_data/countries_ev_data(IEA).csv'
df_6 = pd.read_csv(file_path_6)

## --------- GRAPH 12 ---------- ##
file_path_12 = 'cleaned_data/choropleth_cntry.csv'
df_12 = pd.read_csv(file_path_12)

years_12 = sorted(df_12['year'].unique().tolist(),reverse=True)


## ------ Graph 9 ------- ##
df_9 = pd.read_csv('cleaned_data/cnty_type_sales.csv')
ev_types_9 = df_9['powertrain'].unique().tolist()
ev_types_9.append('ALL')



# String defined for testing purpose -> content to be filled in later
very_long_string = "Lorem ipsum dolor sit amet, \
    consectetur adipisicing elit, sed do eiusmod \
        tempor incididunt ut labore et dolore magna \
            aliqua. Ut enim ad minim veniam, quis \
                nostrud exercitation ullamco laboris \
                    nisi ut aliquip ex ea commodo consequat."

analysis_path = 'plot_analysis_txts'

## ------ Page Layout 1 ------- ##
page_content = html.Div(className='graph-page-type',children=[

    # Page title:
    html.Div(pg_title, className='page-title'),

    # Title
    html.Div(id='anchor-loc-1'), # Specify location with this
    html.Div("Countries with Highest Adoption Rates", className='graph-title'),

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

    # Graph 11
    html.Div([
        dcc.Graph(id="graph_11", className='graph-container-1 graph-grow'),
    ]),
    
    # Collapsible content:
    html.Details([
        html.Summary('Analysis'),
        html.Div(
            className="collapsible-content",
            children=convert_txt_to_html(f'{analysis_path}/Countries with Highest Adoption Rates.txt'))
    ]),

    # Title
    html.Div(id='anchor-loc-3'), # Specify location with this
    html.Div("Choropleth for Country Adoption Rates per Year", className='graph-title'),

    # Graph options
    html.Div(className="graph-opts-1", children=[
        dcc.Dropdown(id="slct_year_12",
            options=years_12, # Defined above
            multi=False,
            value=years_12[0],
            style={'width': "70%", "margin":"0 auto"}, # Hard coded 
            searchable=False
        ),
    ]),
    
    # Graph 12
    html.Div([
        dcc.Graph(id="graph_12", className='graph-container-1 graph-grow'),
    ]),

    # Collapsible content:
    html.Details([
        html.Summary('Analysis'),
        html.Div(
            className="collapsible-content",
            children=convert_txt_to_html(f'{analysis_path}/EV Adoption around the world.txt'))
    ]),


    # Title
    html.Div(id='anchor-loc-2'), # Specify location with this
    html.Div("EV vs ICE Car Sales for Selected Country", className='graph-title'),
    
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

    # Graph 6
    html.Div([
        dcc.Graph(id="graph_6", className='graph-container-1 graph-grow'),
    ]),
    
    # Collapsible content:
    html.Details([
        html.Summary('Analysis'),
        html.Div(
            className="collapsible-content",
            children=convert_txt_to_html(f'{analysis_path}/EV Car Sales vs ICE Car Sales (Australia).txt'))
    ]),

    # Title
    html.Div(id='anchor-loc-4'), # Specify location with this
    html.Div("EV Sales based on Powertrain Type for Selected Country", className='graph-title'),

    # Graph options
    html.Div(className='graph-opts-1',children=[
        dbc.Col(  
            dcc.Dropdown(id="slct_country_9",
                        options=sorted(df_9['region'].unique().tolist()), # Defined above
                        multi=False,
                        value=sorted(df_9['region'].unique().tolist())[0],
                        # style={'width': "40%"},
                        clearable=False 
        )), 
        dbc.Col(
            dcc.Dropdown(id="slct_type_9",
                        options=sorted(ev_types_9), # Defined above
                        multi=False,
                        value='ALL',
                        # style={'width': "40%"},
                        clearable=False 
        )) 
    ]),

    # Graph
    html.Div([
        dcc.Graph(id="graph_9", className='graph-container-1 graph-grow'),
    ]),
    
    # Collapsible content:
    html.Details([
        html.Summary('Analysis'),
        html.Div(
            className="collapsible-content",
            children=convert_txt_to_html(f'{analysis_path}/Electric Vehicle Registrations by Fuel Type and Year (Australia).txt'))
    ]),
    
])

sidebar = html.Div(className='sidebar', children=[
    "Sidebar Menu",
    html.A(href='#anchor-loc-1', children=[
        html.Div('Country Adoption Rates', className='sidebar-selection-box'),
    ]),
    html.A(href='#anchor-loc-3', children=[
        html.Div('Choropleth Adoption Rates', className='sidebar-selection-box'),
    ]),
    html.A(href='#anchor-loc-2', children=[
        html.Div('EV vs ICE sales', className='sidebar-selection-box'),
    ]),
    html.A(href='#anchor-loc-4', children=[
        html.Div('EV Powertrain Sales', className='sidebar-selection-box'),
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


# ----------- Callback function graph_9 -----------
@callback(
    [Output("graph_9", "figure")],

    [Input("slct_country_9", "value"),
    Input("slct_type_9", "value")])
def update_line_chart(continents_9, d_var_9):
    
    df_9 = pd.read_csv('cleaned_data/cnty_type_sales.csv')
    mask_9 = df_9[df_9['region']==continents_9]

    if d_var_9 != 'ALL':
        mask_9 = mask_9[mask_9['powertrain']==d_var_9]

    #make plot
    fig_9 = go.Figure()
    #plots ev data
    fig_9 = px.line(mask_9, 
        x="year", y="sales", color='powertrain')


    return [fig_9]
