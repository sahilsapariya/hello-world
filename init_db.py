import sqlite3

DATABASE_NAME = "db.db"
SCHEMA_FILE = "schema.sql"


def get_database_conn():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn



def create_database():
    connection = sqlite3.connect(DATABASE_NAME)

    with open(SCHEMA_FILE) as f:
        query = f.read()
        connection.executescript(query)
    
    connection.close()


if __name__ == "__main__":
    create_database()