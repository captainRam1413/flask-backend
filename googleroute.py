import os
import pathlib
import requests
from flask import Flask, abort, redirect, request, Blueprint, jsonify
from config import db
from flask_jwt_extended import (
    JWTManager, create_access_token, get_jwt_identity,
    jwt_required, create_refresh_token, get_jwt, set_access_cookies, unset_jwt_cookies
)
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
import google.auth.transport.requests
import logging

googleroute = Blueprint('googleroute', __name__)
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "your_jwt_secret_key"  # Change this to a strong secret key
jwt = JWTManager(app)

GOOGLE_CLIENT_ID = "297666298365-is04mt56qm1aduma1td103m5darfb0od.apps.googleusercontent.com"
client_secrets_file = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")

flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid", "https://www.googleapis.com/auth/calendar"],
    redirect_uri="https://flask-backend-7kfr.onrender.com/google/callback"
)

logging.basicConfig(level=logging.DEBUG)


@googleroute.route("/login")
def login():
    authorization_url, state = flow.authorization_url()
    return redirect(authorization_url)


@googleroute.route("/callback")
def callback():
    logging.debug('callback hit 1')
    flow.fetch_token(authorization_response=request.url)
    logging.debug('callback hit 2')
    credentials = flow.credentials

    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(session=cached_session)
    logging.debug('callback hit 3')
    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=GOOGLE_CLIENT_ID
    )

    google_id = id_info.get("sub")
    name = id_info.get("name")

    access_token = create_access_token(identity=google_id)
    refresh_token = create_refresh_token(identity=google_id)

    logging.debug(f"google_id: {google_id}")
    logging.debug(f"token: {credentials.token}")
    logging.debug(f"refresh_token: {credentials.refresh_token}")

    response = jsonify({
        "access_token": access_token,
        "refresh_token": refresh_token,
        "name": name
    })
    set_access_cookies(response, access_token)
    return response


@googleroute.route("/protected_area")
@jwt_required()
def protected_area():
    logging.debug('callback redirect hit 01')
    google_id = get_jwt_identity()
    return jsonify(logged_in_as=google_id), 200


@googleroute.route("/logout")
def logout():
    response = jsonify({"msg": "logout successful"})
    unset_jwt_cookies(response)
    return response


@googleroute.route("/")
def index():
    return "Hello World <a href='/google/login'><button>Login</button></a>"


app.register_blueprint(googleroute, url_prefix='/google')

if __name__ == "__main__":
    app.run(debug=True)
