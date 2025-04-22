import sqlite3

conn = sqlite3.connect('user_account_data.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE user_data (
        username STRING PRIMARY_KEY,
        yearly_income REAL,
        account_type STRING,
        monthly_spending REAL
    )
''')
