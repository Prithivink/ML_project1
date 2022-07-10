from flask import Flask

app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])

def intro():
    return("Welcome to my first Ml project")

if __name__ == "__main__":
    app.run(debug=True)