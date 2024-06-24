from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)


app.layout = html.Div([
    #html.H4('Life expentancy progression of countries per continents'),
    dcc.Dropdown(id="slct_comparison",
                 options=['Average', 'Top Country'], # Defined above
                 multi=False,
                 value='Average',
                 style={'width': "40%"}
                 ),
    dcc.Dropdown(id="slct_data",
                 options=['Sales', 'Sales Share'], # Defined above
                 multi=False,
                 value='Sales',
                 style={'width': "40%"}
                 ),
    dcc.Graph(id="graph")
])


@app.callback(
    Output("graph", "figure"), 
    Input("slct_comparison", "value"),
    Input("slct_data", "value"))

def update_line_chart(comp, d_var):
    if comp == 'Top Country':
        if d_var == 'Sales':
            comp = 'China'
        else:
            comp = 'Norway'

    df = pd.read_csv('/Users/gillyrosic/Desktop/GitHub/FDMDataEngGrpProject/cleaned_data/australia_ev_comp(plotly).csv')
    mask = df.region.isin(['Australia', comp])
    fig = px.line(df[mask], 
        x="year", y=d_var.split(' ')[-1].lower(), color='region')
    return fig


app.run_server(debug=True)