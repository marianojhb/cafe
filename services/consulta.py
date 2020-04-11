import sqlite3
from pprint import pprint


def return_data_from_database():
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    response = cursor.execute("SELECT * FROM services_service")
    rows = response.fetchall()
    conn.close()
    return rows