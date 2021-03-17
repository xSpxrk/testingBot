import sqlite3


class SQL:
    def __init__(self, database_file):
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()

    def close(self):
        self.connection.close()

    def load_file(self, file_id):
        with self.connection:
            self.cursor.execute("INSERT INTO 'Pictures' ('File_id') VALUES (?)", (file_id,))

    def get_pic(self):
        with self.connection:
            return self.cursor.execute("SELECT File_id FROM Pictures").fetchall()
