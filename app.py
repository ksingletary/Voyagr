"""Flask app for Voyagr"""
from flask import Flask, render_template, request, jsonify, session, redirect, flash
from models import db, connect_db, User
from forms import UserForm, UpdatesForm
# from API_helpers import get_pics, new_token
from functools import wraps


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///voyagr'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.secret_key = 'not_telling_you!'

connect_db(app)

# with app.app_context():
#     db.create_all()

# 5 destinations/ttrips  3-4 activites per destination/trip

# @app.route('/')
# def home_page():
#     """Home Page"""
#     nt = new_token()
#     my_pic = get_pics()     #also storing descriptions in this tuple


#     return render_template('home.html', my_pic=my_pic, nt=nt)
@app.route('/')
def home_page():
    """Home Page"""
    form = UpdatesForm()            #subscribe for updates form. won't send, but will flash success mssg.

    return render_template('home.html', form=form)

def require_login(f):
    """wrapper function to require login"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        
        session_username = session.get('username')
        route_username = kwargs.get('username', None)

        if session_username is None:
            return redirect('/login')
        
        if route_username is not None and session_username != route_username:
            return redirect('/login')
        
        return f(*args, **kwargs)
    return decorated_function

@app.route('/register', methods=["GET", "POST"])
def register_user():
    form = UserForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        new_user = User.register(username, password)

        db.session.add(new_user)
        db.session.commit()
        session['user_id'] = new_user.id
        flash('Welcome!')
        return redirect('/')
    return render_template('register.html', form=form)

@app.route('/login', methods=["GET", "POST"])
def login_user():
    form = UserForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.authenticate(username, password)
        if user:
            flash(f"Welcome back {user.username}")
            session['user_id'] = user.id
            return redirect('/')
        else:
            form.username.errors = ['Invalid username/password']
    return render_template('login.html', form=form)

