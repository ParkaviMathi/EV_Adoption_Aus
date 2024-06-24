# Import Dependencies
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from plotly.subplots import make_subplots
import matplotlib.cm as cm
import matplotlib.colors as mcolors

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

# Filter data for each fuel type
hybrid_df = merged_pd_df[merged_pd_df['Fuel Type'] == 'Hybrid/PHEV']
bev_df = merged_pd_df[merged_pd_df['Fuel Type'] == 'BEV']
hfcev_df = merged_pd_df[merged_pd_df['Fuel Type'] == 'HFCEV']

# Function to normalize data by population
def normalize_by_population(df, year):
    return df[f'Registrations_{year}'].astype(float) / df[f'Population in {year}'].astype(float)

# Color map for different fuel types
fuel_type_colors = {
    'Hybrid/PHEV': 'blue',
    'BEV': 'green',
    'HFCEV': 'orange'
}

# Create traces for each fuel type and each year
traces = []

for fuel_type, df in [('Hybrid/PHEV', hybrid_df), ('BEV', bev_df), ('HFCEV', hfcev_df)]:
    for year in [2021, 2022, 2023]:
        if not df.empty:  # Check if the DataFrame is not empty
            # Normalize registration data by population
            normalized_registrations = normalize_by_population(df, year)
            
            # Use a colormap for visual differentiation
            norm = mcolors.Normalize(vmin=normalized_registrations.min(), vmax=normalized_registrations.max())
            cmap = cm.viridis
            colors_mapped = [mcolors.rgb2hex(cmap(norm(value))) for value in normalized_registrations]
            
            trace = go.Scattermapbox(
                lat=df['Lat_precise'],
                lon=df['Long_precise'],
                mode='markers',
                marker=dict(
                    size=10,
                    opacity=0.7,
                    color=colors_mapped,
                    colorscale='Viridis',
                    showscale=True,
                    colorbar=dict(title=f'Normalized Registrations {year}')
                ),
                name=f'{fuel_type} {year}',
                hoverinfo='text',
                text=df['Local Government Area'] + '<br>' +
                     f'Population {year}: ' + df[f'Population in {year}'].astype(str) + '<br>' +
                     f'Registrations {year}: ' + df[f'Registrations_{year}'].astype(str)
            )
            traces.append(trace)

# Create the Plotly figure
fig = make_subplots(rows=1, cols=1)

# Add all traces to the figure
for trace in traces:
    fig.add_trace(trace)

# Define the layout with legend position
fig.update_layout(
    title='Effect of Income and Population on Electric Vehicle Registrations (2021-2023)',
    mapbox=dict(
        style='open-street-map',
        center=dict(
            lat=merged_pd_df['Lat_precise'].mean(),
            lon=merged_pd_df['Long_precise'].mean()
        ),
        zoom=4
    ),
    legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.01
    ),
    legend_title="Fuel Type and Year"
)

# Show the plot
fig.show()
