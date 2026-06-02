import requests
from models import db, Location
from app import app

# Center coordinates (Edappal) and radius (30 km)
CENTER_LAT, CENTER_LON = 10.8283, 75.9951
RADIUS = 30000  # meters

# Overpass API query: fetch villages, towns, auditoriums, halls, convention centres, religious/community halls
query = f"""
[out:json][timeout:60];
(
  node["place"~"village|town"](around:{RADIUS},{CENTER_LAT},{CENTER_LON});
  node["amenity"~"community_centre|townhall|events_venue"](around:{RADIUS},{CENTER_LAT},{CENTER_LON});
  node["building"~"auditorium|hall|convention_centre"](around:{RADIUS},{CENTER_LAT},{CENTER_LON});
  node["amenity"~"place_of_worship"](around:{RADIUS},{CENTER_LAT},{CENTER_LON});
  node["building"~"mosque|church|temple"](around:{RADIUS},{CENTER_LAT},{CENTER_LON});
  node["amenity"~"school"](around:{RADIUS},{CENTER_LAT},{CENTER_LON});
);
out body;
"""

def fetch_places():
    url = "https://overpass-api.de/api/interpreter"
    response = requests.post(url, data={"data": query})
    data = response.json()
    return data["elements"]

def seed_database():
    places = fetch_places()
    with app.app_context():
        db.create_all()
        for p in places:
            name = p.get("tags", {}).get("name", "Unnamed Place")
            lat = p["lat"]
            lon = p["lon"]
            # classify type
            if any(k in name.lower() for k in ["auditorium","hall","convention","centre","palace"]):
                loc_type = "Auditorium"
            elif any(k in name.lower() for k in ["mosque","church","temple"]):
                loc_type = "Religious Hall"
            elif "school" in name.lower():
                loc_type = "School Auditorium"
            else:
                loc_type = "Place"
            loc = Location(name=name, type=loc_type, latitude=lat, longitude=lon)
            db.session.add(loc)
        db.session.commit()
        print(f"Seeded {len(places)} locations successfully!")

if __name__ == "__main__":
    seed_database()
