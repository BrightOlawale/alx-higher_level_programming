#!/usr/bin/python3
"""function"""
import MySQLdb
from sys import argv
import sys


def myFilter():
    """function"""
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name=%s\
                ORDER BY id ASC", (sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        if row[1] == sys.argv[4]:
            print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    myFilter()
