import csv
import json


def write_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


def csv_to_json(csvFilePath):
    data1 = []
    data2 = []
    switch = False

    player_fields = ["DATASET", "GAME-ID", "DATE", "PLAYER-ID", "PLAYER FULL NAME", "POSITION", "OWN TEAM",
                     "OPPONENT TEAM", "FG", "FGA", "3P", "3PA", "FT", "FTA", "OR", "DR", "TOT", "A", "PF", "ST", "TO", "BL", "PTS"]
    team_fields = ["INITIALS", "LONG NAME",
                   "SHORT NAME", "CONFERENCE", "DIVISION"]

    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.reader(csvf)

        for row in csvReader:
            if row[0] == "NBA-2022-23-PLAYER: Table 1":
                continue
            elif row[0] == "TEAMS: Table 1":
                switch = True
                continue
            if not any(row):
                continue
            if switch:
                data2.append(dict(zip(team_fields, row)))
            else:
                data1.append(dict(zip(player_fields, row)))

    write_json(data1, 'game_stats.json')
    write_json(data2, 'teams.json')


csvFilePath = 'input.csv'
csv_to_json(csvFilePath)
