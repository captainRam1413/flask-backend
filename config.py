from datetime import timedelta
from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_jwt_extended.exceptions import NoAuthorizationError
from flask_migrate import Migrate


app = Flask(__name__)

CORS(app)


app.config['SECRET_KEY'] = ' SUPER-SECRET-KEY'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=30)

app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(hours=12)

app.config["JWT_COOKIE_SECURE"] = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)

jwt = JWTManager(app=app)



@app.errorhandler(NoAuthorizationError)
def handle_no_authorization_error(e):
    return jsonify({"msg": "Missing Authorization Header"}), 402

@jwt.unauthorized_loader
def custom_unauthorized_response(callback):
    return jsonify({"msg": "UnAuthorized Authorization Header"}), 403

@jwt.expired_token_loader
def custom_expired_token_response(jwt_header, jwt_payload):
    return jsonify({"msg": "Token has expired"}), 401

@jwt.invalid_token_loader
def custom_invalid_token_response(callback):
    return jsonify({"msg": "Invalid token"}), 422

@jwt.revoked_token_loader
def custom_revoked_token_response(jwt_header, jwt_payload):
    return jsonify({"msg": "Token has been revoked"}), 402

