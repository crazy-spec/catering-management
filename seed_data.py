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
        {"name": "Mannarkkad", "type": "Town", "latitude": 10.9833, "longitude": 76.4667},
        {"name": "Kollengode", "type": "Village", "latitude": 10.5667, "longitude": 76.6833},
        {"name": "Puthanathani", "type": "Village", "latitude": 10.8833, "longitude": 76.0333},
        {"name": "Kondotty", "type": "Town", "latitude": 11.1333, "longitude": 75.9667},
        {"name": "Malappuram", "type": "City", "latitude": 11.0667, "longitude": 76.0667},
        {"name": "Tirur", "type": "Town", "latitude": 10.9167, "longitude": 75.9167},
        {"name": "Tanur", "type": "Town", "latitude": 10.9833, "longitude": 75.8667},
        {"name": "Kottakkal", "type": "Town", "latitude": 10.9500, "longitude": 76.0000},
        {"name": "Parappanangadi", "type": "Town", "latitude": 11.0500, "longitude": 75.9167},
        {"name": "Feroke", "type": "Town", "latitude": 11.1833, "longitude": 75.8333},
        {"name": "Ramanattukara", "type": "Town", "latitude": 11.2000, "longitude": 75.8667},
        {"name": "Kunnamangalam", "type": "Town", "latitude": 11.3000, "longitude": 75.8667},
        {"name": "Mankada", "type": "Village", "latitude": 11.0333, "longitude": 76.0833},
        {"name": "Nilambur", "type": "Town", "latitude": 11.2833, "longitude": 76.2333},
        {"name": "Pandikkad", "type": "Village", "latitude": 11.0667, "longitude": 76.1667},
        {"name": "Wandoor", "type": "Village", "latitude": 11.1167, "longitude": 76.2667},
        {"name": "Karuvarakundu", "type": "Village", "latitude": 11.0833, "longitude": 76.2333},
        {"name": "Perinthalmanna", "type": "Town", "latitude": 10.9833, "longitude": 76.2167},
        {"name": "Cherpulassery", "type": "Town", "latitude": 10.8833, "longitude": 76.3167},
        {"name": "Sreekrishnapuram", "type": "Village", "latitude": 10.9500, "longitude": 76.3833},
        {"name": "Alanallur", "type": "Village", "latitude": 10.9500, "longitude": 76.3333},
        {"name": "Koppam", "type": "Village", "latitude": 10.8333, "longitude": 76.2833},
        {"name": "Pattambi", "type": "Town", "latitude": 10.8000, "longitude": 76.2000},
        {"name": "Thrithala", "type": "Village", "latitude": 10.7833, "longitude": 76.0833},
        {"name": "Anakkara", "type": "Village", "latitude": 10.7167, "longitude": 76.0333},
        {"name": "Kumaranellur", "type": "Village", "latitude": 10.7500, "longitude": 76.2000},
        {"name": "Parudur", "type": "Village", "latitude": 10.7667, "longitude": 76.1333},
        {"name": "Thirumittacode", "type": "Village", "latitude": 10.7500, "longitude": 76.2833},
        {"name": "Nagallassery", "type": "Village", "latitude": 10.7833, "longitude": 76.1667},
        {"name": "Kumaramputhur", "type": "Village", "latitude": 10.9500, "longitude": 76.4667},
        {"name": "Karimba", "type": "Village", "latitude": 10.9500, "longitude": 76.4000},
        {"name": "Kottayi", "type": "Village", "latitude": 10.7000, "longitude": 76.6333},
        {"name": "Puthunagaram", "type": "Town", "latitude": 10.7000, "longitude": 76.7000},
        {"name": "Muthalamada", "type": "Village", "latitude": 10.5667, "longitude": 76.7500},
        {"name": "Nemmara", "type": "Town", "latitude": 10.5667, "longitude": 76.6833},
        {"name": "Ayilur", "type": "Village", "latitude": 10.5667, "longitude": 76.6500},
        {"name": "Vadakkanchery", "type": "Town", "latitude": 10.6500, "longitude": 76.2667},
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
        {"name": "Ottapalam Convention Centre", "type": "Auditorium", "latitude": 10.7668, "longitude": 76.3834},
        {"name": "Shoranur Community Hall", "type": "Auditorium", "latitude": 10.7668, "longitude": 76.2834},
        {"name": "Chittur Wedding Auditorium", "type": "Auditorium", "latitude": 10.7001, "longitude": 76.7501},
        {"name": "Alathur Convention Hall", "type": "Auditorium", "latitude": 10.6501, "longitude": 76.6334},
        {"name": "Mannarkkad Convention Centre", "type": "Auditorium", "latitude": 10.9834, "longitude": 76.4668},
        {"name": "Kollengode Town Hall", "type": "Auditorium", "latitude": 10.5668, "longitude": 76.6834},
        {"name": "Nilambur Convention Centre", "type": "Auditorium", "latitude": 11.2834, "longitude": 76.2334},
        {"name": "Tirur Town Hall", "type": "Auditorium", "latitude": 10.9168, "longitude": 75.9168},
        {"name": "Tanur Convention Hall", "type": "Auditorium", "latitude": 10.9834, "longitude": 75.8668},
        {"name": "Kottakkal Convention Centre", "type": "Auditorium", "latitude": 10.9501, "longitude": 76.0001},
        {"name": "Parappanangadi Town Hall", "type": "Auditorium", "latitude": 11.0501, "longitude": 75.9168},
        {"name": "Feroke Convention Centre", "type": "Auditorium", "latitude": 11.1834, "longitude": 75.8334},
        {"name": "Ramanattukara Town Hall", "type": "Auditorium", "latitude": 11.2001, "longitude": 75.8668},
        {"name": "Kunnamangalam Convention Centre", "type": "Auditorium", "latitude": 11.3001, "longitude": 75.8668},
        {"name": "Perinthalmanna Town Hall", "type": "Auditorium", "latitude": 10.9834, "longitude": 76.2168},
        {"name": "Cherpulassery Convention Centre", "type": "Auditorium", "latitude": 10.8834, "longitude": 76.3168},
        {"name": "Pattambi Town Hall", "type": "Auditorium", "latitude": 10.8001, "longitude": 76.2001},

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
        {"name": "Mannarkkad Masjid", "type": "Mosque", "latitude": 10.9834, "longitude": 76.4668},
        {"name": "Nilambur Masjid", "type": "Mosque", "latitude": 11.2834, "longitude": 76.2334},
        {"name": "Tirur Masjid", "type": "Mosque", "latitude": 10.9168, "longitude": 75.9168},
        {"name": "Tanur Masjid", "type": "Mosque", "latitude": 10.9834, "longitude": 75.8668},
        {"name": "Kottakkal Masjid", "type": "Mosque", "latitude": 10.9501, "longitude": 76.0001},
        {"name": "Parappanangadi Masjid", "type": "Mosque", "latitude": 11.0501, "longitude": 75.9168},
        {"name": "Feroke Masjid", "type": "Mosque", "latitude": 11.1834, "longitude": 75.8334},
        {"name": "Ramanattukara Masjid", "type": "Mosque", "latitude": 11.2001, "longitude": 75.8668},
        {"name": "Kunnamangalam Masjid", "type": "Mosque", "latitude": 11.3001, "longitude": 75.8668},
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
