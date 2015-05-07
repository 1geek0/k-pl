import plotly.plotly as py  
 
# (*) Useful Python/Plotly tools
import plotly.tools as tls   
 
# (*) Graph objects to piece together plots
from plotly.graph_objs import *

stream = Stream(
token='vts52yaho1',
maxpoints=100
)
TotalIn = Scatter(
x=[],
y=[],
mode='lines+markers',
stream=stream
)
data = Data([TotalIn])
layout = Layout(title="Collector's Office 05-05-15")
fig = Figure(data=data, layout=layout)
unique_url = py.plot(fig, filename="Collector's Office 05-05-15")