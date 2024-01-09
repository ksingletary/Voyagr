"""Seed file to create Voyagr available locations, activities, descriptions, etc."""

from models import Trip, Location, Activity, db
from app import app

#Create all tables
with app.app_context():
    db.drop_all()
    db.create_all()

    japan = Location(city="Tokyo", country="Japan")
    italy = Location(city="Rome", country="Italy")
    france = Location(city="Paris", country="France")
    dubai = Location(city="Dubai", country="United Arab Emirates")
    egypt = Location(city="Greater Cairo", country="Egypt")

    activityJ1 = Activity(name="Asakusa Tour", location_id=japan.id, description="Asakusa is one of Tokyo's most favorite places among tourists. See various spots such as - River Sumida and the Kaminarimon Gate.")
    activityJ2 = Activity(name="Experience Izakaya With A Mini Food Tour", location_id=japan.id, description="Dine out in Japan's signature Izakaya eateries with a unique blend of typical bar snacks and gourmet dishes. Our local hosts will show you all their favorite places!")
    activityJ3 = Activity(name="Unguided Exploration", location_id=japan.id, description="It is your trip! You can choose to explore for yourself and visit all Tokyo has to offer.")

    activityI1 = Activity(name="City Tour", location_id=italy.id, description="Join me on an enchanting stroll through the city centre as we visit major sights that you shouldn't miss! Including the Trevi Fountain and Pantheon!")
    activityI2 = Activity(name="Designer Dinner Next to The Beautiful Castel Sant'Angelo", location_id=italy.id, description="Join the latest culinary trend of immersive and social dining where local hosts invite you into their homes for a magical meal. Dine on quintessential Italian cuisine paired with delicious wines and digestifs chosen by your host.")
    activityI3 = Activity(name="Eat, pray, love in Rome", location_id=italy.id, description="Discover Rome as Julia Roberts did in the movie Eat Pray Love. We will walk through the city, exploring the famous places where the movie was developed.")

    activityF1 = Activity(name="Giverny", location_id=france.id, description="Take a half-day tour outside of Paris to Giverny, the former home of the Impressionist master Claude Monet.")
    activityF2 = Activity(name="Wine Making Workshop", location_id=france.id, description="Learn how to make wine at an historical 18th-century wine cellar in central Paris, and discover the former haunt of the French royals.")
    activityF3 = Activity(name="Minibus Tour", location_id=france.id, description="See the sights of Paris from the comfort of a minibus on a small group tour of the city center. Drive through beautiful neighborhoods like the Marais and more.")

    activityD1 = Activity(name="Helicopter Tour", location_id=dubai.id, description="Embark on a flight over Dubai, a complete and unforgettable experience that will make you discover the city from a different angle!")
    activityD2 = Activity(name="Birthday Everyday-Celebrate every day in life", location_id=dubai.id, description="Join the latest culinary trend of immersive and social dining where local hosts invite you into their homes for a magical meal.")
    activityD3 = Activity(name="Free Exploration", location_id=dubai.id, description="It is your trip to explore! You can choose to explore for yourself and visit all Tokyo has to offer.")

    activityE1 = Activity(name="Pyramid Tour", location_id=egypt.id, description="Take a guided tour of the Pyramid of Khufu and walk around the complexes. Tour guides will inform you of historical facts, scary mummy stories, and more...")
    activityE2 = Activity(name="Camel Ride", location_id=egypt.id, description="In the desert landscape of Egypt, there is only one way for a tourist to travel in style! You can ride a camel around and feel like a character in the movie Hump.")
    activityE3 = Activity(name="The Great Sphinx of Giza", location_id=egypt.id, description="One of the worlds greatest wonders, the sphynx is truly a sight to behold.")

    db.session.add_all([japan, italy, france, dubai, egypt, activityJ1,activityJ2,activityJ3,activityI1,activityI2,activityI3,activityF1,activityF2,activityF3,activityD1,activityD2,activityD3,activityE1,activityE2,activityE3])
    db.session.commit()

    japan_trip = Trip(location_id=japan.id, description="From the serene temples of Kyoto, adorned with vermillion gates and delicate gardens, to the bustling streets of Tokyo, pulsating with neon lights and modernity, Japan unfolds as a captivating fusion of old-world charm and progressive dynamism.", photo="https://screen-api.vizeater.co/files/1279075/-/preview/-/progressive/yes/-/format/jpeg/image.jpg", cost="895", activity_link="https://www.guruwalk.com/walks/35338-free-tour-asakusa-tokyo?ref=ojlgpuf3oo1nuk2s74m5", activity_link1="https://vizeater.co/events/22537?utm_source=amadeus-1381", activity_link2="https://www.japan-guide.com/e/e2164.html")
    italy_trip = Trip(location_id=italy.id, description="The streets tell stories of emperors, artists, and visionaries, while its vibrant piazzas buzz with the energy of bustling cafes and the aroma of Italian cuisine. Rome ignites the soul with its rich history and divine artistry.", photo="https://d1i21eq0w7p1n3.cloudfront.net/ycys9zafo9n80o9ywn234lvb5zwh", cost="700", activity_link="https://www.guruwalk.com/walks/36295-the-very-best-of-rome?ref=ojlgpuf3oo1nuk2s74m5", activity_link1="https://vizeater.co/events/26503?utm_source=amadeus-1381", activity_link2="https://www.guruwalk.com/walks/37247-eat-pray-love-in-rome?ref=ojlgpuf3oo1nuk2s74m5")
    france_trip = Trip(location_id=france.id, description="Paris, the City of Light, exudes an unmatched aura of romance, art, and sophistication. Nestled along the banks of the Seine River, this cosmopolitan capital mesmerizes visitors with its iconic landmarks, centuries-old history, and unparalleled cultural offerings.", photo="https://cdn.getyourguide.com/img/tour/5e299611d771e.jpeg/21.jpg", cost="750", activity_link="http://www.partner.viator.com/en/13257/tours/Paris/Giverny-Private-Tour-Monets-House-and-Garden/d479-19551P58?eap=prod-fxUokaxbikskDHdLPsA3-13257&aid=vba13257en", activity_link1="http://www.partner.viator.com/en/13257/tours/Paris/Winemaking-Workshop-in-Paris/d479-23034P2?eap=prod-fxUokaxbikskDHdLPsA3-13257&aid=vba13257en", activity_link2="http://www.partner.viator.com/en/13257/tours/Paris/Paris-by-Night-Sightseeing-Tour-1h45/d479-9511P39?eap=prod-fTVMRKnO6VYgWu4FKDT7-13257&aid=vba13257en")
    dubai_trip = Trip(location_id=dubai.id, description="Dubai, a glittering jewel amidst the Arabian Desert, is a city of opulence, innovation, and limitless possibilities. Its futuristic skyline, punctuated by towering skyscrapers and architectural wonders, showcases the pinnacle of modern engineering and design.",  photo="https://www.helipass.com/uploads/media/default/0001/04/60f9893e34ccc-img-723-jpeg.jpeg", cost="950", activity_link="https://www.helipass.com/en/touristic-helicopter-flights/1/exclusive-flights-dubai-12.html", activity_link1="https://vizeater.co/events/53795?utm_source=amadeus-1381", activity_link2="https://www.visitdubai.com/en/explore-dubai")
    egypt_trip = Trip(location_id=egypt.id, description="The Giza Pyramids, an enduring testament to ancient Egypt's glory, rise majestically from the golden sands near Cairo. These awe-inspiring structures, including the iconic Great Pyramid of Khufu, mesmerize with their sheer size and enigmatic allure.", photo="https://d1i21eq0w7p1n3.cloudfront.net/rwqgsgwh1tuwuf0li44qguxpc4bs", cost="779", activity_link="https://www.guruwalk.com/walks/37850-giza-pyramids-sphinx-walking-tour?ref=ojlgpuf3oo1nuk2s74m5", activity_link1="https://www.guruwalk.com/walks/38032-giza-pyramids-sphinx-camel-s-horse-s-atv?ref=ojlgpuf3oo1nuk2s74m5", activity_link2="https://www.guruwalk.com/walks/38032-giza-pyramids-sphinx-camel-s-horse-s-atv?ref=ojlgpuf3oo1nuk2s74m5")

    db.session.add_all([japan_trip, italy_trip, france_trip, dubai_trip, egypt_trip])
    db.session.commit()

