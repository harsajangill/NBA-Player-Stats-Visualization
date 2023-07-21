import pymysql

# Establish a connection to the MySQL server
connection = pymysql.connect(host='nba-player-stats.cluster-cfhz3a6zko5f.us-east-2.rds.amazonaws.com',
                             user='admin',
                             password='CW&HGnba2023')

try:
    # Create a new cursor object
    with connection.cursor() as cursor:
        # Execute the SQL command
        cursor.execute('CREATE DATABASE IF NOT EXISTS `nba_player_stats`;')

        # Commit the changes
        connection.commit()

        # Execute a new SQL command to retrieve the list of all databases
        cursor.execute('SHOW DATABASES;')

        # Fetch all the rows from the last command
        databases = cursor.fetchall()

        # Check if your database is in the list of databases
        if ('nba_player_stats',) in databases:
            print("The 'nba_player_stats' database has been created successfully.")
        else:
            print("Failed to create the 'nba_player_stats' database.")
finally:
    # Close the connection
    connection.close()
