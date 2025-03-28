from utils.db import db


class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    mac_address = db.Column(db.String(17), nullable=False)
    serial_number = db.Column(db.String(20), nullable=False)
    manufacturer = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(100), nullable=False)

    def __init__(self, name, price, mac_address, serial_number, manufacturer, description):
        self.name = name
        self.price = price
        self.mac_address = mac_address
        self.serial_number = serial_number
        self.manufacturer = manufacturer
        self.description = description
