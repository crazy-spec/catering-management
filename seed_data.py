from models import db, Location
from app import app

def seed_database():
    with app.app_context():
        db.create_all()

        places = [
            # Villages
            {"name": "Edappal", "type": "Village", "latitude": 10.8283, "longitude": 75.9951},
            {"name": "Kunnamkulam", "type": "Town", "latitude": 10.6500, "longitude": 76.0667},
            {"name": "Perumpilav", "type": "Village", "latitude": 10.7167, "longitude": 76.0333},
            {"name": "Changaramkulam", "type": "Village", "latitude": 10.8333, "longitude": 76.0333},

            # Auditoriums
            {"name": "Shifa Convention Center", "type": "Auditorium", "latitude": 10.8285, "longitude": 75.9955},
            {"name": "Town Hall Kunnamkulam", "type": "Auditorium", "latitude": 10.6502, "longitude": 76.0669},

            # Mosques
            {"name": "Edappal Juma Masjid", "type": "Mosque", "latitude": 10.8284, "longitude": 75.9952},
            {"name": "Kunnamkulam Juma Masjid", "type": "Mosque", "latitude": 10.6501, "longitude": 76.0668},

            # Temples
            {"name": "Thrissur Vadakkumnathan Temple", "type": "Temple", "latitude": 10.5276, "longitude": 76.2144},
            {"name": "Kunnamkulam Sree Krishna Temple", "type": "Temple", "latitude": 10.6503, "longitude": 76.0670},
        ]

        for p in places:
            loc = Location(name=p["name"], type=p["type"], latitude=p["latitude"], longitude=p["longitude"])
            db.session.add(loc)

        db.session.commit()
        print(f"✅ Finished seeding. Total entries added: {len(places)}")

if __name__ == "__main__":
    seed_database()
