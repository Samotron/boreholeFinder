# -*- coding: utf-8 -*-
"""
Created on Fri Jun 05 12:55:50 2015

@author: roge2582
"""

# BGS Borehole URL Format http://scans.bgs.ac.uk/sobi_scans/boreholes/xxxxxx

from bs4 import BeautifulSoup 
import csv
import requests

# Setting up csv file to work into
#f = csv.writer(open("bgsBoreholes.csv", "w"))
#f.writerow(["BGS ID", "BGS Reference"])

#for i in xrange(1,10):
for i in xrange(0,1):
    #Link = "http://scans.bgs.ac.uk/sobi_scans/boreholes/%d" %i    
    Link = 'http://scans.bgs.ac.uk/sobi_scans/boreholes/13207806'   
    r = requests.get(Link, timeout = 1)
    boreholeReference = BeautifulSoup(r.text)
    title = boreholeReference.title.text
    #f.writerow(i , title)
    print title
