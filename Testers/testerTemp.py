
from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA
import matplotlib.pyplot as plt
import pylab
import dateutil

with open('configTemp.py') as f:
    lines = list(f)
print lines

a = open('configTemp.py', 'r')
lines = list(a)
a.close()
print a


if 1:
    
    host = host_subplot(111, axes_class=AA.Axes)
    #plt.subplots_adjust(right=0.75)
    pylab.title('Temperature and Humidity data')
    par1 = host.twinx()
    #par2 = host.twinx()

    #offset = 60
    #new_fixed_axis = par2.get_grid_helper().new_fixed_axis
    #par2.axis["right"] = new_fixed_axis(loc="right",
                                        #axes=par2,
                                        #offset=(offset, 0))

    #par2.axis["right"].toggle(all=True)


    
    datestrings = ['00:00:00','16:50:46','23:59:59']
    dates = [dateutil.parser.parse(s) for s in datestrings]    
    
    host.set_xlim(dates[0],dates[2])
    host.set_ylim(0, 10)

    host.set_xlabel("Distance")
    host.set_ylabel("Density")
    par1.set_ylabel("Temperature")
    #par2.set_ylabel("Velocity")
    
    
        
    
    
    p1, = host.plot(dates, [0, 5, 9], color = 'blue',label="Density")
    p2, = par1.plot(dates, [2, 4, 1], color = 'green',label="Temperature")
    #p3, = par2.plot([0, 1, 2], [50, 30, 15], label="Velocity")

    par1.set_ylim(0, 4)
    #par2.set_ylim(1, 65)
    
    ax=host
    ax.set_xticks(dates)
    timeSamples = pylab.DateFormatter('%H:%M:%S')  
    ax.xaxis.set_major_formatter(timeSamples)
    

    host.legend()
    host.axis["left"].label.set_color(p1.get_color())
    par1.axis["right"].label.set_color(p2.get_color())
    #par2.axis["right"].label.set_color(p3.get_color())

    plt.draw()
    plt.show()
    plt.savefig("DavidDoubleAxis.jpg")
    
    a = open('configTemp.py', 'r')
    lines = list(a)
    a.close()
    print a