import plotly.plotly as py  
 
# (*) Useful Python/Plotly tools
import plotly.tools as tls   
 
# (*) Graph objects to piece together plots
from plotly.graph_objs import *

stream = Stream(
token='l1plr75pg4', #Token Here
maxpoints=100
)
TotalIn = Scatter(
x=[],
y=[],
mode='lines+markers',
stream=stream
)
data = Data([TotalIn])
al = "15 Aug"
layout = Layout(title=al)
fig = Figure(data=data, layout=layout)
unique_url = py.plot(fig, filename=al)