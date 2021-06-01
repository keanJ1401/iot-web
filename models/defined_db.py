from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Home(db.Model):
    __tablename__ = 'home'
    sensor_id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.Integer, db.ForeignKey('devices.device_id'))
    type = db.Column(db.String(50))
    name = db.Column(db.String(50))

    def __init__(self, device_id, type, name):
        self.device_id = device_id
        self.type = type
        self.name = name


class Devices(db.Model):
    __tablename__ = 'devices'
    device_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    ip_device = db.Column(db.String(50))
    parent_id = db.Column(db.String(50), nullable=True)
    up_time = db.Column(db.TIMESTAMP, nullable=True)
    location = db.Column(db.String(50))

    def __init__(self, name, ip_device, location, parent_id=None, up_time=None):
        self.name = name
        self.ip_device = ip_device
        self.parent_id = parent_id
        self.up_time = up_time
        self.location = location


class Sensors(db.Model):
    __tablename__ = 'sensors'
    id = db.Column(db.Integer, primary_key=True)
    sensor_id = db.Column(db.Integer, db.ForeignKey('sensors.sensor_id'))
    value = db.Column(db.JSON)
    time = db.Column(db.TIMESTAMP)

    def __init__(self, sensor_id, value, time):
        self.sensor_id = sensor_id
        self.value = value
        self.time = time

    def json(self):
        return {'sensor_id': self.sensor_id, 'value': self.value, 'time': self.time.strftime("%m/%d/%Y, %H:%M:%S")}

    @classmethod
    def get_by_sensor_id(cls, sensor_id: int):
        db.session.rollback()
        return cls.query.filter_by(sensor_id=sensor_id).order_by(cls.id.desc()).first()


    @classmethod
    def get_last_value(cls):
        last_date = db.session.query(Sensors.sensor_id, db.func.max(Sensors.time).label('value_up_to_date')).group_by(
            Sensors.sensor_id).subquery()
        query = Sensors.query.join(last_date, Sensors.time == last_date.c.value_up_to_date).order_by(Sensors.sensor_id).all()
        data = [i.json() for i in query]
        db.session.rollback()
        return data


class Actuators(db.Model):
    __tablename__ = 'actuators'
    id = db.Column(db.Integer, primary_key=True)
    sensor_id = db.Column(db.Integer, db.ForeignKey('sensors.sensor_id'))
    state = db.Column(db.Boolean)
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
        last_date = db.session.query(Actuators.sensor_id, db.func.max(Actuators.time).label('state_up_to_date')).group_by(
            Actuators.sensor_id).subquery()
        query = Actuators.query.join(last_date, Actuators.time == last_date.c.state_up_to_date).order_by(Actuators.sensor_id).all()
        data = [i.json() for i in query]
        db.session.rollback()
        return data
