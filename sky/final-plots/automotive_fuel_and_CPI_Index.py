#Import dependencies
import pandas as pd
import plotly.express as px

#Read the CSV file
data = pd.read_csv("F:\FDM\FDMDataEngGrpProject\cleaned_data\cleaned_automotive_fuel_and_CPI_Index.csv")

# Convert the Year column to string if necessary
data['Year'] = data['Year'].astype(str)

# Melt the DataFrame to long format
data_melted = data.melt(id_vars='Year', var_name='Index Type', value_name='Value')

# Create the Plotly line plot
fig = px.line(
    data_melted,
    x='Year',
    y='Value',
    color='Index Type',
    title='Automotive Fuel and CPI Index Number, 1972 = 100.0'
)

# Update layout for better readability
fig.update_layout(
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

# Show the plot
fig.show()