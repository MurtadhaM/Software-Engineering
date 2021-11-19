import pandasas pd
import plotly.offline as pyo
import plotly as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/CoronaTimeSeries.csv')
df['Date'] = pd.to_datetime(df['Date'])

# Preparing data
# With px.scatter, each data point is represented as a marker point, whose location is given by the x and y columns.
data = [go.Scatter(x=df['Date'], y=df['Confirmed'], mode='lines', name='Death')]

# Preparing layout
layout = go.Layout(title='Corona Virus Confirmed Cases From 2020-01-22 to 2020-03-17', xaxis_title="Date",
                   yaxis_title="Number of cases")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='static/line.html')
