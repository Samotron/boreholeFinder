__author__ = 'roge2582'

import re

string1 = "Not Found | Borehole Logs"

if string1.startswith("Page 1"):
    list1 = [s for s in re.split("[|]", string1)]
    print list1
    a = list1[1]
    a = a.replace("Borehole","")
    a = a.replace(" ","")
    print a