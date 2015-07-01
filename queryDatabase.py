__author__ = 'roge2582'

import sqlite3

def query_database(BGSreference):
    try:
        conn = sqlite3.connect("bgsBoreholes.db")
        cur = conn.cursor()
        id = cur.execute('SELECT ID FROM "Boreholes" WHERE "BGS Reference" = ?', BGSreference)
        id = id.fetchone()
        id = id[0]
        link = unicode("http://scans.bgs.ac.uk/sobi_scans/boreholes/") + id
        return link
    except TypeError:
        print "Reference does not exist in database"

