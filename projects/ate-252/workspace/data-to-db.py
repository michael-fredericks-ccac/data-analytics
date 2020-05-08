import sqlite3, csv





con = sqlite3.connect('crash-data.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS data''')

