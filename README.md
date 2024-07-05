# Voyagr - Flask Travel Application 

[Voyagr Application](https://voyagr.onrender.com/voyagr)

Voyagr is a Flask web application built to show off mainly my frontend skills, as well as some backend. It features user registration and login, photos/descriptions API endpoints, booking trips, and a sleek looking design of pages for users.

I decided to delve deeper into Tailwind CSS, and design most of the application off this simple, convenient styling. To avoid a large amount of API requests (small usage quota) throughout the site without paying, I chose to employ more of a frontend, than backend, leaving booking links and photos for the bulk of API endpoints. However, most destination photos and descriptions you see on the site are peresonally plucked from the API by yours truly!

## Main Tools Used

- Flask
- Tailwind
- bcrypt
- Flask-SQLAlchemy
- Flask-WTF
- Jinja2
- WTForms

## Features

### User Features

- **User Registration and Login:** Allows users to create an account and log in.
- **Sleek Tailwind CSS Design** Design with Tailwind CSS with animations 
- **Individual activities** Users can book individual activities from link

### Other Features

- **Amadeus for Devs Photos API Endpoints:** Users can access photos from destinations through API endpoints.
- **Destinations with various activities** Users can view and book from desinations
- **About page showing fake info** An about page about Voyagr with FAQ

## User Flow

- Login and Registration (must register to view destinations and book)
- View the home page to see various destinations
- Click destinations to see available 
- Select a particular destination to see details
- About page with more about Voyagr
  

## Install

To set up this project, ensure you have Python, Flask, and PostgreSQL installed.

1. **Clone the repository.**

2. **Install Dependencies:**

pip install -r requirements.txt

3. **Set Up the Database:**

createdb voyagr

4. **Run Seed File:**
   
python3 seed.py

5. **Run the Server.**


## Tailwind Credits (thank you)

- https://tailwindcss.com/
- https://flowbite.com/
- https://youtu.be/PuovsjZN11Y?si=0WFm22fuEZfYSwuo
- https://youtu.be/UBOj6rqRUME?si=XG4XQ5x2bd157j51
- https://youtu.be/tS7upsfuxmo?si=bTBh67hrglo8vTOy
- There are more, but these are a few I learned from. Feel free to check them out :D
