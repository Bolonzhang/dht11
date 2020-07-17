import Adafruit_DHT
import time
import csv

sensor=Adafruit_DHT.DHT11

gpio=4

humi, temp = Adafruit_DHT.read_retry(sensor,gpio)
# if humidity is not None and temperature is not None:
#     record=('Temperature={0:0.1f}*C,Humidity={1:0.1f}%'.format(temperature,humidity))
# else:
#     record=('Failed to get reading. Try again!')
with open('/home/pi/Desktop/dht11_record.csv','a',encoding='utf-8') as file:
    date=time.strftime("%Y/%m/%d")
    etime=time.strftime("%H:%M:%S")
    writer=csv.writer(file)
    writer.writerow([date,etime,temp,humi])