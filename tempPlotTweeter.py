import sys
import os
import configTemp

from twython import Twython
CONSUMER_KEY  = 'somethingSomething'
CONSUMER_SECRET = 'somethingSomething'
ACCESS_KEY = 'somethingSomething'
ACCESS_SECRET = 'somethingSomething'

api = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)

textMine = 'Recent room temperature and humidity :-)'


photo = open(configTemp.plotPath, 'rb')
api.update_status(media=photo,status=textMine)