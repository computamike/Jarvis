#!/usr/bin/env python
import os
import paho.mqtt.client as mqtt
import time
# Jenkins.azure-devices.net

PRIMARY_KEY='jkszsit8KElkcd4H0uSHcdWNT8LY2T4yHEwgxxnT1vg='
SECONDARY_KEU = 'ilfPjjh4RsETAfpwAwga/DF99lYmmcXo+53qr2nO7PI='
CONNECTION_STRING_PRIMARY_KEY ='HostName=Jenkins.azure-devices.net;SharedAccessKeyName=iothubowner;SharedAccessKey=jkszsit8KElkcd4H0uSHcdWNT8LY2T4yHEwgxxnT1vg='
CONNECTION_STRING_SECONDARY_KEY ='HostName=Jenkins.azure-devices.net;SharedAccessKeyName=iothubowner;SharedAccessKey=ilfPjjh4RsETAfpwAwga/DF99lYmmcXo+53qr2nO7PI='

def on_connect(client, userdata, flags, rc):
    m="Connected flags"+str(flags)+"result code "\
    +str(rc)+"client1_id  "+str(client)
    print(m)

def on_message(client1, userdata, message):
    print("message received  "  ,str(message.payload.decode("utf-8")))

# Main Code :
os.system('clear')
broker_address="Jenkins.azure-devices.net"
broker_port = 8883
client1 = mqtt.Client("MQTTFX")         #create new instance
client1.on_connect= on_connect          #attach function to callback
client1.on_message=on_message           #attach function to callback
time.sleep(1)
client1.username_pw_set("Jenkins.azure-devices.net/MQTTFX","SharedAccessSignature sr=Jenkins.azure-devices.net%2fdevices%2fMQTTFX&sig=v6yJrdvLyB53zOXdr0GHKMioPE7FlHj%2fCB%2fkUbU3IoQ%3d&se=1501798273")
client1.connect(broker_address,8883,60 )      #connect to broker
client1.loop_start()    #start the loop
client1.subscribe("house/bulbs/bulb1")
client1.publish("house/bulbs/bulb1","OFF")
time.sleep(50)
client1.disconnect()
client1.loop_stop()