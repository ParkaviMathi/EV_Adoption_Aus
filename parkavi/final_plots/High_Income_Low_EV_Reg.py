#Import Dependencies
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

# Read in CSV file

File_Path = "F:/FDM/FDMDataEngGrpProject/cleaned_data/Population_Income_Registration.csv"
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


# Define criteria for high income and low registrations
# These thresholds can be adjusted based on your analysis
high_income_threshold = merged_pd_df['Mean Income'].quantile(0.75)  # Top 25% for high income
low_registration_threshold = merged_pd_df['Registrations_2023'].quantile(0.25)  # Bottom 25% for low registrations

# Filter data based on the criteria
high_income_low_registration_df = merged_pd_df[
    (merged_pd_df['Mean Income'] > high_income_threshold) &
    (merged_pd_df['Registrations_2023'] < low_registration_threshold)
]

# Create a scatter mapbox plot using Plotly
fig = go.Figure()

# Add filtered data as a scatter plot
fig.add_trace(go.Scattermapbox(
    lat=high_income_low_registration_df['Lat_precise'],
    lon=high_income_low_registration_df['Long_precise'],
    mode='markers',
    marker=go.scattermapbox.Marker(
        size=10,
        color='purple',  # Color for high income, low registration points
        opacity=0.7
    ),
    text=high_income_low_registration_df['Local Government Area'] + '<br>' +
         'Income: ' + high_income_low_registration_df['Mean Income'].astype(str) + '<br>' +
         'Registrations: ' + high_income_low_registration_df['Registrations_2023'].astype(str),
    hoverinfo='text'
))

# Update the layout to use an OpenStreetMap tile
fig.update_layout(
    mapbox=dict(
        style='open-street-map',
        zoom=4,  # Adjust zoom level based on the density of points
        center=dict(lat=-25.2744, lon=133.7751)  # Center on Australia
    ),
    legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.01
    ),
    title='High Income, Low EV Registrations in Australia',
    autosize=True,
    height=600
)

# Show the map
fig.show()

