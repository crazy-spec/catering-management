from app import app
from models import db, Location

with app.app_context():
    print("Total entries:", Location.query.count())
    for loc in Location.query.limit(20).all():
        print(loc.name, loc.type, loc.latitude, loc.longitude)
