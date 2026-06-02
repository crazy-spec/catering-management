import requests
from models import db, Location
from app import app

# --- Manual entries (important auditoriums you want to ensure are always included) ---
manual_places = [
    {"name": "Shifa Convention Center", "type": "Auditorium", "latitude": 10.8283, "longitude": 75.9951},
    {"name": "Rozia International Convention Centre", "type": "Convention Centre", "latitude": 10.8302, "longitude": 75.9904},
    {"name": "Bianco Castle", "type": "Auditorium", "latitude": 10.8325, "longitude": 75.9887},
    {"name": "Crown Convention Center", "type": "Auditorium", "latitude": 10.8350, "longitude": 75.9922},
    {"name": "Modern Auditorium", "type": "Auditorium", "latitude": 10.8299, "longitude": 75.9970},
    {"name": "Rose Auditorium", "type": "Auditorium", "latitude": 10.6501, "longitude": 76.0503},
    {"name": "Arabian Palace Convention Centre", "type": "Convention Centre", "latitude": 10.6405, "longitude": 76.0602},
    {"name": "Changramkulam Town Hall", "type": "Auditorium", "latitude": 10.8100, "longitude": 75.9800},
    {"name": "Perumpilav Convention Hall", "type": "Auditorium", "latitude": 10.7200, "longitude": 76.0300},
]

# --- OSM auto-fetch settings ---
CENTER_LAT, CENTER_LON = 10.8283, 75.9951  # Edappal
RADIUS = 30000  # 30 km

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

def fetch_osm_places():
    url = "https://overpass-api.de/api/interpreter"
    response = requests.post(url, data={"data": query})
    data = response.json()
    return data["elements"]

def seed_database():
    with app.app_context():
        db.create_all()

        # Insert manual entries first
        for p in manual_places:
            loc = Location(name=p["name"], type=p["type"], latitude=p["latitude"], longitude=p["longitude"])
            db.session.add(loc)

        # Insert OSM fetched entries
        osm_places = fetch_osm_places()
        for p in osm_places:
            name = p.get("tags", {}).get("name", "Unnamed Place")
            lat = p["lat"]
            lon = p["lon"]
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
        print(f"Seeded {len(manual_places) + len(osm_places)} locations successfully!")

if __name__ == "__main__":
    seed_database()
