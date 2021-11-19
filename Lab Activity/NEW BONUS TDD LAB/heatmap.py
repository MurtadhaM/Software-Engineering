import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# Load CSV file from Datasets folder
df = pd.read_csv('Datasets/CoronaTimeSeries.csv')

# Preparing data
# The data is being broken up into a matrix and assigned a color value
data = [go.Heatmap(x=df['Day'],
                   y=df['WeekofMonth'],
                   z=df['Recovered'].values.tolist(),
                   colorscale='Jet')]

# Preparing layout
layout = go.Layout(title='Cats killed Per Month', xaxis_title="Cats",
                   yaxis_title="Mortality Rate")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='static/heatmap.html')