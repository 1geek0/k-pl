from __future__ import print_function
import csv
import time
import mmap
import plotly.plotly as py
from plotly.graph_objs import *
from datetime import datetime
import plotly.tools as tls
from boto.dynamodb2.table import *;

#DynamoDB initialization
dbTable = Table('ashioto1')
dbQuery = dbTable.query_2(plotted__eq=0,index='plotted-index')
plots = []
#dbScan = dbTable.scan(Plotted__eq=0)
for res in dbQuery:
    #Get Item
    pl = res['timestamp']
    plotted = dbTable.get_item(timestamp=pl)
    print(str(plotted['outcount']) + str(plotted['plotted']))
    #Resources
    outInt = int(res['outcount'])
    #Time
    timestamp = res['timestamp']
    td = datetime.strptime(timestamp, "%Y/%m/%d %H:%M:%S")
    
    #Time Ends
    if res['plotted'] != 1:
        #Plotting
       # print("New Plot")
       plots.append(res)
       plots.sort()
    #else:
      #  print("Already Plotted")
plots.sort()
for plotPoint in plots:
    inStream = py.Stream('qantwq6c5u')
    inStream.open()
    inStream.write(dict(x=td, y=outInt))
    inStream.close()
    plotted['plotted'] = 1
    plotted.save()

dsbfddfbdb = '''dataFile = open('/home/geek/k-pl/data.csv', 'a+')
doneFile = open('/home/geek/k-pl/done.log', 'a+')

m = mmap.mmap(doneFile.fileno(), 0, access=mmap.ACCESS_READ)

dataR = csv.DictReader(dataFile)

tInList = []
tdList = []
for row in dataR:

    if m.find(str(row)) != -1:
        n = 1
    else:
        inInt = int(row['in'])
        outInt = int(row['out'])
        monthInt = int(row['month'])
        dateInt = int(row['date'])
        hourInt = int(row['hour'])
        minuteInt = int(row['minute'])
        secondInt = int(row['second'])
        td = datetime(year=2015, month=monthInt, day=dateInt, hour=hourInt, minute=minuteInt, second=secondInt)
        tInList.append(inInt)
        tdList.append(td)
        print("New Plot")
        #Plotting the Total In Count *1
        inStream = py.Stream('vts52yaho1')
        inStream.open()
        inStream.write(dict(x=td, y=inInt))
        inStream.close()
        #End of *1
        #Plotting the Total Out Count
#        outStream = py.Stream('nhzfl55ut2')
#        outStream.open()
#        outStream.write(dict(x=td, y=outInt))
#        outStream.close()
        print(row, file = doneFile)
      
#stream = Stream(
#    token='9bfuux3mfq',
#    maxpoints=50
#)
#TotalIn = Scatter(
#x=tdList,
#y=tInList,
#x=[],
#y=[],
#mode="lines+markers",
#stream=stream
#)
#data = Data([TotalIn])
#layout = Layout(title='Stream In Test 2')
#fig = Figure(data=data, layout=layout)
#unique_url = py.plot(fig, filename='Stream In Test 2')
'''

