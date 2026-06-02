from flask import Flask, render_template_string, request
from models import db, Staff, Location, Event, WorkAssignment
import math

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///catering.db'
db.init_app(app)

# -----------------------------
# Distance calculation function
# -----------------------------
def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371  # Earth radius in km
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c

# -----------------------------
# Homepage
# -----------------------------
@app.route('/')
def index():
    staff = Staff.query.all()
    events = Event.query.all()
    return render_template_string(open("index.html").read(), staff=staff, events=events)

# -----------------------------
# Add Event
# -----------------------------
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

# -----------------------------
# Assign Work
# -----------------------------
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

    assignment = WorkAssignment(
        staff_id=staff_id,
        event_id=event_id,
        role=role,
        work_fund=work_fund,
        travel_expense=travel_expense
    )
    db.session.add(assignment)
    db.session.commit()

    return f"Assigned {staff.name} to {event.name}. Total = {work_fund + travel_expense:.2f} INR"

# -----------------------------
# Reporting Module
# -----------------------------
@app.route('/report')
def report():
    events = Event.query.all()
    report_data = []

    for e in events:
        assignments = WorkAssignment.query.filter_by(event_id=e.id).all()
        total_works = len(assignments)
        reception_count = sum(1 for a in assignments if a.role.lower() == "reception")
        lunch_count = sum(1 for a in assignments if a.role.lower() == "lunch")
        total_fund = sum(a.work_fund for a in assignments)
        total_travel = sum(a.travel_expense for a in assignments)
        total_extras = sum(a.extras for a in assignments)

        report_data.append({
            "event": e.name,
            "total_works": total_works,
            "reception": reception_count,
            "lunch": lunch_count,
            "fund": total_fund,
            "travel": total_travel,
            "extras": total_extras,
            "grand_total": total_fund + total_travel + total_extras
        })

    return render_template_string(open("report.html").read(), report_data=report_data)

# -----------------------------
# Run locally
# -----------------------------
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
