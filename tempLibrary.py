#save data in new file every day

import modTemp
import os.path
import configTemp
import csv
import time
import datetime

def writeLine(temp,humdty,concName):
    """
    Append data to the file.
    """
    tempDataStorage = open(concName, 'ab')
    toFile = csv.writer(tempDataStorage)
    toFile.writerow([configTemp.timeNow,temp,humdty])
    tempDataStorage.close()

def tempLibrary(temp,humdty):
    """
    Create file into a chosen folder.

    Example for filePath format:
    'C:/Users/David/Documents/Personal files/Code/Python file'
    """
 
    concName = modTemp.nameCreator()
    
    if os.path.isfile(concName):
        writeLine(temp,humdty,concName)
   

    else:
        modTemp.updateDate()
        print configTemp.dateToday
        tempDataStorage = open(concName, 'w')
        tempDataStorage.write('DATE:' + ' ' + configTemp.dateToday + '\n')

        toFile = csv.writer(tempDataStorage)
        toFile.writerow(['Time','Temperature [degree C]','Relative humidity [%]'])
        tempDataStorage.close()
        writeLine(temp,humdty,concName)

