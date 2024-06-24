import dash
from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from sklearn.linear_model import LinearRegression
import numpy as np

dash.register_page(__name__, name='EV Retailer Information')

## ------ Graph 9 ------- ##
df_9 = pd.read_csv('cleaned_data/cnty_type_sales.csv')
ev_types_9 = df_9['powertrain'].unique().tolist()
ev_types_9.append('ALL')



## ------ GRAPH 3 ------- ##


File_Path_13 = "cleaned_data/Population_Income_Registration.csv"
merged_pd_df_13 = pd.read_csv(File_Path_13)

# Convert relevant columns to numeric types
numeric_columns_13 = [
    'Population in 2021', 'Population in 2022', 'Population in 2023',
    'Median Age of Earners', 'Registrations_2021', 'Registrations_2022', 'Registrations_2023'
]

for column in numeric_columns_13:
    merged_pd_df_13[column] = pd.to_numeric(merged_pd_df_13[column], errors='coerce')

# Ensure there are no null values after conversion (this step can be skipped if data is clean)
merged_pd_df_13.dropna(subset=numeric_columns_13, inplace=True)

# Extract relevant columns for plotting
income_13 = merged_pd_df_13['Mean Income']
registrations_2021_13 = merged_pd_df_13['Registrations_2021'].astype(float)
registrations_2022_13 = merged_pd_df_13['Registrations_2022'].astype(float)
registrations_2023_13 = merged_pd_df_13['Registrations_2023'].astype(float)


def add_trendline(fig_13, x_13, y_13, name_13, color_13):
    # Reshape x for sklearn
    x_13 = np.array(x_13).reshape(-1, 1)
    # Fit linear regression model
    model_13 = LinearRegression().fit(x_13, y_13)
    # Predict y values for trend line
    trend_y_13 = model_13.predict(x_13)
    # Add the trend line to the plot
    fig_13.add_scatter(x=x_13.flatten(), y=trend_y_13, mode='lines', name=f'Trend {name_13}', line=dict(color=color_13))




### ----- GRAPH 15 ------- ###
# Create a grouped bar chart
EV_Reg_by_Fuel_Type_15 = "cleaned_data/Population_Income_Registration(15).csv"

df_15 = pd.read_csv(EV_Reg_by_Fuel_Type_15)

fig_15 = px.bar(df_15, 
             x='Year', 
             y='Registrations', 
             color='Fuel Type', 
             barmode='group',
             title='Electric Vehicle Registrations by Fuel Type and Year',
             labels={'Year': 'Year', 'Registrations': 'Total Registrations'},
             category_orders={'Year': ['2021', '2022', '2023']})

# Define the layout with legend position
fig_15.update_layout(
    legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.01
    )
)





layout = html.Div([
    html.H4('EV Retailer Information'),
    dbc.Row([dbc.Col(  
        dcc.Dropdown(id="slct_comparison_5",
                    options=['Average', 'Top Country'], # Defined above
                    multi=False,
                    value='Average',
                    style={'width': "40%"},
                    clearable=False
                    ) ), dbc.Col(
        dcc.Dropdown(id="slct_data_5",
                    options=['Sales', 'Sales Share'], # Defined above
                    multi=False,
                    value='Sales',
                    style={'width': "40%"},
                    clearable=False
                    ) ) ]),
    dcc.Graph(id="graph_5"),


    html.Br(),



    dbc.Row([dbc.Col(  
        dcc.Dropdown(id="slct_country_9",
                    options=sorted(df_9['region'].unique().tolist()), # Defined above
                    multi=False,
                    value=sorted(df_9['region'].unique().tolist())[0],
                    style={'width': "40%"},
                    clearable=False ) ), dbc.Col(
        dcc.Dropdown(id="slct_type_9",
                    options=sorted(ev_types_9), # Defined above
                    multi=False,
                    value='ALL',
                    style={'width': "40%"},
                    clearable=False ) ) ] ),
    dcc.Graph(id="graph_9"),


    html.Br(),
    dcc.Dropdown(id="slct_year_13",
                 options=['ALL', '2021', '2022', '2023'], # Defined above
                 multi=False,
                 value='ALL',
                 style={'width': "40%"},
                 clearable=False ),

    dcc.Graph(id="graph_13"),

    html.Br(),

    dcc.Graph(figure=fig_15, style={'width': '80vw', 
                                    'height': '70vh',
                                    'margin': '0 auto'})
])

@callback(
    Output("graph_5", "figure"),
    Output("graph_9", "figure"),
    Output("graph_13", "figure"), 

    Input("slct_comparison_5", "value"),
    Input("slct_data_5", "value"),

    Input("slct_country_9", "value"),
    Input("slct_type_9", "value"),
    
    Input("slct_year_13", "value"))

def update_line_chart(comp_5, d_var_5, continents_9, d_var_9,  year_13):


    ## --- GRAPH [5] --- ##
    if comp_5 == 'Top Country':
        if d_var_5 == 'Sales':
            comp_5 = 'China'
        else:
            comp_5 = 'Norway'

    df_5 = pd.read_csv('cleaned_data/australia_ev_comp(plotly).csv')
    mask_5 = df_5.region.isin(['Australia', comp_5])
    fig_5 = px.line(df_5[mask_5], 
        x="year", y=d_var_5.split(' ')[-1].lower(), color='region')
    

    ## --- GRAPH [9] --- ##
    df_9 = pd.read_csv('cleaned_data/cnty_type_sales.csv')
    mask_9 = df_9[df_9['region']==continents_9]

    if d_var_9 != 'ALL':
        mask_9 = mask_9[mask_9['powertrain']==d_var_9]

    #make plot
    fig_9 = go.Figure()
    #plots ev data
    fig_9 = px.line(mask_9, 
        x="year", y="sales", color='powertrain')
    


    ## --- GRAPH 3 --- ##
    if year_13 == 'ALL':

        fig_13 = px.scatter(
            merged_pd_df_13,
            x='Mean Income',
            y=['Registrations_2021', 'Registrations_2022', 'Registrations_2023'],
            labels={
                'value': 'Hybrid/PHEV Registrations',
                'Mean Income': 'Mean Income',
                'variable': 'Year'
            },
            title='Hybrid/PHEV Registrations vs Mean Income',
            color_discrete_sequence=px.colors.qualitative.Set1  # Set1 has distinct colors
        )

        # Add trend lines for each year
        add_trendline(fig_13, income_13, registrations_2021_13, '2021', 'blue')
        add_trendline(fig_13, income_13, registrations_2022_13, '2022', 'green')
        add_trendline(fig_13, income_13, registrations_2023_13, '2023', 'orange')
    
    else:
        fig_13 = px.scatter(
            merged_pd_df_13,
            x='Mean Income',
            y='Registrations_'+year_13,
            labels={
                'value': 'Hybrid/PHEV Registrations',
                'Mean Income': 'Mean Income',
                'variable': 'Year'
            },
            title='Hybrid/PHEV Registrations vs Mean Income',
            color_discrete_sequence=px.colors.qualitative.Set1  # Set1 has distinct colors
        )

        if year_13 == '2021':
            reg_13 = registrations_2021_13
        elif year_13 == '2022':
            reg_13 = registrations_2022_13
        else:
            reg_13 = registrations_2023_13
        # Add trend lines for each year
        add_trendline(fig_13, income_13, reg_13, year_13, 'blue')
        

    # Update layout for better visualization
    fig_13.update_layout(
        xaxis_title='Mean Income',
        yaxis_title='Hybrid/PHEV Registrations',
        legend_title='Year',
        hovermode='closest'
    )



    return fig_5, fig_9, fig_13