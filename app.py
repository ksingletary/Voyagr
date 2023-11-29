"""Flask app for Voyagr"""
from flask import Flask, render_template, request, jsonify
from models import db, connect_db 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///voyagr'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.secret_key = 'not_telling_you!'

connect_db(app)

# with app.app_context():
#     db.create_all()

@app.route('/')
def home_page():
    """Home Page"""
    return render_template('home.html')