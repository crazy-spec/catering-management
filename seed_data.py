from models import db, Location
from app import app

auditoriums = [
    {"name": "Shifa Convention Center", "type": "Auditorium", "latitude": 10.828, "longitude": 75.995},
    {"name": "Rozia International Convention Centre", "type": "Convention Centre", "latitude": 10.830, "longitude": 75.990},
    {"name": "Bianco Castle", "type": "Auditorium", "latitude": 10.832, "longitude": 75.988},
    {"name": "Crown Convention Center", "type": "Auditorium", "latitude": 10.835, "longitude": 75.992},
    {"name": "Modern Auditorium", "type": "Auditorium", "latitude": 10.829, "longitude": 75.997},
    {"name": "Zubaida Park Auditorium", "type": "Auditorium", "latitude": 10.827, "longitude": 75.993},
    {"name": "Taj Convention Centre", "type": "Auditorium", "latitude": 10.826, "longitude": 75.991},
    {"name": "Airport Garden Auditorium", "type": "Convention Hall", "latitude": 10.850, "longitude": 75.980},
    {"name": "Rose Auditorium", "type": "Auditorium", "latitude": 10.650, "longitude": 76.050},
    {"name": "Arabian Palace Convention Centre", "type": "Convention Centre", "latitude": 10.640, "longitude": 76.060},
    {"name": "Kalachalil Auditorium", "type": "Auditorium", "latitude": 10.820, "longitude": 75.985},
    {"name": "Sofia Lounge", "type": "Auditorium", "latitude": 10.825, "longitude": 75.994},
    {"name": "Qatar Auditorium", "type": "Auditorium", "latitude": 10.824, "longitude": 75.996},
    {"name": "Diamond Auditorium", "type": "Auditorium", "latitude": 10.822, "longitude": 75.992},
    {"name": "Peeyem Auditorium", "type": "Auditorium", "latitude": 10.821, "longitude": 75.989},
    {"name": "Pullat Convention Centre", "type": "Convention Centre", "latitude": 10.823, "longitude": 75.987}
]

with app.app_context():
    db.create_all()
    for a in auditoriums:
        loc = Location(name=a["name"], type=a["type"], latitude=a["latitude"], longitude=a["longitude"])
        db.session.add(loc)
    db.session.commit()
    print("All auditoriums seeded successfully!")
