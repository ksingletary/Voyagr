"""Flask app for Voyagr"""
from flask import Flask, render_template, request, jsonify
from models import db, connect_db 
from API_helpers import get_pics, new_token

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///voyagr'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.secret_key = 'not_telling_you!'

connect_db(app)

# with app.app_context():
#     db.create_all()

# 5 destinations/ttrips  3-4 activites per destination/trip

@app.route('/')
def home_page():
    """Home Page"""
    nt = new_token()
    my_pic = get_pics()

    return render_template('home.html', my_pic=my_pic, nt=nt)