import sqlite3

class Database:
    """ Connect to db """
    def __init__(self, database_file):
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()
    
    def add_user(self, user_id, status = True):
        with self.connection:
            return self.cursor.execute("INSERT INTO 'subs' ('user_id', 'status') VALUES (?,?)", (user_id, status))
    
    def change_status(self, user_id, status):
        with self.connection:
            return self.cursor.execute("UPDATE subs SET 'status' = ? WHERE user_id = ?", (status, user_id))
    
    def check_user(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM 'subs' WHERE user_id = ?", (user_id,)).fetchall()
            return bool(len(result))
    
    def active_users(self, status = True):
        with self.connection:
            users = self.cursor.execute(
                "SELECT user_id FROM 'subs' WHERE status = ?", (status,)).fetchall()
            return users
    
    def close(self):
        self.connection.commit()
