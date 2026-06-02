from models import db, Location
from app import app

# Auditorium data (sample coordinates, replace with actual Google Maps lat/long)
auditoriums = [
    {"name": "Shifa Convention Center", "type": "Auditorium", "latitude": 10.828, "longitude": 75.995},
    {"name": "Rozia International Convention Centre", "type": "Convention Centre", "latitude": 10.830, "longitude": 75.990},
    {"name": "Bianco Castle", "type": "Auditorium", "latitude": 10.832, "longitude": 75.988},
    {"name": "Crown Convention Center", "type": "Auditorium", "latitude": 10.835, "longitude": 75.992},
    {"name": "Rose Auditorium", "type": "Auditorium", "latitude": 10.650, "longitude": 76.050},
    {"name": "Modern Auditorium", "type": "Auditorium", "latitude": 10.829, "longitude": 75.997},
    {"name": "Arabian Palace Convention Centre", "type": "Convention Centre", "latitude": 10.640, "longitude": 76.060},
    {"name": "Zubaida Park Auditorium", "type": "Auditorium", "latitude": 10.827, "longitude": 75.993},
    {"name": "Taj Convention Centre", "type": "Auditorium", "latitude": 10.826, "longitude": 75.991},
    {"name": "Airport Garden Auditorium", "type": "Convention Hall", "latitude": 10.850, "longitude": 75.980}
]

with app.app_context():
    db.create_all()
    for a in auditoriums:
        loc = Location(name=a["name"], type=a["type"], latitude=a["latitude"], longitude=a["longitude"])
        db.session.add(loc)
    db.session.commit()
    print("Auditoriums seeded successfully!")
