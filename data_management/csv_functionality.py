import sqlite3
import csv

#reads csv file and inserts data to end of table
def csv_to_db(csv_file):
    db = '../user_account_data.db'

    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        rows = [(row['username'], int(row['yearly_income']),
                 row['account_type'], int(row['monthly_spending'])) for row in reader]

    cursor.executemany('INSERT INTO user_data (username, yearly_income, account_type, monthly_spending) VALUES (?, ?, ?, ?)', rows)
    conn.commit()
    conn.close()

#writes database table to csv file
def db_to_csv():
    csv_file = '../user_data.csv'
    db = '../user_account_data.db'

    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM user_data')

    columns = [description[0] for description in cursor.description]

    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(columns)

        for row in cursor:
            writer.writerow(row)

    conn.close()
