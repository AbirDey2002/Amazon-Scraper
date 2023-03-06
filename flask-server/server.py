from flask import Flask,jsonify
from flask_cors import CORS
import pickle as pk
import amazon_model
import json

app = Flask(__name__)
cors = CORS(app)

# members api route
v = 'samsung smartwatch'

d = (amazon_model.amazon_scrape(v))

@app.route("/members")
def members():
  return d

if __name__ == "__main__":
  app.run(debug=True)