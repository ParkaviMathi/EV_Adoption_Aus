import pandas as pd
import plotly.express as px

in_file_path = "cleaned_data/electric_vehicle_energy_consumption_ev_database.csv"
df = pd.read_csv(in_file_path)

df = df.sort_values(by='Consumption (Wh/km)', ascending=True) # Lowest consumption first 
df = df[:10][::-1] # A hacky solution. [::-1] reverses order. In horizontal bar chart i would like best range to be at top.

fig = px.bar(
    df,
    y='Vehicle',
    x='Consumption (Wh/km)',
    orientation='h'
)

fig.show()