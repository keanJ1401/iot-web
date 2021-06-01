import paho.mqtt.client as mqtt
from datetime import datetime


devices = [(1, '8F0F', 'Living Room'), (2, '8F0F', 'Living Room')]
topic = "#"
broker = "192.168.0.104"
port = 1883


def on_connect(mqttc, obj, flags, rc):
    print(f"Connected to Broker: {broker}:{port}")


def on_message(mqttc, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))


def on_publish(mqttc, obj, mid):
    print("mid: " + str(mid))


def on_subscribe(mqttc, obj, mid, granted_qos):
    print(f"Subscribed successes topic '{topic}, qos: {granted_qos}")


def on_log(mqttc, obj, level, string):
    print(string)


mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe
# Uncomment to enable debug messages
# mqttc.on_log = on_log
try:
    mqttc.connect(broker, port, 1)
except:
    print(f"Timed out, something wrong when connect to Broker {broker}:{port}")
mqttc.subscribe(topic, 0)
mqttc.loop_forever()
