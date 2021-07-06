from models.db import db
from datetime import datetime


class Home(db.Model):
    __tablename__ = 'home'
    sensor_id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.Integer, db.ForeignKey('devices.device_id'))
    type = db.Column(db.String)
    name = db.Column(db.String)

    def __init__(self, sensor_id, device_id, type, name):
        self.sensor_id = sensor_id
        self.device_id = device_id
        self.type = type
        self.name = name

    def json(self):
        return {'sensor_id': self.sensor_id, 'device_id': self.device_id, 'type': self.type,
                'name': self.name}

    @classmethod
    def get_all_device(cls):
        query = db.session.query(cls)
        homes = [i.json() for i in query]
        db.session.rollback()
        return homes

    @classmethod
    def get_by_device_id(cls, device_id: int):
        device_data = db.session.query(cls).filter_by(device_id=device_id).first().json()
        db.session.rollback()
        return device_data

    @classmethod
    def get_by_sensor_id(cls, sensor_id: int):
        device_data = db.session.query(cls).filter_by(sensor_id=sensor_id).frist().json()
        db.session.rollback()
        return device_data

    @classmethod
    def add(cls, sensor_id, device_id, type, name):
        new_device = cls(sensor_id=sensor_id, device_id=device_id, type=type, name=name)
        db.session.add(new_device)
        db.session.commit()
        db.session.rollback()
        return new_device


class Devices(db.Model):
    __tablename__ = 'devices'
    device_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ip_device = db.Column(db.String)
    parent_id = db.Column(db.String, nullable=True)
    up_time = db.Column(db.TIMESTAMP, nullable=True)
    location = db.Column(db.String)

    def __init__(self, device_id, name, ip_device, location, parent_id=None, up_time=None):
        self.device_id = device_id
        self.name = name
        self.ip_device = ip_device
        self.parent_id = parent_id
        self.up_time = up_time
        self.location = location

    def json(self):
        return {'device_id': self.device_id, 'name': self.name, 'ip_device': self.ip_device,
                'parent_id': self.parent_id, 'up_time': self.up_time, 'location': self.location}

    @classmethod
    def get_by_device_id(cls, device_id: int):
        device_data = db.session.query(cls).filter_by(device_id=device_id).first().json()
        db.session.rollback()
        return device_data

    @classmethod
    def get_all_device(cls):
        query = db.session.query(cls)
        devices = [i.json() for i in query]
        return devices

    @classmethod
    def add(cls, device_id, name, ip_device='NaN', parent_id=None, up_time=None, location='NaN'):
        new_devices = cls(device_id=device_id, name=name, ip_device=ip_device,
                          location=location, parent_id=parent_id, up_time=up_time)
        db.session.add(new_devices)
        db.session.commit()
        db.session.rollback()
        return new_devices.json()

    @classmethod
    def update_name(cls, name=name):
        stmt = db.update(cls).where(cls.name == name).values(
            name=name).execution_options(synchronize_session="fetch")
        result = db.session.execute(stmt)
        db.session.rollback()
        return result

    @classmethod
    def delete_by_name(cls, name=name):
        stmt = db.delete(cls).where(cls.name == name).execution_options(synchronize_session="fetch")
        result = db.session.execute(stmt)
        db.session.rollback()
        return result


class Sensors(db.Model):
    __tablename__ = 'sensors'
    id = db.Column(db.Integer, primary_key=True)
    sensor_id = db.Column(db.Integer, db.ForeignKey('home.sensor_id'))
    value = db.Column(db.JSON)
    time = db.Column(db.TIMESTAMP)

    def __init__(self, id, sensor_id, value, time):
        self.id = id
        self.sensor_id = sensor_id
        self.value = value
        self.time = time

    def json(self):
        return {'sensor_id': self.sensor_id, 'value': self.value, 'time': self.time.strftime("%m/%d/%Y, %H:%M:%S")}

    @classmethod
    def get_by_sensor_id(cls, sensor_id: int):
        sensor = cls.query.filter_by(sensor_id=sensor_id).order_by(cls.id.desc()).first()
        db.session.rollback()
        return sensor

    @classmethod
    def get_last_value(cls):
        last_date = db.session.query(cls.sensor_id, db.func.max(cls.time).label('value_up_to_date')).group_by(
            cls.sensor_id).subquery()
        query = cls.query.join(last_date, cls.time == last_date.c.value_up_to_date).order_by(cls.sensor_id).all()
        last_value = [i.json() for i in query]
        db.session.rollback()
        return last_value

    @classmethod
    def add(cls, sensor_id, value, time=datetime.now()):
        new_value = cls(sensor_id=sensor_id, value=value, time=time.strftime("%Y-%m-%d %H:%M:%S"))
        db.session.add(new_value)
        db.session.commit()
        db.session.rollback()
        return new_value

    @classmethod
    def update(cls, sensor_id, value, time=datetime.now()):
        stmt = db.update(cls).where(cls.sensor_id == sensor_id).values(
            value=value, time=time.strftime("%Y-%m-%d %H:%M:%S")).execution_options(synchronize_session="fetch")
        result = db.session.execute(stmt)
        db.session.rollback()
        return result


class Actuators(db.Model):
    __tablename__ = 'actuators'
    id = db.Column(db.Integer, primary_key=True)
    sensor_id = db.Column(db.Integer, db.ForeignKey('home.sensor_id'))
    state = db.Column(db.Integer)
    time = db.Column(db.TIMESTAMP)

    def __init__(self, sensor_id, state, time):
        self.sensor_id = sensor_id
        self.state = state
        self.time = time

    def json(self):
        return {'sensor_id': self.sensor_id, 'state': self.state, 'time': self.time.strftime("%m/%d/%Y, %H:%M:%S")}

    @classmethod
    def get_by_sensor_id(cls, sensor_id: int):
        db.session.rollback()
        return cls.query.filter_by(sensor_id=sensor_id).order_by(cls.id.desc()).first()

    @classmethod
    def get_last_state(cls):
        query = db.session.query(cls).distinct(cls.sensor_id)
        last_state = [i.json() for i in query]
        db.session.rollback()
        return last_state

    @classmethod
    def add(cls, sensor_id, state, time=datetime.now()):
        new_state = cls(sensor_id=sensor_id, state=state, time=time.strftime("%Y-%m-%d %H:%M:%S"))
        db.session.add(new_state)
        db.session.commit()
        db.session.rollback()
        return new_state.json()

    @classmethod
    def update(cls, sensor_id, state, time=datetime.now()):
        stmt = db.update(cls).where(cls.sensor_id == sensor_id).values(
            state=state, time=time.strftime("%Y-%m-%d %H:%M:%S")).execution_options(synchronize_session="fetch")
        result = db.session.execute(stmt)
        db.session.rollback()
        return result


