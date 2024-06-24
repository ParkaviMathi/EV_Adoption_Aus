from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import dash_bootstrap_components as dbc



app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

df = pd.read_csv('/Users/gillyrosic/Desktop/GitHub/FDMDataEngGrpProject/cleaned_data/cnty_type_sales.csv')

ev_types = df['powertrain'].unique().tolist()
ev_types.append('ALL')


app.layout = html.Div([
    #html.H4('Life expentancy progression of countries per continents'),
    dbc.Row([dbc.Col(  
    dcc.Dropdown(id="slct_country",
                 options=sorted(df['region'].unique().tolist()), # Defined above
                 multi=False,
                 value=sorted(df['region'].unique().tolist())[0],
                 style={'width': "40%"},
                 clearable=False ) ), dbc.Col(
    dcc.Dropdown(id="slct_type",
                 options=sorted(ev_types), # Defined above
                 multi=False,
                 value='ALL',
                 style={'width': "40%"},
                 clearable=False ) ) ] ),
    dcc.Graph(id="graph")
    
])


@app.callback(
    Output("graph", "figure"), 
    Input("slct_country", "value"),
    Input("slct_type", "value"))

def update_line_chart(continents, d_var):

    df = pd.read_csv('/Users/gillyrosic/Desktop/GitHub/FDMDataEngGrpProject/cleaned_data/cnty_type_sales.csv')
    mask = df[df['region']==continents]

    if d_var != 'ALL':
        mask = mask[mask['powertrain']==d_var]

    #make plot
    fig = go.Figure()
    #plots ev data
    fig = px.line(mask, 
        x="year", y="sales", color='powertrain')
    return fig


app.run_server(debug=True)