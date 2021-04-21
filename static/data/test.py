import sqlite3
from sqlite3 import Error
import pandas as pd


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        c = conn.cursor()
        print(sqlite3.version)
        c.execute('''CREATE TABLE players (PLAYER_NAME text, TEAM_ID text, PLAYER_ID text, SEASON int)''')
        players = pd.read_csv('players.csv')
        players.to_sql('players', conn, if_exists='append', index=False)

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    create_connection(r"nba_test.db")
