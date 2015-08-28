import plotly.plotly as py

#    (*) Useful Python/Plotly tools
import plotly.tools as tls   
 
# (*) Graph objects to piece together plots
from plotly.graph_objs import *

stream = Stream(
token='cpgedgpn9v', #Token Here
maxpoints=1000
)
lineL = Line(
    color = 'rgb(67,160,71)',
    smoothing = 2,
    width = 3
)
lineO = Line(
    color = 'rgb(67,160,71)',
    smoothing = 2,
    width = 3
)
TotalIn = Scatter(
x=[],
y=[],
marker = Marker(
    color = 'rgb(244,67,54)',
    size = 5,
    symbol = 'dot'
),
mode='lines+markers+text',
stream=stream,
name = "Out Count",
text = "Out Count",
line = lineL
)
TotalOut = Scatter(
x=[],
y=[],
marker = Marker(
    color = 'rgb(244,67,54)',
    size = 5,
    symbol = 'dot'
),
mode='lines+markers+text',
stream=stream,
name = "Out Count",
text = "Out Count",
line = lineO
)
legendOut = Legend(
    bgcolor = 'rgb(0,191,165)',
    bordercolor = 'black'
)
data = Data([TotalIn])  
al = "Talkuteshwar Mandir Road"
layout = Layout(title=al,
                legend = legendOut,
                showlegend = True,
                hovermode = 'closest',
                dragmode = 'zoom')
fig = Figure(data=data, layout=layout)
unique_url = py.plot(fig, filename=al)