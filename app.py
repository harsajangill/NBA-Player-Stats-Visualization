from flask import Flask, render_template
from models import Player, SessionReader

app = Flask(__name__)


@app.route('/')
def index():
    # Create a new Session
    session = SessionReader()

    # Query the database to fetch all Player records
    players = session.query(Player).all()

    # Render the 'index.html' template, passing the players as context
    return render_template('index.html', players=players)
