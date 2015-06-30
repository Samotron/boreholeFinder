__author__ = 'roge2582'

import sqlite3
from boreholeFinder import scraper

#conn = sqlite3.connect(r"~\Data\aaa.db")
#cur = conn.cursor()
scraper.bgs_scraper()
