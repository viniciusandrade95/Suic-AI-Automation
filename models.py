from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    businesses = db.relationship('Business', backref='owner', lazy=True)

class Business(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(255), nullable=False)
    whatsapp = db.Column(db.String(30))
    phone = db.Column(db.String(30))
    address = db.Column(db.String(255))
    hours = db.Column(db.String(255))
    welcome_message = db.Column(db.Text)
    bot_persona = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    services = db.relationship('Service', backref='business', lazy=True)
    clients = db.relationship('Client', backref='business', lazy=True)

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    business_id = db.Column(db.Integer, db.ForeignKey('business.id'), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.String(50))
    duration = db.Column(db.String(30))

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    business_id = db.Column(db.Integer, db.ForeignKey('business.id'), nullable=False)
    name = db.Column(db.String(255))
    contact = db.Column(db.String(255))
    last_seen = db.Column(db.DateTime)
    notes = db.Column(db.Text)
