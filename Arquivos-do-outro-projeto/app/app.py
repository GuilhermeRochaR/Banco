from flask import Flask
from configs.extensions import db, login_manager
from models.user import User
from models.equipment import Equipment
from models.polo import Polo
from models.sector import Sector
from models.room import Room
from models.request import Request
from routes.user_routes import user_router
from routes.equipment_routes import equipment_router
from routes.sector_route import sector_router
from routes.request_routes import request_router
from routes.polos_routes import polos_router
from dotenv import load_dotenv
from datetime import timedelta
import os


load_dotenv()


def create_app():

    app = Flask(__name__)
    app.register_blueprint(equipment_router)
    app.register_blueprint(user_router)
    app.register_blueprint(sector_router)
    app.register_blueprint(request_router)
    app.register_blueprint(polos_router)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
    app.config["SECRET_KEY"] = os.getenv("FLASK_SECRET_KEY")
    app.config['REMEMBER_COOKIE_DURATION'] = timedelta(hours= 1)
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=1)
    db.init_app(app)
    login_manager.init_app(app)


    with app.app_context():
        db.create_all()
    return app


app = create_app()
app.run(debug=True)