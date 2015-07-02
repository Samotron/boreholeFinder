__author__ = 'roge2582'
import queryDatabase
import webbrowser

def cli_run():
    reference = raw_input("Enter the BGS Borehole Reference?")
    reference =(reference,)
    #print reference
    link = queryDatabase.query_database(reference)
    if link == "None":
        print "No link to open! :-("
    else:
        ie = webbrowser.get(webbrowser.iexplore)
        ie.open(link)

