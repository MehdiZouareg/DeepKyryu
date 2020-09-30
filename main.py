from flask import Flask
from flaskwebgui import FlaskUI #get the FlaskUI class
from flask import render_template

app = Flask(__name__)

# Feed it the flask app instance 
ui = FlaskUI(app)

# do your logic as usual in Flask
@app.route("/")
def index():
  return render_template("index.html")


# call the 'run' method
ui.run()