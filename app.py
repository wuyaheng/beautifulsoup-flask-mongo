from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_costa

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/weather_app")


# Route to render index.html template using data from Mongo
@app.route("/")
def home():
    destination_data = mongo.db.collection.find_one()
    return render_template("index.html", vacation=destination_data)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():
    costa_data = scrape_costa.scrape_info()
    mongo.db.collection.update({}, costa_data, upsert = True) 
    return redirect("/") 


if __name__ == "__main__":
    app.run(debug=True)
