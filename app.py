"""Flask app for Voyagr"""
from flask import Flask, render_template, request, session, redirect, flash
from models import db, connect_db, User, Trip, Location,  Activity, Booked_Trip
from forms import UserForm, UpdatesForm, EditProfileForm, BookedTrips, PremiumBookedTrips, CancelTrip
from API_helpers import get_tokyo_pics, get_rome_pics, get_paris_pics, get_dubai_pics, get_egypt_pics
from functools import wraps


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://wnmanvsrpaymnk:828bbcd9ed2a85e432dc72bc2fe5909c732ce0a320266c826f0dcb117c1c9a92@ec2-44-215-40-87.compute-1.amazonaws.com:5432/d4v5hovun8m6b2'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///voyagr'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.secret_key = 'not_telling_you!'

connect_db(app)

with app.app_context():
    db.create_all()

@app.route('/voyagr')
def home_page():
    """Home Page"""

    form = UpdatesForm()
    descr = Trip.query.all()          #subscribe for updates form. won't send, but will flash success mssg.

    return render_template('home.html', form=form, descr=descr)

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
    """Registration form"""

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
    """Login User"""

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


#Individual Destinations

global booked_package
booked_package = set()          #set so there's no duplicate bookings
canceled_package = set()        #recording of canceled trip for user

@app.route('/voyagr/tokyo', methods=["GET", "POST"])
@require_login
def destinations_tokyo():
    """Individual Tokyo Destinations Page"""

    location = Location.query.get_or_404(1)
    trip = Trip.query.get_or_404(1)            
    
    form1 = PremiumBookedTrips()
    form = BookedTrips()
    if form.validate_on_submit():
        if form.booking.data:
            if location.city in booked_package:         #if city is already in booked_package 
                print("Already in booked_package so we print this!")
            else:
                booked_package.add(location.city)
                booked_trip = Booked_Trip(cost=trip.cost, location_id=location.id, user_id=session['username'])
                db.session.add(booked_trip)
                db.session.commit()
                flash(f"Succesfully booked your {location.country} trip! View in your profile")

        return redirect('/voyagr/tokyo')
    
    return render_template('tokyo.html', form=form, form1=form1)

@app.route('/voyagr/tokyo/prem', methods=["POST"])
@require_login
def destinations_tokyo_p():
    """Individual Tokyo Destinations Page"""

    location = Location.query.get_or_404(1)
    trip = Trip.query.get_or_404(1)            

    form = BookedTrips()
    form1 = PremiumBookedTrips()
    if form1.validate_on_submit():
        if form1.premium_booking.data:
            if location.city in booked_package:
                print("Already in booked_package so we print this!")
            else:
                booked_package.add(f"{location.city}P")
                booked_trip = Booked_Trip(cost=trip.cost, location_id=location.id, user_id=session['username'])
                db.session.add(booked_trip)
                db.session.commit()
                flash(f"Succesfully booked your {location.country} premium trip! View in your profile")
        
        return redirect('/voyagr/tokyo')
    
    return render_template('tokyo.html', form1=form1, form=form)

@app.route('/voyagr/rome', methods=["GET", "POST"])
@require_login
def destinations_rome():
    """Individual Rome Destinations Page"""

    location = Location.query.get_or_404(2)
    trip = Trip.query.get_or_404(2)            
    
    form1 = PremiumBookedTrips()
    form = BookedTrips()
    if form.validate_on_submit():
        if form.booking.data:
            if location.city in booked_package:
                print("Already booked!")
            else:
                booked_package.add(location.city)
                booked_trip = Booked_Trip(cost=trip.cost, location_id=location.id, user_id=session['username'])
                db.session.add(booked_trip)
                db.session.commit()
                flash(f"Succesfully booked your {location.country} trip! View in your profile")

        return redirect('/voyagr/rome')

    return render_template('rome.html', form=form, form1=form1)

@app.route('/voyagr/rome/prem', methods=["POST"])
@require_login
def destinations_rome_p():
    """Individual Rome Destinations Page"""

    location = Location.query.get_or_404(2)
    trip = Trip.query.get_or_404(2)            
    
    form1 = PremiumBookedTrips()
    form = BookedTrips()
    if form1.validate_on_submit():
        if form1.premium_booking.data:
            if location.city in booked_package:
                flash("Already booked!")
            else:
                booked_package.add(f"{location.city}P")
                booked_trip = Booked_Trip(cost=trip.cost, location_id=location.id, user_id=session['username'])
                db.session.add(booked_trip)
                db.session.commit()
                flash(f"Succesfully booked your {location.country} premium trip! View in your profile")

        return redirect('/voyagr/rome')

    return render_template('rome.html', form=form, form1=form1)

@app.route('/voyagr/giza', methods=["GET", "POST"])
@require_login
def destinations_giza():
    """Individual Giza Pyramids Destinations Page"""

    location = Location.query.get_or_404(5)
    trip = Trip.query.get_or_404(5)            
    
    form1 = PremiumBookedTrips()
    form = BookedTrips()
    if form.validate_on_submit():
        if form.booking.data:
            if location.city in booked_package:
                print("Already booked!")
            else:
                booked_package.add(location.city)
                booked_trip = Booked_Trip(cost=trip.cost, location_id=location.id, user_id=session['username'])
                db.session.add(booked_trip)
                db.session.commit()
                flash(f"Succesfully booked your {location.country} trip! View in your profile")

        return redirect('/voyagr/giza')


    return render_template('giza.html', form=form, form1=form1)

@app.route('/voyagr/giza/prem', methods=["POST"])
@require_login
def destinations_giza_p():
    """Individual Giza Pyramids Destinations Page"""

    location = Location.query.get_or_404(5)
    trip = Trip.query.get_or_404(5)            
    
    form1 = PremiumBookedTrips()
    form = BookedTrips()
    if form1.validate_on_submit():
        if form1.premium_booking.data:
            if location.city in booked_package:
                print("Already booked!")
            else:
                booked_package.add(f"{location.city}P")
                booked_trip = Booked_Trip(cost=trip.cost, location_id=location.id, user_id=session['username'])
                db.session.add(booked_trip)
                db.session.commit()
                flash(f"Succesfully booked your {location.country} premium trip! View in your profile")

        return redirect('/voyagr/giza')


    return render_template('giza.html', form=form, form1=form1)

@app.route('/voyagr/paris', methods=["GET", "POST"])
@require_login
def destinations_paris():
    """Individual Paris Destinations Page"""

    location = Location.query.get_or_404(3)
    trip = Trip.query.get_or_404(3)            
    
    form1 = PremiumBookedTrips()
    form = BookedTrips()
    if form.validate_on_submit():
        if form.booking.data:
            if location.city in booked_package:
                print("Already booked!")
            else:
                booked_package.add(location.city)
                booked_trip = Booked_Trip(cost=trip.cost, location_id=location.id, user_id=session['username'])
                db.session.add(booked_trip)
                db.session.commit()
                flash(f"Succesfully booked your {location.country} trip! View in your profile")

        return redirect('/voyagr/paris')


    return render_template('paris.html', form=form, form1=form1)

@app.route('/voyagr/paris/prem', methods=["POST"])
@require_login
def destinations_paris_p():
    """Individual Paris Destinations Page"""

    location = Location.query.get_or_404(3)
    trip = Trip.query.get_or_404(3)            
    
    form1 = PremiumBookedTrips()
    form = BookedTrips()
    if form1.validate_on_submit():
        if form1.premium_booking.data:
            if location.city in booked_package:
                print("Already booked!")
            else:
                booked_package.add(f"{location.city}P")
                booked_trip = Booked_Trip(cost=trip.cost, location_id=location.id, user_id=session['username'])
                db.session.add(booked_trip)
                db.session.commit()
                flash(f"Succesfully booked your {location.country} premium trip! View in your profile")

        return redirect('/voyagr/paris')


    return render_template('paris.html', form=form, form1=form1)

@app.route('/voyagr/dubai', methods=["GET", "POST"])
@require_login
def destinations_dubai():
    """Individual Dubai Destinations Page"""

    location = Location.query.get_or_404(4)
    trip = Trip.query.get_or_404(4)            
    
    form1 = PremiumBookedTrips()
    form = BookedTrips()
    if form.validate_on_submit():
        if form.booking.data:
            if location.city in booked_package:
                print("Already booked!")
            else:
                booked_package.add(location.city)
                booked_trip = Booked_Trip(cost=trip.cost, location_id=location.id, user_id=session['username'])
                db.session.add(booked_trip)
                db.session.commit()
                flash(f"Succesfully booked your {location.country} trip! View in your profile")

        return redirect('/voyagr/dubai')

    return render_template('dubai.html', form=form, form1=form1)

@app.route('/voyagr/dubai/prem', methods=["POST"])
@require_login
def destinations_dubai_p():
    """Individual Dubai Destinations Page"""

    location = Location.query.get_or_404(4)
    trip = Trip.query.get_or_404(4)            
    
    form1 = PremiumBookedTrips()
    form = BookedTrips()
    if form1.validate_on_submit():
        if form1.premium_booking.data:
            if location.city in booked_package:
                print("Already booked!")
            else:
                booked_package.add(f"{location.city}P")
                booked_trip = Booked_Trip(cost=trip.cost, location_id=location.id, user_id=session['username'])
                db.session.add(booked_trip)
                db.session.commit()
                flash(f"Succesfully booked your {location.country} premium trip! View in your profile")

        return redirect('/voyagr/dubai')

    return render_template('dubai.html', form=form, form1=form1)

@app.route('/voyagr/users/<int:user_id>', methods=["GET", "POST"])
@require_login
def user_show(user_id):
    """Show User Profile"""

    user = User.query.get_or_404(user_id)
    if booked_package:
        booked_trips = Booked_Trip.query.filter(Booked_Trip.user_id == user.id).all()           #call booked_trips for respective user id bookings
        new_booked_packaged = list(booked_package)

        # call trip where location id is equal to bookedtrip location id            
        trip = Trip.query.filter(Trip.location_id == Booked_Trip.location_id).all()
        activities = Activity.query.all()
        form = CancelTrip()
        if form.validate_on_submit():
            canceled_package.add("Trip[x] Canceled")
            flash("We have successfully canceled your trip! It may still appear in your profile, but it has been recorded!")
            return redirect(f'/voyagr/users/{user.id}')
        
        return render_template('user.html', user=user, trip=trip, booked_package=booked_package, booked_trips=booked_trips, activities=activities, new_booked_packaged=new_booked_packaged, form=form)
    
    if user.id != session['username']:
        return redirect(f"/voyagr/users/{session['username']}")

    
    return render_template('user.html', user=user, booked_package=booked_package)


@app.route('/voyagr/users/<int:user_id>/edit', methods=["GET", "POST"])
@require_login
def user_update(user_id):
    """Edit a User"""

    user = User.query.get_or_404(user_id)
    form = EditProfileForm(username=user.username, image_url=user.image_url)

    if form.validate_on_submit():
        user.username = form.username.data
        user.image_url = form.image_url.data or user.image_url #if no image_url, use current image_url

        db.session.commit()
        return redirect(f"/voyagr/users/{user.id}")
    
    return render_template("user_edit.html", form=form, user=user)

@app.route('/voyagr/pics')
@require_login
def see_pics_page_tokyo():
    """Showing Pictures through API request"""

    pics = get_tokyo_pics()
    flash("*Click location to generate new batch. Paris and Rome might not appear. Voyagr appreciates your cooperation while we fix the issue.")

    return render_template('pictures.html', pics=pics)

@app.route('/voyagr/pics/rome')
@require_login
def see_pics_page_rome():
    """Showing Pictures through API request"""

    pics1 = get_rome_pics()
    flash("*Click location to generate new batch. Paris and Rome might not appear. Voyagr appreciates your cooperation while we fix the issue.")

    return render_template('pictures_rome.html', pics1=pics1)

@app.route('/voyagr/pics/paris')
@require_login
def see_pics_page_paris():
    """Showing Pictures through API request"""

    pics2 = get_paris_pics()
    flash("*Click location to generate new batch. Paris and Rome might not appear. Voyagr appreciates your cooperation while we fix the issue.")

    return render_template('pictures_paris.html', pics2=pics2)

@app.route('/voyagr/pics/dubai')
@require_login
def see_pics_page_dubai():
    """Showing Pictures through API request"""

    pics3 = get_dubai_pics()
    flash("*Click location to generate new batch. Paris and Rome might not appear. Voyagr appreciates your cooperation while we fix the issue.")

    return render_template('pictures_dubai.html', pics3=pics3)

@app.route('/voyagr/pics/egypt')
@require_login
def see_pics_page_egypt():
    """Showing Pictures through API request"""

    pics4 = get_egypt_pics()
    flash("*Click location to generate new batch. Paris and Rome might not appear. Voyagr appreciates your cooperation while we fix the issue.")

    return render_template('pictures_egypt.html', pics4=pics4)







