import pandas as pd
import plotly.express as px

in_file_path = "cleaned_data/electric_vehicle_ranges_ev_database.csv"
df = pd.read_csv(in_file_path)

df = df.sort_values(by='Range (km)', ascending=False) 
df = df[:10][::-1] # A hacky solution. [::-1] reverses order. In horizontal bar chart i would like best range to be at top.

fig = px.bar(
    df,
    y='Vehicle',
    x='Range (km)',
    orientation='h'
)

fig.show()

#### dash app solution ######

# Solution from: https://community.plotly.com/t/is-it-possible-to-add-vertical-scroll-bar-to-a-horizontal-bar-chart/73278/5

# import dash
# import plotly.graph_objects as go
# from dash import html, dcc
# import numpy as np

# # create data, lots of bars
# data = np.arange(200)

# # app and layout
# app = dash.Dash(__name__)
# app.layout = html.Div(
#     [
#         html.Div(
#             dcc.Graph(
#                 figure=go.Figure(
#                     data=go.Bar(
#                         y=data,
#                         orientation='h'
#                     ),
#                     layout={'height': 10000}
#                     # ^^ adapt the height to your needs so that the bars
#                     #    show the desired thickness
#                 )
#             ),
#             className='scroll'
#             # ^^ custom css in the assets folder
#         )
#     ],
# )

### Custom css: ####
# .scroll
# {
# width:80%;
# height:400px;
# overflow:scroll;
# float: left;
# }

# if __name__ == '__main__':
#     app.run(debug=True)