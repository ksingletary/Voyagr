"""Flask app for Voyagr"""
from flask import Flask, render_template, request, session, redirect, flash
from models import db, connect_db, User, Trip, Location, Booked_Trip
from forms import UserForm, UpdatesForm, EditProfileForm, BookedTrips, PremiumBookedTrips, CancelTrip
from API_helpers import get_tokyo_pics, get_rome_pics, get_paris_pics, get_dubai_pics, get_egypt_pics
from functools import wraps
import os



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.secret_key = 'not_telling_you!'

print("DATABASE_URL:", os.environ.get('DATABASE_URL'))
connect_db(app)

with app.app_context():
    db.create_all()

@app.route('/voyagr', methods=["GET", "POST"])
def home_page():
    """Home Page"""

    form = UpdatesForm() 
    if form.validate_on_submit():
        flash('You have successfully subscribed!')                       #subscribe for updates form. won't send email, but will flash success mssg.
    descr = Trip.query.all()                                             #description for trips

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

@app.route('/voyagr/about', methods=["GET", "POST"])
def about_page():
    """About Page for Voyagr"""

    form = UpdatesForm()            #subscribe for updates form. won't send, but will flash success mssg.
    if form.validate_on_submit():
        flash('You have successfully subscribed!') 

    return render_template('about.html', form=form)

@app.route('/voyagr/destinations', methods=["GET", "POST"])
@require_login
def destinations_page():
    """Destinations showing various hotspots"""

    form = UpdatesForm()            #subscribe for updates form. won't send, but will flash success mssg.
    if form.validate_on_submit():
        flash('You have successfully subscribed!') 

    return render_template('destinations.html', form=form)


#Individual Destinations

global booked_package
booked_package = []         

@app.route('/voyagr/tokyo', methods=["GET", "POST"])
@require_login
def destinations_tokyo():
    """Individual Tokyo Destinations Page"""

    location = Location.query.get_or_404(1)
    trip = Trip.query.get_or_404(1)            
    form1 = PremiumBookedTrips()
    form = BookedTrips()

    if form.validate_on_submit() and form.date.data == '1':
        flash("You must choose a date for your trip!")
    if form.validate_on_submit() and form.date.data != '1':
        if location.city in booked_package or (location.city + 'P') in booked_package:         #if city is already in booked_package, we ensure no duplicate bookings 
            flash(f"Already booked your {location.country} trip!")
        else:
            booked_package.append(location.city)                                            #else we append to booked trip list, and db booked_trip for user
            booked_trip = Booked_Trip(cost=trip.cost, location_id=location.id, user_id=session['username'])
            db.session.add(booked_trip)
            db.session.commit()
            flash(f"Succesfully booked your {location.country} trip! View in your profile")

        return redirect('/voyagr/tokyo')
    
    return render_template('tokyo.html', form=form, form1=form1)

@app.route('/voyagr/tokyo/prem', methods=["POST"])
@require_login
def destinations_tokyo_premium():
    """Individual Tokyo Destinations Page"""

    location = Location.query.get_or_404(1)
    trip = Trip.query.get_or_404(1)            
    form = BookedTrips()
    form1 = PremiumBookedTrips()

    if form1.validate_on_submit() and form1.date.data == '1':
        flash("You must choose a date for your trip!")
    if form1.validate_on_submit() and form1.date.data != '1':
        if location.city in booked_package or (location.city + 'P') in booked_package:          
            flash(f"Already booked your {location.country} trip!")
        else:
            booked_package.append(location.city + 'P')
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

    if form.validate_on_submit() and form.date.data == '1':
        flash("You must choose a date for your trip!")
    if form.validate_on_submit() and form.date.data != '1':
        if location.city in booked_package or (location.city + 'P') in booked_package:        
            flash(f"Already booked your {location.country} trip!")
        else:
            booked_package.append(location.city)
            booked_trip = Booked_Trip(cost=trip.cost, location_id=location.id, user_id=session['username'])
            db.session.add(booked_trip)
            db.session.commit()
            flash(f"Succesfully booked your {location.country} trip! View in your profile")

        return redirect('/voyagr/rome')

    return render_template('rome.html', form=form, form1=form1)

@app.route('/voyagr/rome/prem', methods=["POST"])
@require_login
def destinations_rome_premium():
    """Individual Rome Destinations Page"""

    location = Location.query.get_or_404(2)
    trip = Trip.query.get_or_404(2)            
    form1 = PremiumBookedTrips()
    form = BookedTrips()

    if form1.validate_on_submit() and form1.date.data == '1':
        flash("You must choose a date for your trip!")
    if form1.validate_on_submit() and form1.date.data != '1':
        if location.city in booked_package or (location.city + 'P') in booked_package:         
            flash(f"Already booked your {location.country} trip!")
        else:
            booked_package.append(location.city + 'P')
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

    if form.validate_on_submit() and form.date.data == '1':
        flash("You must choose a date for your trip!")
    if form.validate_on_submit() and form.date.data != '1':
        if location.city in booked_package or (location.city + 'P') in booked_package:         
            flash(f"Already booked your {location.country} trip!")
        else:
            booked_package.append(location.city)
            booked_trip = Booked_Trip(cost=trip.cost, location_id=location.id, user_id=session['username'])
            db.session.add(booked_trip)
            db.session.commit()
            flash(f"Succesfully booked your {location.country} trip! View in your profile")

        return redirect('/voyagr/giza')


    return render_template('giza.html', form=form, form1=form1)

@app.route('/voyagr/giza/prem', methods=["POST"])
@require_login
def destinations_giza_premium():
    """Individual Giza Pyramids Destinations Page"""

    location = Location.query.get_or_404(5)
    trip = Trip.query.get_or_404(5)            
    form1 = PremiumBookedTrips()
    form = BookedTrips()

    if form1.validate_on_submit() and form1.date.data == '1':
        flash("You must choose a date for your trip!")
    if form1.validate_on_submit() and form1.date.data != '1':
        if location.city in booked_package or (location.city + 'P') in booked_package:          
            flash(f"Already booked your {location.country} trip!")
        else:
            booked_package.append(location.city + 'P')
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

    if form.validate_on_submit() and form.date.data == '1':
        flash("You must choose a date for your trip!")
    if form.validate_on_submit() and form.date.data != '1':
        if location.city in booked_package or (location.city + 'P') in booked_package:         
            flash(f"Already booked your {location.country} trip!")
        else:
            booked_package.append(location.city)
            booked_trip = Booked_Trip(cost=trip.cost, location_id=location.id, user_id=session['username'])
            db.session.add(booked_trip)
            db.session.commit()
            flash(f"Succesfully booked your {location.country} trip! View in your profile")

        return redirect('/voyagr/paris')


    return render_template('paris.html', form=form, form1=form1)

@app.route('/voyagr/paris/prem', methods=["POST"])
@require_login
def destinations_paris_premium():
    """Individual Paris Destinations Page"""

    location = Location.query.get_or_404(3)
    trip = Trip.query.get_or_404(3)            
    form1 = PremiumBookedTrips()
    form = BookedTrips()

    if form1.validate_on_submit() and form1.date.data == '1':
        flash("You must choose a date for your trip!")
    if form1.validate_on_submit() and form1.date.data != '1':
        if location.city in booked_package or (location.city + 'P') in booked_package:        
            flash(f"Already booked your {location.country} trip!")
        else:
            booked_package.append(location.city + 'P')
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

    if form.validate_on_submit() and form.date.data == '1':
        flash("You must choose a date for your trip!")
    if form.validate_on_submit() and form.date.data != '1':
        if location.city in booked_package or (location.city + 'P') in booked_package:         
            flash(f"Already booked your {location.country} trip!")
        else:
            booked_package.append(location.city)
            booked_trip = Booked_Trip(cost=trip.cost, location_id=location.id, user_id=session['username'])
            db.session.add(booked_trip)
            db.session.commit()
            flash(f"Succesfully booked your {location.country} trip! View in your profile")
        return redirect('/voyagr/dubai')

    return render_template('dubai.html', form=form, form1=form1)

@app.route('/voyagr/dubai/prem', methods=["POST"])
@require_login
def destinations_dubai_premium():
    """Individual Dubai Destinations Page"""

    location = Location.query.get_or_404(4)
    trip = Trip.query.get_or_404(4)            
    form1 = PremiumBookedTrips()
    form = BookedTrips()

    if form1.validate_on_submit() and form1.date.data == '1':
        flash("You must choose a date for your trip!")
    if form1.validate_on_submit() and form1.date.data != '1':
        if location.city in booked_package or (location.city + 'P') in booked_package:         
            flash(f"Already booked your {location.country} trip!")
        else:
            booked_package.append(location.city + 'P')
            booked_trip = Booked_Trip(cost=trip.cost, location_id=location.id, user_id=session['username'])
            db.session.add(booked_trip)
            db.session.commit()
            flash(f"Succesfully booked your {location.country} premium trip! View in your profile")
        return redirect('/voyagr/dubai')

    return render_template('dubai.html', form=form, form1=form1)

#User show route and update

@app.route('/voyagr/users/<int:user_id>', methods=["GET", "POST"])
@require_login
def user_show(user_id):
    """Show User Profile"""
    form = CancelTrip()
    user = User.query.get_or_404(user_id)
    trip = Trip.query.filter(Trip.location_id == Booked_Trip.location_id).all()

    if user.id != session['username']:
        return redirect(f"/voyagr/users/{session['username']}")         #this ensures a user can't alter url and access another user profile

    if booked_package:
        booked_trips = Booked_Trip.query.filter_by(user_id=user.id).all()

        if form.validate_on_submit():
            trip_to_cancel = form.cancel.data               #Assuming the cancellation data is same as trip data, which it is
            for booked_trip in range(len(booked_package)):
                if booked_package[booked_trip] == trip_to_cancel or booked_package[booked_trip][0:-1] == form.cancel.data:          #the [0:-1] takes into account a premium booking and removes the 'P'
                    booked_package.remove(booked_package[booked_trip])              #we must remove from booked_package and booked_trips
                    db.session.delete(booked_trips[booked_trip])
                    db.session.commit()
                    flash("Successfully canceled the trip!")
                    return redirect(f'/voyagr/users/{user.id}')
            flash("Trip not found in your bookings. No trip canceled.")
            return redirect(f'/voyagr/users/{user.id}')
        return render_template('user.html', user=user, trip=trip, booked_package=booked_package, booked_trips=booked_trips, form=form)
    
    return render_template('user.html', user=user, booked_package=booked_package, form=form)


@app.route('/voyagr/users/<int:user_id>/edit', methods=["GET", "POST"])
@require_login
def user_update(user_id):
    """Edit a User"""

    user = User.query.get_or_404(user_id)
    form = EditProfileForm(username=user.username, image_url=user.image_url)

    if form.validate_on_submit():
        user.username = form.username.data
        user.image_url = form.image_url.data or user.image_url      #if no image_url, use current image_url

        db.session.commit()
        return redirect(f"/voyagr/users/{user.id}")
    
    return render_template("user_edit.html", form=form, user=user)

#All Picture Routes for locations

@app.route('/voyagr/pics')
@require_login
def see_pics_page_tokyo():
    """Showing Pictures through API request"""

    pics = get_tokyo_pics()
    flash("*Click location to generate new batch.")

    return render_template('pictures.html', pics=pics)

@app.route('/voyagr/pics/rome')
@require_login
def see_pics_page_rome():
    """Showing Pictures through API request"""

    pics1 = get_rome_pics()
    flash("*Click location to generate new batch.")

    return render_template('pictures_rome.html', pics1=pics1)

@app.route('/voyagr/pics/paris')
@require_login
def see_pics_page_paris():
    """Showing Pictures through API request"""

    pics2 = get_paris_pics()
    flash("*Click location to generate new batch.")

    return render_template('pictures_paris.html', pics2=pics2)

@app.route('/voyagr/pics/dubai')
@require_login
def see_pics_page_dubai():
    """Showing Pictures through API request"""

    pics3 = get_dubai_pics()
    flash("*Click location to generate new batch.")

    return render_template('pictures_dubai.html', pics3=pics3)

@app.route('/voyagr/pics/egypt')
@require_login
def see_pics_page_egypt():
    """Showing Pictures through API request"""

    pics4 = get_egypt_pics()
    flash("*Click location to generate new batch.")

    return render_template('pictures_egypt.html', pics4=pics4)







