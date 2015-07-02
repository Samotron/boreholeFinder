__author__ = 'roge2582'

import argparse
import database
import cli_file


def main():
    parser = argparse.ArgumentParser(description="Open BGS logs from its reference (avoiding Geoindex!)")
    g = parser.add_mutually_exclusive_group()
    g.add_argument('-d' '--database', type=str, help="Builds the database! !!!WARNING!!! Takes ages")
    g.add_argument('-b' '--borehole', type=str, help="Enter your reference to open the log")

    if len(sys.argv) == 1:
        parser.print_help()
        return

    args = parser.parse_args()

    # Build database
    if args.database:
        database.databaseBuilder()
        return

    # Query Database
    if args.borehole:
        cli_file.cli_run()
        return
