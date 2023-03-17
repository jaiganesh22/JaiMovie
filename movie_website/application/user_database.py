import sqlite3
from sqlite3 import Error
from datetime import datetime

FILE = "users.db"
USER_TABLE = "Usertable"

class User_db:
    def __init__(self):
        self.conn = None
        try:
            self.conn = sqlite3.connect(FILE)
        except Error as e:
            print(e)

        self.cursor = self.conn.cursor()
        self._initialize_tables()
        
    def _initialize_tables(self):
        query = f"""Create Table if not exists {USER_TABLE} (id Integer Primary Key Autoincrement, 
                    name Text, username Text, email Text, password Text, plan Text)"""
        self.cursor.execute(query)
        self.conn.commit()
        
    def register_user(self, name, username, email, password, plan):
        query = f"""Insert into {USER_TABLE} VALUES(?, ?, ?, ?, ?, ?)"""
        self.cursor.execute(query, (None, name, username, email, password, plan,))
        self.conn.commit()
        
    def check_user(self, username):
        query = f"""Select * from {USER_TABLE} Where username = ?"""
        self.cursor.execute(query, (username,))
        user = self.cursor.fetchone()
        if(user): 
            return True
        return False
    
    def get_user(self, username):
        query = f"""Select * from {USER_TABLE} Where username = ?"""
        self.cursor.execute(query, (username,))
        user = self.cursor.fetchone()
        user_dict = {"id": user[0], "name": user[1], "username": user[2], "email": user[3],
                        "password": user[4], "plan": user[5]}
        return user_dict
        