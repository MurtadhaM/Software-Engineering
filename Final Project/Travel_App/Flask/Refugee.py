
# Author: Murtadha Marzouq
# Assignment: Refugees
# Date: 11/9/2020
# 
# 
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Read in the data
df = pd.read_csv('Refugees.csv')
# print(df.head())
df['Year'] = pd.to_datetime(df['Year'], format = '%Y') # %Y filters only the year
df = df[(df['Year'] == "2020")]
df = df[(df['Population Type'] == "REF")]
# trace = go.Scatter(x = df['Year'], y = df['Refugees'])
trace3 = go.Scatter(x=df['Country of Origin Code'], y=df['Total'], mode='markers+lines', name='Total')
data = [ trace3]
# data = [trace]
layout = go.Layout(title='Population of Refugees and Asylum Seekers in the United States', xaxis_title="Country of Origin",
                   yaxis_title="Total population")
fig = go.Figure(data=data, layout=layout)
# show plot 
pyo.plot(fig, filename='static/Refugees.html')
