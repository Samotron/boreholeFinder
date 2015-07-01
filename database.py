__author__ = 'roge2582'

import sqlite3
from boreholeFinder import scraper
import csv

def databaseBuilder():
    conn = sqlite3.connect("../bgsBoreholes.db")
    scraper.bgs_scraper()
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS Boreholes ("ID" varchar(255), "BGS Reference" varchar(255));')

    f = open('../bgsBoreholes.csv')
    csv_reader = csv.reader(f, delimiter=',', quotechar='"')

    cur.executemany('INSERT OR REPLACE INTO Boreholes VALUES(?, ?)', csv_reader)
    cur.close()
    conn.commit()
    conn.close()
    f.close()



