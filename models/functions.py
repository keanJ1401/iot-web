import time
from .defined_db import Actuators


def format_server_time():
    server_time = time.localtime()
    return time.strftime("%d/%m/%Y, %H:%M:%S", server_time)


def CurrentLights(sensor_id):
    current_lights = [
    {
        "id": sensor_id,
        "state": Actuators.get_by_sensor_id(sensor_id).state,
    },
    {
        "id": Actuators.get_by_sensor_id(2).sensor_id,
        "state": Actuators.get_by_sensor_id(2).state,
    },
                    ]
    return current_lights 

def CurrentDoor(sensor_id):
    current_door = [
    {
        "id": sensor_id,
        "state": Actuators.get_by_sensor_id(sensor_id).state,
    },
                    ]
    return current_door

def CurrentFan(sensor_id):
    current_fan = [
    {
        "id": sensor_id,
        "state": Actuators.get_by_sensor_id(sensor_id).state,
    },
                    ]
    return current_fan