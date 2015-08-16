from __future__ import print_function
import csv
import mmap
import plotly.plotly as py
from plotly.graph_objs import *
from datetime import datetime
import plotly.tools as tls
from boto.dynamodb2.table import *;

#DynamoDB initialization
dbTable = Table('test_gate1')
dbQuery = dbTable.query_2(Plotted__eq=0,index='Plotted-n-index')
#dbScan = dbTable.scan(Plotted__eq=0)
r = 1
for res in dbQuery:
    #Get Item
    t = str(r)
    pl = res['uuid']
    plotted = dbTable.get_item(uuid=pl)
    print(str(plotted['In']) + str(plotted['Plotted']))
    r += 1
    #Resources
    inInt = int(res['In'])
    #Time
    yearInt = int(res['Year'])
    monthInt = int(res['Month'])
    dateInt = int(res['Date'])
    hourInt = int(res['Hour'])
    minuteInt = int(res['Minute'])
    secondInt = int(res['Second'])
    td = datetime(year=yearInt, month=monthInt, day=dateInt, hour=hourInt, minute=minuteInt, second=secondInt)
    #Time Ends
    if res['Plotted'] != 1:
        #Plotting
       # print("New Plot")
        inStream = py.Stream('oij5ld5l72')
        inStream.open()
        inStream.write(dict(x=td, y=inInt))
        inStream.close()
        plotted['Plotted'] = 1
        plotted.save()
    #else:
      #  print("Already Plotted")


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

