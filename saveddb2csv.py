import pandas as pd
from models import Player, SessionReader

# Create a new Session
session = SessionReader()

# Query the database to fetch all Player records
players = session.query(Player).all()

# Convert the SQLAlchemy objects to dictionaries
players_dict_list = [player.__dict__ for player in players]

# Remove the '_sa_instance_state' field from each dictionary
for player_dict in players_dict_list:
    player_dict.pop('_sa_instance_state', None)

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(players_dict_list)

# Write the DataFrame to a CSV file
df.to_csv('output/players_data.csv', index=False)
