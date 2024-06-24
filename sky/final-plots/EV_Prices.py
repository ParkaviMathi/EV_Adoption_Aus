import plotly.express as px
import pandas as pd

df = pd.read_csv("F:/FDM/FDMDataEngGrpProject/cleaned_data/cleaned_ev_prices_comparison.csv")

# Melt the DataFrame to make it suitable for seaborn
df_melted = df.melt(id_vars='Model', var_name='Country', value_name='Price')

# Melt the DataFrame to make it suitable for seaborn
df_melted = df.melt(id_vars='Model', var_name='Country', value_name='Price')

# Create the Plotly bar plot using Plotly Express
fig = px.bar(
    df_melted,
    x='Model',
    y='Price',
    color='Country',
    title='Price Comparison of Car Models by Country',
    labels={'Model': 'EV Model', 'Price': 'Price (Australian Dollar)'},
    barmode='group'
)

# Update layout for better readability
fig.update_layout(
    xaxis_title='EV Model',
    yaxis_title='Price (Australian Dollar)',
    legend_title='Country',
    bargap=0.15,
    bargroupgap=0.1,
    legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="right",
        x=0.99
    )
)

# Show the plot
fig.show()