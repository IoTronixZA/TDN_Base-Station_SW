# MQTT Publish Demo
# Publish two messages, to two different topics

import paho.mqtt.publish as publish
from time import sleep
import serial
from datetime import datetime

broker = "broker.hivemq.com"
topic = "IoTronix/TakeNoteIT/TestData"

ser = serial.Serial("/dev/serial0", 115200, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)
ser.flushInput()
    
while True:    
    s = ser.read()
    sleep(0.03)
    data_left = ser.inWaiting()
    s += ser.read(data_left)
    s = s.strip()
    s = s.decode("utf-8")
    data = s.split(", ")
        
    JSON = "{"

    JSON += ("\"node_id\":\"")+(data[0]) + ("\"")
    JSON += ","

    JSON += ("\"status\":\"")+ (data[1]) + ("\"")
    JSON += ","

    JSON += ("\"battery\":\"")+ (data[2]) + ("\"")
    JSON += ","

    JSON += ("\"temperature\":\"")+ (data[3]) + ("\"")

    JSON += "}"

    try:
        timeNow = datetime.now();
        datestr = timeNow.strftime("%Y-%m-%d %H:%M:%S")
    
        publish.single(topic, payload=JSON, port=1883, hostname=broker)
        print(datestr + " Data Published: "+ JSON)
        print("")
    except:
        print("ERROR: Publish Failed!")