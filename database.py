__author__ = 'roge2582'

import sqlite3
from scraper import bgs_scraper

def database():
    conn = sqlite3.connect(r"~\Data\aaa.db")
    cur = conn.cursor()
    bgs_scraper()
