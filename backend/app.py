from flask import Flask
from sqlalchemy import text

from config import Config
from database import db
from models import User, Product, Order, OrderItem

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return {
        "status": "success",
        "message": "ShopSphere API Running 🚀"
    }


@app.route("/health")
def health():
    return {
        "status": "UP"
    }, 200


@app.route("/ready")
def ready():
    try:
        db.session.execute(text("SELECT 1"))
        return {
            "application": "ready",
            "database": "connected"
        }, 200
    except Exception as e:
        return {
            "application": "not ready",
            "database": "disconnected",
            "error": str(e)
        }, 500


if __name__ == "__main__":
    app.run(debug=True)