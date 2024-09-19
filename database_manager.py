import sqlite3


class DatabaseManager:
    def __init__(self, db_name = "fitness_app.db"):
        self.connection_string = sqlite3.connect(db_name)
        self.cursor = self.connection_string.cursor()

    def connect(self):
        """Establishes a connection to the SQL database."""
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS user(
            id INTEGER PRIMARY KEY,
            username TEXT,
            age INTEGER,
            weight REAL,
            height REAL,
            goal TEXT)''')
        self.connection_string.commit()

    def save_user_data(self):
        """Saves or updates user data in the database."""
        pass

    def retrieve_user_data(self):
        """Retrieves user data for returning users."""
        pass