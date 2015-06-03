

#this read and plot data from actual storage

import pylab
import modTemp
import os.path
import configTemp
from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA
import matplotlib.pyplot as plt
import pylab
import dateutil
import time

#concName = modTemp.nameCreator()
#assert os.path.isfile(concName)
#modTemp.updateData()
timeSamples = ['02:10:20','03:10:22','05:10:24','11:10:26','12:10:28','14:10:30']
tempSamples = [37.5,38.5,13.5,77.5,10.5,46.5]
humSamples = [35.9,340.7,95.7,10.1,21.5,0.00]


if 1:
    
    host = host_subplot(111, axes_class=AA.Axes)
    modTemp.updateDate()
 
    pylab.title('Temperature and Humidity'+ '\n'+ 'plotted @ ' + configTemp.dateToday)
    
    secondAxis = host.twinx()
    
    #time data and parsing
    datestrings = timeSamples
    dates = [dateutil.parser.parse(s) for s in datestrings]

    ax=host
    #the following line helps avoiding overlapping on x axis
    ax.set_xticks([dates[0],dates[2],dates[-1]])
    timeSamples = pylab.DateFormatter('%H:%M:%S')  
    ax.xaxis.set_major_formatter(timeSamples)
    
    

    #set the length of the host axes
    # it would be nice to use 0-6, 0-12, 0-18 and 0-24 for the x axis length
    #the length of x axis can be given like this --> host.set_xlim(dates[0], dates[2])
    #if int(time.strftime("%H")) < 6:
    #    host.set_xlim('00:00:00', '06:00:00')
    #elif int(time.strftime("%H")) > 6 and int(time.strftime("%H")) < 12:
    #    host.set_xlim('00:00:00', '12:00:00')
    #elif int(time.strftime("%H")) > 12 and int(time.strftime("%H")) < 18:
    #    host.set_xlim('00:00:00', '18:00:00')
    #elif int(time.strftime("%H")) > 18 and int(time.strftime("%H")) < 24:
    #    host.set_xlim('00:00:00', '23:59:59')
    
    #the length of y axis on the left
    host.set_ylim(0, 100)
    
    #labels 
    host.set_xlabel("Time")
    host.set_ylabel("Temperature")
    secondAxis.set_ylabel("Relative Humidity")

    #here X and Y axis data should be inserted and they must match in length
    p1, = host.plot(dates, tempSamples, color = 'magenta', 
    	label="Temperature")
    p2, = secondAxis.plot(dates, humSamples, color = 'green',
    	label="Relative Humidity")
    
    #set the length of the second axis
    secondAxis.set_ylim(0, 100)    

    #make a legend for the axes
    host.legend()
    host.axis["left"].label.set_color(p1.get_color())
    secondAxis.axis["right"].label.set_color(p2.get_color())

    #last bit
    plt.draw()
    plt.show()
    #plt.savefig(configTemp.dateToday + ' ' + configTemp.timeNow)
