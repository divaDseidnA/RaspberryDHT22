#this read and plot data from actual storage

import pylab
import modTemp
import os.path
import configTemp
from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA
import matplotlib.pyplot as plt
import dateutil
import time

concName = modTemp.nameCreator()
assert os.path.isfile(concName)
modTemp.updateData()

if 1:

    host = host_subplot(111, axes_class=AA.Axes)
    modTemp.updateDate()
 
    plt.title('Temperature and Humidity data'+ '\n'+ 'plotted @ ' + configTemp.dateToday)
    
    secondAxis = host.twinx()
    
    #time data and parsing
    datestrings = configTemp.timeData
    dates = [dateutil.parser.parse(s) for s in datestrings]
    
    timeSamples = pylab.DateFormatter('%H:%M:%S')
    #make the axis format to match with the time inputs
    ax=host
    
    #the following line helps avoiding overlapping on x axis
    setOfTicks = ['00:00:00','00:30:00','01:00:00','01:30:00','02:00:00','02:30:00',
    '03:00:00','03:30:00','04:00:00','04:30:00','05:00:00','05:30:00','06:00:00',
    '06:30:00','07:00:00','07:30:00','08:00:00','08:30:00','09:00:00','09:30:00',
    '10:00:00','10:30:00','11:00:00','11:30:00','12:00:00','12:30:00','13:00:00',
    '13:30:00','14:00:00','14:30:00','15:00:00','15:30:00','16:00:00','16:30:00',
    '17:00:00','17:30:00','18:00:00','18:30:00','19:00:00','19:30:00','20:00:00',
    '20:30:00','21:00:00','21:30:00','22:00:00','22:30:00','23:00:00','23:59:59']

    ticks = [dateutil.parser.parse(s) for s in setOfTicks]
    if int(time.strftime("%H")) < 6:
        ax.set_xticks(ticks[:13])
    elif int(time.strftime("%H")) > 6 and int(time.strftime("%H")) < 12:
        ax.set_xticks(ticks[:26])
    elif int(time.strftime("%H")) > 12 and int(time.strftime("%H")) < 18:
        ax.set_xticks(ticks[:39])
    elif int(time.strftime("%H")) > 18 and int(time.strftime("%H")) < 24:
        ax.set_xticks(ticks[:46])

    #AXISARTIST namespace explains these lines
    ax.axis["bottom"].major_ticklabels.set_rotation(90)
    #places the labels further from the axis
    ax.axis["bottom"].major_ticklabels.set_pad(20)
    ax.axis["bottom"].label.set_pad(30)
    ax.xaxis.set_major_formatter(timeSamples)

    

    #set the length of the host axes
    #it would be nice to use 0-6, 0-12, 0-18 and 0-24 for the x axis length
    #the length of x axis can be given like this --> host.set_xlim(dates[0], dates[2])
##    if int(time.strftime("%H")) < 6:
##        host.set_xlim('00:00:00', '06:00:00')
##    elif int(time.strftime("%H")) > 6 and int(time.strftime("%H")) < 12:
##        host.set_xlim('00:00:00', '12:00:00')
##    elif int(time.strftime("%H")) > 12 and int(time.strftime("%H")) < 18:
##        host.set_xlim('00:00:00', '18:00:00')
##    elif int(time.strftime("%H")) > 18 and int(time.strftime("%H")) < 24:
##        host.set_xlim('00:00:00', '23:59:59')
    
    #the length of y axis on the left
    host.set_ylim(10, 30)
    
    #labels 
    host.set_xlabel("Time")
    host.set_ylabel("Temperature")
    secondAxis.set_ylabel("Relative Humidity")
    
    #here X and Y axis data should be inserted and they must match in length
    p1, = host.plot(dates, configTemp.tempData, color = 'magenta', 
    	label="Temperature")
    p2, = secondAxis.plot(dates, configTemp.humidityData, color = 'green',
    	label="Relative Humidity")
    
    #set the length of the second axis
    secondAxis.set_ylim(0, 100)    

    #make a legend for the axes
    host.legend()

    #name of the two vertical axes
    host.axis["left"].label.set_color(p1.get_color())
    secondAxis.axis["right"].label.set_color(p2.get_color())

    #last bit
    plt.draw()
    
    #plt.savefig("nahove.jpg")
    figName = str(time.strftime('%y-%m-%d-%H-%M-%S')) + '.jpeg'
    #plt.savefig(figName, dpi=300, bbox_inches='tight')
    plt.savefig(figName,dpi=300, bbox_inches='tight', pad_inches=0.2)
    #update and store the path to current picture of the plot
    modTemp.updatePlotPath(figName)
    plt.show()
