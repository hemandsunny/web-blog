from sapp import app,db  # Import the db instance from your Flask app
from sapp import Post  # Import the Post model

with app.app_context():
    db.create_all()
