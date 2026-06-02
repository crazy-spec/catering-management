from models import db, Location
from app import app

auditoriums = [
    # --- Edappal Auditoriums ---
    {"name": "Shifa Convention Center", "type": "Auditorium", "latitude": 10.8283, "longitude": 75.9951},
    {"name": "Rozia International Convention Centre", "type": "Convention Centre", "latitude": 10.8302, "longitude": 75.9904},
    {"name": "Bianco Castle", "type": "Auditorium", "latitude": 10.8325, "longitude": 75.9887},
    {"name": "Crown Convention Center", "type": "Auditorium", "latitude": 10.8350, "longitude": 75.9922},
    {"name": "Modern Auditorium", "type": "Auditorium", "latitude": 10.8299, "longitude": 75.9970},
    {"name": "Zubaida Park Auditorium", "type": "Auditorium", "latitude": 10.8277, "longitude": 75.9933},
    {"name": "Taj Convention Centre", "type": "Auditorium", "latitude": 10.8264, "longitude": 75.9918},
    {"name": "Kalachalil Auditorium", "type": "Auditorium", "latitude": 10.8200, "longitude": 75.9850},
    {"name": "Sofia Lounge", "type": "Auditorium", "latitude": 10.8250, "longitude": 75.9940},
    {"name": "Qatar Auditorium", "type": "Auditorium", "latitude": 10.8240, "longitude": 75.9960},
    {"name": "Diamond Auditorium", "type": "Auditorium", "latitude": 10.8220, "longitude": 75.9920},
    {"name": "Peeyem Auditorium", "type": "Auditorium", "latitude": 10.8210, "longitude": 75.9890},
    {"name": "Pullat Convention Centre", "type": "Convention Centre", "latitude": 10.8230, "longitude": 75.9870},

    # --- Kunnamkulam Auditoriums ---
    {"name": "Rose Auditorium", "type": "Auditorium", "latitude": 10.6501, "longitude": 76.0503},
    {"name": "Arabian Palace Convention Centre", "type": "Convention Centre", "latitude": 10.6405, "longitude": 76.0602},

    # --- Changramkulam / Perumpilav Auditoriums ---
    {"name": "Changramkulam Town Hall", "type": "Auditorium", "latitude": 10.8100, "longitude": 75.9800},
    {"name": "Perumpilav Convention Hall", "type": "Auditorium", "latitude": 10.7200, "longitude": 76.0300},

    # --- Key Towns/Villages (for staff hometowns & expense calc) ---
    {"name": "Edappal Town", "type": "Place", "latitude": 10.8280, "longitude": 75.9900},
    {"name": "Kunnamkulam Town", "type": "Place", "latitude": 10.6500, "longitude": 76.0700},
    {"name": "Changramkulam", "type": "Place", "latitude": 10.8100, "longitude": 75.9800},
    {"name": "Perumpilav", "type": "Place", "latitude": 10.7200, "longitude": 76.0300},
    {"name": "Thrissur", "type": "Place", "latitude": 10.5276, "longitude": 76.2144},
    {"name": "Kozhikode", "type": "Place", "latitude": 11.2588, "longitude": 75.7804},
    {"name": "Ponnani", "type": "Place", "latitude": 10.7666, "longitude": 75.9259},
    {"name": "Valanchery", "type": "Place", "latitude": 10.8790, "longitude": 76.0500},
    {"name": "Kottakkal", "type": "Place", "latitude": 10.9940, "longitude": 76.0050},
    {"name": "Tirur", "type": "Place", "latitude": 10.9000, "longitude": 75.9200}
]

with app.app_context():
    db.create_all()
    for a in auditoriums:
        loc = Location(name=a["name"], type=a["type"], latitude=a["latitude"], longitude=a["longitude"])
        db.session.add(loc)
    db.session.commit()
    print("All auditoriums and places seeded successfully!")
