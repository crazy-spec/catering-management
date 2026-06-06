import requests
from models import db, Location
from app import app

CENTER_LAT, CENTER_LON = 10.8283, 75.9951  # Edappal
RADIUS = 30000  # 30 km

# Start with villages only
queries = {
    "Villages": f"""
    [out:json][timeout:60];
    node["place"="village"](around:{RADIUS},{CENTER_LAT},{CENTER_LON});
    out body;
    """
}

def fetch_places(query):
    # Use a more reliable Overpass mirror
    url = "https://overpass.kumi.systems/api/interpreter"
    response = requests.post(url, data={"data": query})
    print("Status:", response.status_code)
    if response.status_code != 200:
        print("Error from Overpass API:", response.text[:200])
        return []
    try:
        data = response.json()
        return data.get("elements", [])
    except Exception as e:
        print("Failed to parse:", e)
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
                loc = Location(name=name, type=category, latitude=lat, longitude=lon)
                db.session.add(loc)
            db.session.commit()
            total += len(places)
            print(f"Seeded {len(places)} {category} entries.")
        print(f"✅ Finished seeding. Total entries added: {total}")

if __name__ == "__main__":
    seed_database()
