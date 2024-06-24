#Import Dependencies
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

# Read in Fuel_Vs_Electricit CSV

EV_Reg_by_Fuel_Type = "F:/FDM/FDMDataEngGrpProject/cleaned_data/Population_Income_Registration.csv"

merged_pd_df = pd.read_csv(EV_Reg_by_Fuel_Type)

# Convert relevant columns to numeric types
numeric_columns = [
    'Population in 2021', 'Population in 2022', 'Population in 2023',
    'Median Age of Earners', 'Registrations_2021', 'Registrations_2022', 'Registrations_2023'
]

for column in numeric_columns:
    merged_pd_df[column] = pd.to_numeric(merged_pd_df[column], errors='coerce')

# Ensure there are no null values after conversion (this step can be skipped if data is clean)
merged_pd_df.dropna(subset=numeric_columns, inplace=True)

# Ensure data types are appropriate for aggregation
merged_pd_df['Registrations_2021'] = merged_pd_df['Registrations_2021'].astype(float)
merged_pd_df['Registrations_2022'] = merged_pd_df['Registrations_2022'].astype(float)
merged_pd_df['Registrations_2023'] = merged_pd_df['Registrations_2023'].astype(float)

# Aggregate the registration data by Fuel Type and Year
agg_data = merged_pd_df.groupby('Fuel Type').agg({
    'Registrations_2021': 'sum',
    'Registrations_2022': 'sum',
    'Registrations_2023': 'sum'
}).reset_index()

# Melt the data to long format for easier plotting with Plotly
melted_data = pd.melt(agg_data, id_vars='Fuel Type', 
                      value_vars=['Registrations_2021', 'Registrations_2022', 'Registrations_2023'],
                      var_name='Year', value_name='Registrations')

# Convert year format from 'Registrations_2021' to '2021' for better readability
melted_data['Year'] = melted_data['Year'].str.extract('(\d+)')

# Create a grouped bar chart
fig = px.bar(melted_data, 
             x='Year', 
             y='Registrations', 
             color='Fuel Type', 
             barmode='group',
             title='Electric Vehicle Registrations by Fuel Type and Year',
             labels={'Year': 'Year', 'Registrations': 'Total Registrations'},
             category_orders={'Year': ['2021', '2022', '2023']})

# Define the layout with legend position
fig.update_layout(
    legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.01
    )
)

# Show the plot
fig.show()
