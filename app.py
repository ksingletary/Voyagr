"""Flask app for Voyagr"""
from flask import Flask, render_template, request, jsonify, session, redirect, flash
from models import db, connect_db, User
from forms import UserForm, UpdatesForm, EditProfileForm
# from API_helpers import get_pics, new_token
from functools import wraps


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///voyagr'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.secret_key = 'not_telling_you!'

connect_db(app)

with app.app_context():
    db.create_all()

@app.route('/voyagr')
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
            return redirect('/voyagr/login')
        
        if route_username is not None and session_username != route_username:
            return redirect('/voyagr/login')
        
        return f(*args, **kwargs)
    return decorated_function

@app.route('/voyagr/register', methods=["GET", "POST"])
def register_user():
    form = UserForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        new_user = User.register(username, password)

        db.session.add(new_user)
        db.session.commit()
        session['username'] = new_user.id
        flash('Welcome!')
        return redirect('/voyagr')
    return render_template('register.html', form=form)

@app.route('/voyagr/login', methods=["GET", "POST"])
def login_user():
    form = UserForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.authenticate(username, password)
        if user:
            flash(f"Welcome back {user.username}!")
            session['username'] = user.id
            return redirect('/voyagr')
        else:
            form.username.errors = ['Invalid username/password']
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    """logout a user"""
    session.pop('username', None)
    return redirect('/voyagr')

@app.route('/voyagr/about')
def about_page():
    """About Page for Voyagr"""

    return render_template('about.html')

@app.route('/voyagr/destinations')
@require_login
def destinations_page():
    """Destinations showing various hotspots"""

    form = UpdatesForm()            #subscribe for updates form. won't send, but will flash success mssg.

    return render_template('destinations.html', form=form)

@app.route('/voyagr/tokyo')
@require_login
def destinations_tokyo():
    """Individual Tokyo Destinations Page"""

    return render_template('tokyo.html')

@app.route('/voyagr/rome')
@require_login
def destinations_rome():
    """Individual Rome Destinations Page"""

    return render_template('rome.html')

@app.route('/voyagr/giza')
@require_login
def destinations_giza():
    """Individual Giza Pyramids Destinations Page"""

    return render_template('giza.html')

@app.route('/voyagr/paris')
@require_login
def destinations_paris():
    """Individual Paris Destinations Page"""

    return render_template('paris.html')

@app.route('/voyagr/dubai')
@require_login
def destinations_dubai():
    """Individual Dubai Destinations Page"""

    return render_template('dubai.html')

@app.route('/voyagr/users/<int:user_id>')
@require_login
def user_show(user_id):
    """Show User Profile"""

    user = User.query.get_or_404(user_id)
    form = EditProfileForm()

    return render_template('user.html', user=user)

@app.route('/voyagr/users/<int:user_id>/edit', methods=["GET", "POST"])
@require_login
def user_edit(user_id):
    """Edit a User"""

    user = User.query.get_or_404(user_id)
    form = EditProfileForm(username=user.username, password=user.password, image_url=user.image_url)

    if form.validate_on_submit():
        # Check if password is correct
        if User.authenticate(user.username, user.password):
            user.username = form.username.data
            user.password = form.password.data
            user.image_url = form.image_url.data or user.image_url #if no image_url, use current image_url

            edited_user = User.edit(user.username, user.password)
            db.session.add(edited_user)
            db.session.commit()

            return redirect(f"/voyagr/users/{user.id}")
        else:
            flash("Invalid password, please try again.", "danger")
            return redirect(f"/voyagr/users/{user.id}/edit")
    
    return render_template("user_edit.html", form=form, user=user)





