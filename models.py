from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    hometown = db.Column(db.String(100))
    vehicle = db.Column(db.Boolean, default=False)
    category = db.Column(db.String(50))
    partner_id = db.Column(db.Integer, db.ForeignKey('staff.id'), nullable=True)
    attendance = db.Column(db.Integer, default=0)

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    type = db.Column(db.String(50))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'))
    rate_per_km = db.Column(db.Float, default=2.5)
    expense_type = db.Column(db.String(20))

class WorkAssignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'))
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))
    role = db.Column(db.String(50))
    work_fund = db.Column(db.Float)
    travel_expense = db.Column(db.Float)
    extras = db.Column(db.Float, default=0.0)

class Outsourcing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    provider_name = db.Column(db.String(100))
    staff_count = db.Column(db.Integer)
    details = db.Column(db.Text)
