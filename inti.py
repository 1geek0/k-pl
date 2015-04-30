import plotly.plotly as py  
 
# (*) Useful Python/Plotly tools
import plotly.tools as tls   
 
# (*) Graph objects to piece together plots
from plotly.graph_objs import *

stream = Stream(
token='89fmomwu4g',
maxpoints=100
)
TotalIn = Scatter(
x=[],
y=[],
mode='lines+markers',
stream=stream
)
data = Data([TotalIn])
layout = Layout(title='Stream Out Test 3')
fig = Figure(data=data, layout=layout)
unique_url = py.plot(fig, filename='Stream Out Test 3')