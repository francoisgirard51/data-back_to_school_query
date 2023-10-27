""" This return a list of students from a specific city
"""
# pylint:disable=C0111,C0103

import sqlite3

conn = sqlite3.connect('data/school.sqlite')
cursor = conn.cursor()

def students_from_city(db_cursor, city):
    """return a list of students from a specific city"""
    db_cursor.execute("SELECT first_name, last_name FROM students WHERE birth_city = ?", (city,))
    return [f"{row[0]} {row[1]}" for row in db_cursor.fetchall()]

print(students_from_city(cursor, 'Paris'))
