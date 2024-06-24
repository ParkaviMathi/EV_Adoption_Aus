import pandas as pd
import plotly.express as px

vehicle_registration_file_path = 'cleaned_data/aaa_geographic_vehicle_distribution_lats_longs.csv'
df = pd.read_csv(vehicle_registration_file_path)
df = df[df["Registrations as at 31 January 2023"] > 0] # Remove 0 registered sites

# Specify color:
color_dict = {'ICE': '#3C8DFF', 'BEV': '#FFA500', "Hybrid/PHEV":'#32CD32'}
df['Color'] = df['Fuel Type'].apply(lambda x: color_dict.get(x))



# Plotly Express
fig = px.scatter_mapbox(df,
    lon = "Longitude",
    lat = "Latitude",
    color="Fuel Type",
    color_discrete_map=color_dict,
    hover_data="Fuel Type",
    size=None,
    opacity=0.7,
    zoom = 3,
    title = 'Dash Plotly Test',)


fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0, "t":50, "l":0, "b":10}) # Set margin of plot (right, top, left, bottom)

fig['data'][0]['showlegend']=True

fig.show()