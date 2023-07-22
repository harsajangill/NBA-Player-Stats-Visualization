from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from models import Player, SessionReader
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
import pandas as pd

# BIG Data Group 4 - Christian Wierzbicki and Harsajan Gill Authors
# NBA Stats Dashboard and Data Exploration App
# Big Data Analytics techniques employed

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Query the database to fetch all Player records
with SessionReader() as session:
    players = session.query(Player).all()

# Mapping from column name to full name
stat_full_name = {
    'pts': 'Points',
    'a': 'Assists',
    'tot': 'Rebounds',
}

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("NBA Statistics - Big Data Group 4 Project",
                    className='text-center my-3')
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.Label('Select Player:'),
            dcc.Dropdown(
                id='player-selector',
                options=[
                    {'label': player.player_name, 'value': player.player_id} for player in players],
                value=players[0].player_id
            )
        ], width=4),
        dbc.Col([
            html.Label('Select Statistic(s):'),
            dcc.Checklist(
                id='stat-selector',
                options=[
                    {'label': 'Points', 'value': 'pts'},
                    {'label': 'Assists', 'value': 'a'},
                    {'label': 'Rebounds', 'value': 'tot'},
                    # Add more options as needed
                ],
                value=['pts']
            )
        ], width=4),
        dbc.Col([
            html.Label('Moving Average Window:'),
            dcc.Input(
                id='moving-average-window',
                type='number',
                min=1,
                max=30,
                step=1,
                value=5,
                style={'width': '100%'}
            )
        ], width=4),
    ], className='my-3'),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='player-stats-graph')
        ]),
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='player-team-stats-graph')
        ]),
    ])
], fluid=True)


@app.callback(
    Output('player-stats-graph', 'figure'),
    [Input('player-selector', 'value'),
     Input('stat-selector', 'value'),
     Input('moving-average-window', 'value')]
)
def update_stats_graph(player_id, stats, moving_average_window):
    if not stats:
        return go.Figure()

    # Fetch all records for the player from the database
    with SessionReader() as session:
        player_records = session.query(Player).filter(
            Player.player_id == player_id).all()

    # Convert the player records to a DataFrame
    df = pd.DataFrame([player.__dict__ for player in player_records])

    # Sort the DataFrame by date
    df = df.sort_values('date')

    # Initialize figure
    fig = go.Figure()

    for stat in stats:
        # Calculate the moving average
        df[f'{stat}_ma'] = df[stat].rolling(
            window=moving_average_window).mean()

        # Create a line plot of the player's selected stat and its moving average over time
        fig.add_trace(go.Scatter(x=df['date'], y=df[stat],
                                 mode='markers',
                                 name=f'{stat_full_name.get(stat, stat)}'))

        fig.add_trace(go.Scatter(x=df['date'], y=df[f'{stat}_ma'],
                                 mode='lines',
                                 name=f'{stat_full_name.get(stat, stat)} Moving Average'))

    # Update layout
    fig.update_layout(title='Player Statistics Over Time',
                      xaxis_title='Date',
                      yaxis_title='Value')

    return fig


@app.callback(
    Output('player-team-stats-graph', 'figure'),
    [Input('player-selector', 'value'),
     Input('stat-selector', 'value')]
)
def update_team_stats_graph(player_id, stats):
    if not stats:
        return go.Figure()

    # Fetch all records for the player from the database
    with SessionReader() as session:
        player_records = session.query(Player).filter(
            Player.player_id == player_id).all()

    # Convert the player records to a DataFrame
    df = pd.DataFrame([player.__dict__ for player in player_records])

    # Initialize figure
    fig = go.Figure()

    for stat in stats:
        # Group the data by opponent team and calculate the mean of the selected statistic
        df_team_avg = df.groupby('opponent_team')[stat].mean().reset_index()

        # Create a bar plot of the player's average statistic for each team
        fig.add_trace(go.Bar(x=df_team_avg['opponent_team'], y=df_team_avg[stat],
                             name=f'{stat_full_name.get(stat, stat)}'))

    # Update layout
    fig.update_layout(title='Average Player Statistics by Team',
                      xaxis_title='Team',
                      yaxis_title='Average Value',
                      barmode='group')

    return fig


if __name__ == '__main__':
    app.run_server()
    server = app.server
