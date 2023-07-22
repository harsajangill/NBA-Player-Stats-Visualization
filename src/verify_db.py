import pymysql

# Establish a connection to the MySQL server
connection = pymysql.connect(host='nba-player-stats.cluster-ro-cfhz3a6zko5f.us-east-2.rds.amazonaws.com',
                             user='admin',
                             password='CW&HGnba2023')

try:
    # Create a new cursor object
    with connection.cursor() as cursor:
        # Execute the SQL command to check if the database exists
        cursor.execute(
            "SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = 'nba_player_stats'")
        result = cursor.fetchone()

        if result is None:
            print("Database does not exist.")
        else:
            print("Database exists.")

        # Now check if the table exists
        cursor.execute(
            "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'nba_player_stats' AND TABLE_NAME = 'players'")
        result = cursor.fetchone()

        if result is None:
            print("Table does not exist.")
        else:
            print("Table exists.")

finally:
    # Close the connection
    connection.close()
