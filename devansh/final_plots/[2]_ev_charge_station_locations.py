import pandas as pd
import plotly.express as px


in_path = "cleaned_data/ev_charge_stations_australia.csv"
df = pd.read_csv(in_path)

# Plotly Express
fig = px.scatter_mapbox(df,
    lon = "Longitude",
    lat = "Latitude",
    color_discrete_sequence=["#FF0000"], # Bright red colour for the ev charge stations
    size=None,
    opacity=0.7,
    zoom = 3,
    title = 'Dash Plotly Test',)


fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0, "t":50, "l":0, "b":10}) # Set margin of plot (right, top, left, bottom)


fig.show()