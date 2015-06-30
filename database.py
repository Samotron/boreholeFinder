__author__ = 'roge2582'

import sqlite3
from boreholeFinder import scraper
import csv

conn = sqlite3.connect("bgsBoreholes.db")
# scraper.bgs_scraper()
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS"stuff" ("one" varchar(255), "two" varchar(255));')

f = open('bgsBoreholes.csv')
csv_reader = csv.reader(f, delimiter=',')

cur.executemany('INSERT INTO stuff VALUES(?, ?)', csv_reader)
cur.close()
conn.commit()
conn.close()
f.close()


#cur.execute("CREATE TABLE t (col1, col2);")
