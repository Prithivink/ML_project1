from flask import Flask
from Housing.Logger import logging
app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])

def intro():
    logging.info("First logging introduced")
    return("Welcome to my first Ml project")

if __name__ == "__main__":
    app.run(debug=True)