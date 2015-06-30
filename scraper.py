# -*- coding: utf-8 -*-
"""
Created on Fri Jun 05 12:55:50 2015

@author: roge2582
"""

# BGS Borehole URL Format http://scans.bgs.ac.uk/sobi_scans/boreholes/xxxxxx

from bs4 import BeautifulSoup
import csv
import requests
import re
import unicodedata as ud


def bgs_scraper():
    """
    Generates a list of the BGS borehole references and BGS borehole IDs
    
    """
    # Setting up csv file to work into
    f = csv.writer(open("bgsBoreholes.csv", "w"))
    f.writerow(["BGS ID", "BGS Reference"])

    # for i in xrange(1,10):
    i = 100
    data2 = []
    for i in xrange(0, i):
        try:
            linker = "http://scans.bgs.ac.uk/sobi_scans/boreholes/%d" % i
            # Link = 'http://scans.bgs.ac.uk/sobi_scans/boreholes/13207806'
            r = requests.get(linker, timeout=10)
            if r != "<Response [404]>":
                boreholeReference = BeautifulSoup(r.text)
                title = boreholeReference.title.text
                # print i, title
                if title.startswith("Page 1"):
                    list1 = [s for s in re.split("[|]", title)]
                    a = list1[1]
                    a = a.replace("Borehole", "")
                    title = a.replace(" ", "")
                # print title
                input = str(i) + ',' + title
                data2.append(input)

                # f.writerow([i, title])
            print i
        except requests.exceptions.ConnectTimeout:
            print i
            continue
    print data2
    for item in data2:
        f.writerow([item])
    return 0
