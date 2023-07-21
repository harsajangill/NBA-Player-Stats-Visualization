from flask import Flask, render_template, request
from models import Player, SessionReader
from sqlalchemy import and_

app = Flask(__name__)


def to_dict(model_instance):
    """Converts a SQLAlchemy model instance to a dictionary."""
    return {c.name: getattr(model_instance, c.name) for c in model_instance.__table__.columns}


@app.route('/')
def index():
    # Create a new Session
    session = SessionReader()

    # Query the database to fetch all Player records
    players = session.query(Player).all()

    # Render the 'index.html' template, passing the players as context
    return render_template('index.html', players=players)


@app.route('/query', methods=['GET'])
def query():
    # Fetch the parameters from the GET request
    player_id = request.args.get('player_id')

    # Create a new Session
    session = SessionReader()

    # Fetch all records for the player from the database
    player_records = session.query(Player).filter(
        Player.player_id == player_id).all()

    # Convert each Player instance to a dictionary
    player_stats = [to_dict(record) for record in player_records]

    # Render the 'player.html' template, passing the player's statistics as context
    return render_template('player.html', player_stats=player_stats)


@app.route('/search', methods=['GET'])
def search():
    # Fetch the parameters from the GET request
    team = request.args.get('team')
    player = request.args.get('player')

    # Create a new Session
    session = SessionReader()

    # Initialize a query
    query = session.query(Player.player_name, Player.player_id)

    # Filter the query based on the team and player parameters
    if team:
        query = query.filter(Player.own_team.like(f"%{team}%"))
    if player:
        query = query.filter(Player.player_name.like(f"%{player}%"))

    # Fetch all distinct player names and IDs matching the query
    player_names_ids = query.distinct().all()

    # Render the 'search.html' template, passing the players as context
    return render_template('search.html', players=player_names_ids)
