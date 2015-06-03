import configTemp
import math
import time
import datetime
import os.path

def nameCreator():
	#creating name
    dateName = str(datetime.date.today())
    
    #concatinating name
    concName = os.path.join(configTemp.filePath, dateName + '.csv')
    #print concName
    return concName

def updateTime():
    configTemp.timeNow = time.strftime("%H:%M:%S")

def updateDate():
    configTemp.dateToday = str(time.strftime("%a, %d %b %Y %X +0000"))

def updateData():
    concName = nameCreator()
    with open(concName) as f:
        lines = list(f)
    
    #print lines
    
    #slice the lines in such a way that data points can be extracted
    measuredTimes = []
    measuredTemps = []
    measuredHmdty = []

    for e in lines:
        if len(e) > 2:
            #print e[0]
            if e[0] != 'D' and e[0] != 'T':
                #print e
                measuredTimes.append(str(e[0:8]))
                #this line splits the element into a list at character ','
                var = (e[9:-1]).rsplit(',', 1)
                measuredTemps.append(float(var[0]))
                measuredHmdty.append(float(var[1]))

    configTemp.timeData = measuredTimes
    configTemp.tempData = measuredTemps
    configTemp.humidityData = measuredHmdty

    #print measuredTimes
    #print measuredTemps
    #print measuredHmdty

def updatePlotPath(fig):
    #concatinating name
    configTemp.plotPath = os.path.join(configTemp.pictureStore, fig)