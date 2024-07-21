from flask import Blueprint,jsonify,request
import logging
from models2 import ConToUser, Consultant,ConPswd, User
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, create_refresh_token # type: ignore
from config import db
from googleapiclient.discovery import build_from_document, build

from oauth2client.client import OAuth2WebServerFlow
from flask import redirect, url_for, session, request, jsonify
from google.oauth2 import credentials
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
import os
import pickle

CLIENT_ID = "1032598425328-eqbc8sab7j52jpfqeuvor2433ti88a4t.apps.googleusercontent.com"
CLIENT_SECRET = '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'

googleroute = Blueprint('googleroute',__name__)
logging.basicConfig(level=logging.DEBUG)

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

# Replace with your Google Cloud project details
CLIENT_SECRETS_FILE = "client_secret_1032598425328-eqbc8sab7j52jpfqeuvor2433ti88a4t.apps.googleusercontent.com.json"
SCOPES = ['https://www.googleapis.com/auth/calendar']

# Route to initiate OAuth flow
# @googleroute.route('/get-authorize',methods=['GET'])
# def authorize():
#     flow = OAuth2WebServerFlow(client_id=CLIENT_ID,
#     client_secret=CLIENT_SECRET,
#     scope='https://www.googleapis.com/auth/calendar',
#     redirect_uri='http://localhost:5000/google/oauth2callback',
#     approval_prompt='force',
#     access_type='offline')

#     auth_uri = flow.step1_get_authorize_url()
#     # return redirect(auth_uri)
#     return jsonify(
#         {
#             "authorization_url":auth_uri
#         },200
#     )
    

# # OAuth2 callback route
# @googleroute.route('/oauth2callback',methods=['GET'])
# def oauth2callback():
#     code = request.args.get('code')
#     if code:
#     # exchange the authorization code for user credentials
#         flow = OAuth2WebServerFlow(CLIENT_ID,
#         CLIENT_SECRET,
#         "https://www.googleapis.com/auth/calendar")
#         flow.redirect_uri = request.base_url
#         try:
#           credentials = flow.step2_exchange(code)
#         except Exception as e:
#           print(f"Unable to get an access token because {e.message}")

#         # store these credentials for the current user in the session
#         # This stores them in a cookie, which is insecure. Update this
#         # with something better if you deploy to production land
#         session['credentials'] = credentials

#     return jsonify(
#         {
#             "meassage":"success"
#         },200
#     )

# # Fetch and display calendar events
# @googleroute.route('/calendar/events', methods=['GET'])
# @jwt_required()
# def calendar_events():
#     if 'credentials' not in session:
#         return jsonify({"msg": "No credentials in session"}), 401

#     credentials = google.oauth2.credentials.Credentials(
#         **session['credentials']
#     )
#     service = build('calendar', 'v3', credentials=credentials)

#     events_result = service.events().list(calendarId='primary', maxResults=10).execute()
#     events = events_result.get('items', [])

#     session['credentials'] = credentials_to_dict(credentials)
#     return jsonify(events), 200

# # Schedule a new event
# @googleroute.route('/calendar/events/create', methods=['POST'])
# @jwt_required()
# def create_event():
#     if 'credentials' not in session:
#         return jsonify({"msg": "No credentials in session"}), 401

#     event_data = request.json
#     credentials = google.oauth2.credentials.Credentials(
#         **session['credentials']
#     )
#     service = build('calendar', 'v3', credentials=credentials)

#     event = service.events().insert(calendarId='primary', body=event_data).execute()

#     session['credentials'] = credentials_to_dict(credentials)
#     return jsonify(event), 200

# def credentials_to_dict(credentials):
#     return {
#         'token': credentials.token,
#         'refresh_token': credentials.refresh_token,
#         'token_uri': credentials.token_uri,
#         'client_id': credentials.client_id,
#         'client_secret': credentials.client_secret,
#         'scopes': credentials.scopes
#     }

flow = Flow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES, redirect_uri='http://localhost:5000/oauth2callback')

@googleroute.route('/')
def index():
    if 'credentials' not in session:
        return redirect('authorize')
    credentials = pickle.loads(session['credentials'])
    service = build('calendar', 'v3', credentials=credentials)
    events_result = service.events().list(calendarId='primary', maxResults=10, singleEvents=True, orderBy='startTime').execute()
    events = events_result.get('items', [])
    return jsonify(events)

@googleroute.route('/authorize')
def authorize():
    authorization_url, state = flow.authorization_url(prompt='consent')
    session['state'] = state
    return redirect(authorization_url)

@googleroute.route('/oauth2callback')
def oauth2callback():
    flow.fetch_token(authorization_response=request.url)
    if not flow.credentials:
        return 'Error: Could not get credentials'
    session['credentials'] = pickle.dumps(flow.credentials)
    return redirect(url_for('index'))

@googleroute.route('/logout')
def logout():
    session.pop('credentials', None)
    return redirect(url_for('index'))