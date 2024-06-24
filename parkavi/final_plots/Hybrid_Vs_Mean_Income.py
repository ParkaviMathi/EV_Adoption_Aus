#Import Dependencies
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

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

# Extract relevant columns for plotting
income = merged_pd_df['Mean Income']
registrations_2021 = merged_pd_df['Registrations_2021'].astype(float)
registrations_2022 = merged_pd_df['Registrations_2022'].astype(float)
registrations_2023 = merged_pd_df['Registrations_2023'].astype(float)

# Function to fit and plot a linear regression line
def add_trendline(fig, x, y, name, color):
    # Reshape x for sklearn
    x = np.array(x).reshape(-1, 1)
    # Fit linear regression model
    model = LinearRegression().fit(x, y)
    # Predict y values for trend line
    trend_y = model.predict(x)
    # Add the trend line to the plot
    fig.add_scatter(x=x.flatten(), y=trend_y, mode='lines', name=f'Trend {name}', line=dict(color=color))

# Create a scatter plot with trend lines
fig = px.scatter(
    merged_pd_df,
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
add_trendline(fig, income, registrations_2021, '2021', 'blue')
add_trendline(fig, income, registrations_2022, '2022', 'green')
add_trendline(fig, income, registrations_2023, '2023', 'orange')

# Update layout for better visualization
fig.update_layout(
    xaxis_title='Mean Income',
    yaxis_title='Hybrid/PHEV Registrations',
    legend_title='Year',
    hovermode='closest',
     legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="right",
        x=0.99
    ),
)

# Show the plot
fig.show()