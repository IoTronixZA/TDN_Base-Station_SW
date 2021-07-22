# MQTT Publish Demo
# Publish two messages, to two different topics

import paho.mqtt.publish as publish
from random import randint
from time import sleep
import csv
from datetime import datetime

broker = "broker.hivemq.com"
topic = "IoTronix/TakeNoteIT/TestData"


with open('/home/pi/Documents/DummyMQTTCSV.csv') as csv_file:
    CSVdata = [row for row in csv.reader(csv_file)]
    
while 1:    
    index = randint(0,99)        

    timeNow = datetime.now();
    datestr = timeNow.strftime("%Y-%m-%d %H:%M:%S")
        
    JSON = "{"

    JSON += ("\"node_id\":\"")+("FFFF-3830-3235-3830-")+(CSVdata[index][0]) + ("\"")
    JSON += ","

    JSON += ("\"status\":\"")+ ("0") + ("\"")
    JSON += ","

    JSON += ("\"battery\":\"")+ str(randint(80,100)) + ("\"")
    JSON += ","

    JSON += ("\"temperature\":\"")+ str(randint(15,32)) + ("\"")

    JSON += "}"
    
    try:
        publish.single(topic, payload=JSON, port=1883, hostname=broker)
        print(datestr + " Data Published: " + JSON)
        print("")
    except:
        print("Publish Failed")
    sleep(randint(5,30))