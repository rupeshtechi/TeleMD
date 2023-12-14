import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, abort
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import VideoGrant

load_dotenv()
twilio_account_sid = 'AC246f9cf5aa51fbfb5639b0fbb3e761ea'
twilio_api_key_sid = 'SK44351122bc303573e6c44cb6111cb0d5'
twilio_api_key_secret = 'HX2jnMi3sLaMiXyaTrCylGjmVgZC0Hqw'

app = Flask(__name__)
 

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.get_json(force=True).get('username')
    if not username:
        abort(401)

    token = AccessToken(twilio_account_sid, twilio_api_key_sid,
                        twilio_api_key_secret, identity=username)
   
    # Set the Identity of this token
    #token.identity = username
    
    # Grant access to Video
    grant = VideoGrant()
    grant.room = 'My Room'
    token.add_grant(grant)
    #token.add_grant(VideoGrant(room='My Room'))
    #return  token.to_jwt() 
    return {'token': token.to_jwt()}



