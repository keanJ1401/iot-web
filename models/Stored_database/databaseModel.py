import sqlite3, json
from db import db

database_location = r"F:\Thesis\web-flask\database.db"


class BrokerModel(db.Model):
    __tablename__ = 'brokers'

    id = db.Column(db.Integer, primary_key=True)
    ip_device = db.Column(db.String(32))
    uptime_at = db.Column(db.TIMESTAMP)
    rssi_value = db.Column(db.Integer)
    location = db.Column(db.String(32))
    id_device = db.Column(db.Integer, db.ForeignKey('device.id'))
    device = db.relationship('DeviceModel')

    __tablename__ = 'devices'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    value = db.Column(db.Float(precision=2))
    state = db.Column(db.Boolean)

    items = db.relationship('Broker', lazy='dynamic')

    def __int__(self, _id: int, ip: str, uptime: str, location: str):
        self.id = _id
        self.ip = ip
        self.uptime = uptime
        self.location = location

    @classmethod
    def insert(cls):
        conn = sqlite3.connect(database_location)
        cur = conn.cursor()

        query = "INSERT INTO "

