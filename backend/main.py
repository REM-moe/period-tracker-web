from flask import Flask
from flask_restx import Api
from dbmodels import Journal, Userdata, Userdates 
from exts import db
from flask_jwt_extended import JWTManager

from auth import auth_ns
from getdates import date_ns
from journal import journal_ns


def create_app(config):
    app = Flask(__name__)

    app.config.from_object(config)
    api = Api(app, doc= '/docs')
    db.init_app(app)
    JWTManager(app)

    api.add_namespace(auth_ns)
    api.add_namespace(date_ns)
    api.add_namespace(journal_ns)

    @app.shell_context_processor
    def make_shell_context():
        return{
            "db":db,
            "Journal": Journal,
            "Userates": Userdates,
            "Userdata":Userdata
        }
    
    return app
