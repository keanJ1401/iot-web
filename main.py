from flask import Flask, render_template, make_response, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
import paho.mqtt.client as mqtt
from models.sql_alchemy_subsclass import Home, Devices, Sensors, Actuators
from datetime import datetime


app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_MAX_OVERFLOW'] = 20
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:user@35.221.141.147/database'

db = SQLAlchemy(app)


def on_connect(client, userdata, flags, rc):
    global FLAG_CONNECTED
    if rc == 0:
        FLAG_CONNECTED = 1
        print("Connected to MQTT Broker! with return code: {rc}".format(rc=rc))
    else:
        print("Failed to connect, with return code {rc}".format(rc=rc))


def on_publish(client, userdata, mid):
    pass


@app.route('/')
def root():
    current_state = Actuators.get_last_state()
    current_lights = [current_state[0], current_state[1]]
    current_fan = [current_state[4]]
    current_door = [current_state[2]]
    return render_template('index.html', currentLights=current_lights, currentFan=current_fan, currentDoor=current_door)


@app.route('/api/sensor_data')
def dht_data():
    data = Sensors.get_last_value()
    return jsonify(data)


@app.route('/api/actuator_data')
def state_data():
    data = Actuators.get_last_state()
    return jsonify(data)


@app.route('/light<light_id>/<state>')
def light_control(light_id: str, state: str):
    light_id = int(light_id)
    if light_id == 1:
        client.publish(topic="actuator/light1", payload=state, qos=0)
    elif light_id == 2:
        client.publish(topic="actuator/light2", payload=state, qos=0)
    return redirect(url_for('root'))


@app.route('/door/control/<state>')
def door_control(state: str):
    client.publish(topic="actuator/door/control", payload=state, qos=0)
    return redirect(url_for('root'))


@app.route('/door/mode/<state>')
def door_mode(state: str):
    client.publish(topic="actuator/door/mode", payload=state, qos=0)
    return redirect(url_for('root'))


@app.route('/fan/<state>')
def fan_control(state):
    client.publish(topic="actuator/fan", payload=state, qos=0)
    return redirect(url_for('root'))


if __name__ == '__main__':
    client = mqtt.Client()
    client.username_pw_set('', '')
    client.on_connect = on_connect
    client.on_publish = on_publish
    client.connect('192.168.0.101', 1883, 60)
    client.loop_start()
    app.run(debug=True)