import pandas as pd
from models import Player, SessionWriter
from tqdm import tqdm


def clean_nba_data(df):
    df.columns = df.columns.str.replace('\n', ' ')
    df.columns = df.columns.str.replace(' +', ' ')
    df.columns = df.columns.str.replace(' ', '_')
    df.columns = df.columns.str.replace('__', '_')

    df = df.dropna(how='all')
    df = df.fillna(0)

    return df


if __name__ == '__main__':
    df = pd.read_csv('output/cleaned_data.csv')

    cleaned_data = clean_nba_data(df)

    print(cleaned_data.columns)

    session = SessionWriter()

    # Create a list to hold the player data dictionaries
    player_data = []

    # Iterate over the rows of the DataFrame
    for index, row in tqdm(cleaned_data.iterrows(), total=cleaned_data.shape[0]):
        player = {
            "dataset": row['BIGDATABALL_DATASET'],
            "game_id": row['GAME-ID'],
            "date": row['DATE'],
            "player_id": row['PLAYER-ID'],
            "player_name": row['PLAYER_FULL_NAME'],
            "position": row['POSITION'],
            "own_team": row['OWN_TEAM'],
            "opponent_team": row['OPPONENT_TEAM'],
            "fg": row['FG'],
            "fga": row['FGA'],
            "_3p": row['3P'],
            "_3pa": row['3PA'],
            "ft": row['FT'],
            "fta": row['FTA'],
            "or_": row['OR'],
            "dr": row['DR'],
            "tot": row['TOT'],
            "a": row['A'],
            "pf": row['PF'],
            "st": row['ST'],
            "to": row['TO'],
            "bl": row['BL'],
            "pts": row['PTS']
        }
        player_data.append(player)

    # Bulk insert player data
    session.bulk_insert_mappings(Player, player_data)
    session.commit()
