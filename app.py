from flask import Flask, render_template_string, request
from models import db, Staff, Location, Event, WorkAssignment
import math

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///catering.db'
db.init_app(app)

# Distance calculation (Haversine formula)
def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c

@app.route('/')
def index():
    staff = Staff.query.all()
    events = Event.query.all()
    return render_template_string(open("index.html").read(), staff=staff, events=events)

@app.route('/add_event', methods=['POST'])
def add_event():
    name = request.form['name']
    location_id = request.form['location_id']
    rate = float(request.form['rate'])
    expense_type = request.form['expense_type']
    event = Event(name=name, location_id=location_id, rate_per_km=rate, expense_type=expense_type)
    db.session.add(event)
    db.session.commit()
    return "Event added!"

@app.route('/assign_work', methods=['POST'])
def assign_work():
    staff_id = int(request.form['staff_id'])
    event_id = int(request.form['event_id'])
    role = request.form['role']
    work_fund = float(request.form['work_fund'])

    staff = Staff.query.get(staff_id)
    event = Event.query.get(event_id)
    location = Location.query.get(event.location_id)
    hometown = Location.query.filter_by(name=staff.hometown).first()

    distance = calculate_distance(hometown.latitude, hometown.longitude, location.latitude, location.longitude)
    travel_expense = distance * event.rate_per_km

    assignment = WorkAssignment(staff_id=staff_id, event_id=event_id, role=role, work_fund=work_fund, travel_expense=travel_expense)
    db.session.add(assignment)
    db.session.commit()

    return f"Assigned {staff.name} to {event.name}. Total = {work_fund + travel_expense:.2f} INR"
