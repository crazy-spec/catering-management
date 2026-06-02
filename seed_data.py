from models import db, Location
from app import app

auditoriums = [
    {"name": "Shifa Convention Center", "type": "Auditorium", "latitude": 10.8283, "longitude": 75.9951},
    {"name": "Rozia International Convention Centre", "type": "Convention Centre", "latitude": 10.8302, "longitude": 75.9904},
    {"name": "Bianco Castle", "type": "Auditorium", "latitude": 10.8325, "longitude": 75.9887},
    {"name": "Crown Convention Center", "type": "Auditorium", "latitude": 10.8350, "longitude": 75.9922},
    {"name": "Modern Auditorium", "type": "Auditorium", "latitude": 10.8299, "longitude": 75.9970},
    {"name": "Rose Auditorium", "type": "Auditorium", "latitude": 10.6501, "longitude": 76.0503},
    {"name": "Arabian Palace Convention Centre", "type": "Convention Centre", "latitude": 10.6405, "longitude": 76.0602},
    {"name": "Changramkulam Town Hall", "type": "Auditorium", "latitude": 10.8100, "longitude": 75.9800},
    {"name": "Perumpilav Convention Hall", "type": "Auditorium", "latitude": 10.7200, "longitude": 76.0300},
    # … plus every other hall and surrounding place within 30 km
]

with app.app_context():
    db.create_all()
    for a in auditoriums:
        loc = Location(name=a["name"], type=a["type"], latitude=a["latitude"], longitude=a["longitude"])
        db.session.add(loc)
    db.session.commit()
    print("All auditoriums and places seeded successfully!")
