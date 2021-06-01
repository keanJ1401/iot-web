import paho.mqtt.client as mqtt

config = {
    "topic": "#",
    "broker": "192.168.0.101",
    "port": 1883,
    "keepalive": 60,
}
actuator_topic = [
        "home/light1",
        "home/light2",
        "home/door/control",
        "home/door/mode",
        "home/mq2/buzzer"
    ],


def on_connect(mqttc, obj, flags, rc):
    print(f"Connected to Broker: {config['broker'],}:{config['port'],}")
    mqttc.subscribe(topic=config['topic'], qos=0)


def on_message(mqttc, obj, msg):
    pass # Because, we using data on database


def on_publish(mqttc, obj, mid):
    pass


def on_subscribe(mqttc, obj, mid, granted_qos):
    print(f"Subscribed successes topic '{config['topic']}', qos: {granted_qos}")


def on_log(mqttc, obj, level, string):
    print(string)





def connect_init():
    mqttc = mqtt.Client()
    mqttc.on_message = on_message
    mqttc.on_connect = on_connect
    mqttc.on_publish = on_publish
    mqttc.on_subscribe = on_subscribe
    try:
        mqttc.connect(host=config["broker"], port=config["port"], keepalive=config["keepalive"])
    except:
        print(f"Timed out, something wrong when connect to Broker {config['broker']}:{config['port']}")
    # mqttc.loop_forever()
    return mqttc