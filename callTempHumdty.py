import Adafruit_DHT as dht
import tempLibrary
import modTemp

modTemp. updateTime()
h, t = dht.read_retry(dht.DHT22, 4)
tempLibrary.tempLibrary(t,h)