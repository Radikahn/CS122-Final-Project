import sqlite3


class UserDataTable:

    def __init__(self):
        self.conn = sqlite3.connect('user_account_data.db')

        self.cursor = self.conn.cursor()

        self.cursor.execute('''
            CREATE TABLE user_data (
                username STRING PRIMARY_KEY,
                yearly_income REAL,
                account_type STRING,
                monthly_spending REAL
            )
        ''')
