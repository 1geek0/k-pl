import plotly.plotly as py

# (*) Useful Python/Plotly tools
import plotly.tools as tls   
 
# (*) Graph objects to piece together plots
from plotly.graph_objs import *

stream = Stream(
token='qantwq6c5u', #Token Here
maxpoints=1000
)

TotalIn = Scatter(
x=[],
y=[],
mode='lines+markers',
stream=stream,
name = "In Count"
)

TotalOut = Scatter(
x=[],
y=[],
mode='lines+markers',
stream=stream,
name = "Out Count",
yaxis = 'y2'
)

data = Data([TotalIn,TotalOut])
al = "InOut"
layout = Layout(
    title=al,
    yaxis=YAxis(
        title="In"
    ),
    yaxis2=YAxis(
        title = "Out",
        overlaying = 'y',
        side = 'right'
    )
    )
fig = Figure(data=data, layout=layout)
unique_url = py.plot(fig, filename=al)