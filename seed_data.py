from models import db, Location
from app import app

def seed_database():
    with app.app_context():
        db.create_all()

        places = [
            # Villages & Towns
            {"name": "Edappal", "type": "Village", "latitude": 10.8283, "longitude": 75.9951},
            {"name": "Kunnamkulam", "type": "Town", "latitude": 10.6500, "longitude": 76.0667},
            {"name": "Perumpilav", "type": "Village", "latitude": 10.7167, "longitude": 76.0333},
            {"name": "Changaramkulam", "type": "Village", "latitude": 10.8333, "longitude": 76.0333},
            {"name": "Thrissur", "type": "City", "latitude": 10.5276, "longitude": 76.2144},
            {"name": "Ponnani", "type": "Town", "latitude": 10.7833, "longitude": 75.9167},
            {"name": "Valanchery", "type": "Town", "latitude": 10.8833, "longitude": 76.0667},
            {"name": "Kuttippuram", "type": "Village", "latitude": 10.8333, "longitude": 76.0667},
            {"name": "Vattamkulam", "type": "Village", "latitude": 10.8167, "longitude": 76.0333},
            {"name": "Koottanad", "type": "Village", "latitude": 10.7500, "longitude": 76.0833},
            {"name": "Pazhanji", "type": "Village", "latitude": 10.6833, "longitude": 76.0333},
            {"name": "Cheruthuruthy", "type": "Village", "latitude": 10.6833, "longitude": 76.2667},
            {"name": "Guruvayur", "type": "Town", "latitude": 10.6000, "longitude": 76.0333},
            {"name": "Kozhikode", "type": "City", "latitude": 11.2588, "longitude": 75.7804},
            {"name": "Palakkad", "type": "City", "latitude": 10.7860, "longitude": 76.6548},
            {"name": "Ottapalam", "type": "Town", "latitude": 10.7667, "longitude": 76.3833},
            {"name": "Shoranur", "type": "Town", "latitude": 10.7667, "longitude": 76.2833},
            {"name": "Chittur", "type": "Town", "latitude": 10.7000, "longitude": 76.7500},
            {"name": "Alathur", "type": "Town", "latitude": 10.6500, "longitude": 76.6333},
            # … continue adding until 60+ villages/towns

            # Auditoriums / Wedding Venues
            {"name": "Shifa Convention Center", "type": "Auditorium", "latitude": 10.8285, "longitude": 75.9955},
            {"name": "Town Hall Kunnamkulam", "type": "Auditorium", "latitude": 10.6502, "longitude": 76.0669},
            {"name": "Perumpilav Auditorium", "type": "Auditorium", "latitude": 10.7168, "longitude": 76.0334},
            {"name": "Valanchery Convention Centre", "type": "Auditorium", "latitude": 10.8834, "longitude": 76.0668},
            {"name": "Thrissur Jubilee Hall", "type": "Auditorium", "latitude": 10.5277, "longitude": 76.2145},
            {"name": "Ponnani Wedding Hall", "type": "Auditorium", "latitude": 10.7835, "longitude": 75.9169},
            {"name": "Kozhikode Town Hall", "type": "Auditorium", "latitude": 11.2589, "longitude": 75.7805},
            {"name": "Palakkad Town Hall", "type": "Auditorium", "latitude": 10.7861, "longitude": 76.6549},

            # Mosques
            {"name": "Edappal Juma Masjid", "type": "Mosque", "latitude": 10.8284, "longitude": 75.9952},
            {"name": "Kunnamkulam Juma Masjid", "type": "Mosque", "latitude": 10.6501, "longitude": 76.0668},
            {"name": "Ponnani Juma Masjid", "type": "Mosque", "latitude": 10.7834, "longitude": 75.9168},
            {"name": "Valanchery Juma Masjid", "type": "Mosque", "latitude": 10.8835, "longitude": 76.0669},
            {"name": "Thrissur Juma Masjid", "type": "Mosque", "latitude": 10.5279, "longitude": 76.2147},
            {"name": "Palakkad Juma Masjid", "type": "Mosque", "latitude": 10.7862, "longitude": 76.6550},
            {"name": "Ottapalam Masjid", "type": "Mosque", "latitude": 10.7669, "longitude": 76.3835},
            {"name": "Shoranur Masjid", "type": "Mosque", "latitude": 10.7668, "longitude": 76.2834},
            {"name": "Chittur Masjid", "type": "Mosque", "latitude": 10.7001, "longitude": 76.7501},
            {"name": "Alathur Masjid", "type": "Mosque", "latitude": 10.6501, "longitude": 76.6334},
            # … continue until 20+ mosques

            # Temples
            {"name": "Thrissur Vadakkumnathan Temple", "type": "Temple", "latitude": 10.5276, "longitude": 76.2144},
            {"name": "Kunnamkulam Sree Krishna Temple", "type": "Temple", "latitude": 10.6503, "longitude": 76.0670},
            {"name": "Edappal Bhagavathi Temple", "type": "Temple", "latitude": 10.8286, "longitude": 75.9956},
            {"name": "Perumpilav Shiva Temple", "type": "Temple", "latitude": 10.7169, "longitude": 76.0335},
            {"name": "Guruvayur Temple", "type": "Temple", "latitude": 10.6001, "longitude": 76.0334},
            {"name": "Kalpathy Vishwanatha Swamy Temple", "type": "Temple", "latitude": 10.7863, "longitude": 76.6551},
            {"name": "Jainimedu Jain Temple", "type": "Temple", "latitude": 10.7864, "longitude": 76.6552},
            {"name": "Ottapalam Shiva Temple", "type": "Temple", "latitude": 10.7671, "longitude": 76.3837},
            {"name": "Shoranur Bhagavathi Temple", "type": "Temple", "latitude": 10.7669, "longitude": 76.2835},
            {"name": "Chittur Bhagavathi Temple", "type": "Temple", "latitude": 10.7002, "longitude": 76.7502},
            # … continue until 20+ temples

            # Schools
            {"name": "Edappal Higher Secondary School", "type": "School", "latitude": 10.8287, "longitude": 75.9957},
            {"name": "Kunnamkulam Govt. High School", "type": "School", "latitude": 10.6504, "longitude": 76.0671},
            {"name": "Thrissur Model School", "type": "School", "latitude": 10.5278, "longitude": 76.2146},
            {"name": "Ponnani Public School", "type": "School", "latitude": 10.7836, "longitude": 75.9170},
            {"name": "Valanchery English School", "type": "School", "latitude": 10.8836, "longitude": 76.0670},
            {"name": "Palakkad Govt. Victoria College", "type": "School", "latitude": 10.7865, "longitude": 76.6553},
            {"name": "Ottapalam Higher Secondary School", "type": "School", "latitude": 10.7670, "longitude": 76.3836},
            {"name": "Shoranur Govt. High School", "type": "School", "latitude": 10.7669, "longitude": 76.2836},
            {"name": "Chittur Govt. High School", "type": "School", "latitude": 10.7003, "longitude": 76.7503},
            {"name": "Alathur Govt. High School", "type": "School", "latitude": 10.6502, "longitude": 76.6335},
            # … continue until 15+ schools
        ]

        for p in places:
            loc = Location(name=p["name"], type=p["type"], latitude=p["latitude"], longitude=p["longitude"])
            db.session.add(loc)

        db.session.commit()
        print(f"✅ Finished seeding. Total entries added: {len(places)}")

if __name__ == "__main__":
    seed_database()
