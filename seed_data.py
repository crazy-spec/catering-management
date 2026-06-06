import requests
from models import db, Location
from app import app

CENTER_LAT, CENTER_LON = 10.8283, 75.9951  # Edappal
RADIUS = 30000  # 30 km

# Queries split into chunks
queries = {
    "Villages/Towns": f"""
    [out:json][timeout:60];
    node["place"~"village|town"](around:{RADIUS},{CENTER_LAT},{CENTER_LON});
    out body;
    """,
    "Auditoriums/Halls": f"""
    [out:json][timeout:60];
    node["building"~"auditorium|hall|convention_centre"](around:{RADIUS},{CENTER_LAT},{CENTER_LON});
    out body;
    """,
    "Community Centres": f"""
    [out:json][timeout:60];
    node["amenity"~"community_centre|townhall|events_venue"](around:{RADIUS},{CENTER_LAT},{CENTER_LON});
    out body;
    """,
    "Religious Halls": f"""
    [out:json][timeout:60];
    node["building"~"mosque|church|temple"](around:{RADIUS},{CENTER_LAT},{CENTER_LON});
    out body;
    """,
    "Schools": f"""
    [out:json][timeout:60];
    node["amenity"="school"](around:{RADIUS},{CENTER_LAT},{CENTER_LON});
    out body;
    """
}

def fetch_places(query):
    url = "https://overpass-api.de/api/interpreter"
    response = requests.post(url, data={"data": query})
    if response.status_code != 200:
        print("Error from Overpass API:", response.status_code)
        return []
    try:
        data = response.json()
        return data.get("elements", [])
    except Exception as e:
        print("Failed to parse Overpass response:", e)
        print("Raw response:", response.text[:200])
        return []

def seed_database():
    with app.app_context():
        db.create_all()
        total = 0
        for category, q in queries.items():
            print(f"Fetching {category}...")
            places = fetch_places(q)
            for p in places:
                name = p.get("tags", {}).get("name", "Unnamed Place")
                lat = p["lat"]
                lon = p["lon"]
                if any(k in name.lower() for k in ["auditorium","hall","convention","centre","palace"]):
                    loc_type = "Auditorium"
                elif any(k in name.lower() for k in ["mosque","church","temple"]):
                    loc_type = "Religious Hall"
                elif "school" in name.lower():
                    loc_type = "School Auditorium"
                elif any(k in name.lower() for k in ["community","townhall","event"]):
                    loc_type = "Community Centre"
                else:
                    loc_type = "Place"
                loc = Location(name=name, type=loc_type, latitude=lat, longitude=lon)
                db.session.add(loc)
            db.session.commit()
            total += len(places)
            print(f"Seeded {len(places)} {category} entries.")
        print(f"✅ Finished seeding. Total entries added: {total}")

if __name__ == "__main__":
    seed_database()
