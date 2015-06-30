__author__ = 'roge2582'

import sqlite3

def database():
    conn = sqlite3.connect(r"~\Data\aaa.db")
    cur = conn.cursor()
