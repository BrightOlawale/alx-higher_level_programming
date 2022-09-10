#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect('localhost', argv[1], argv[2], argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    the_row = cur.fetchall()

    for row in the_row:
        print(row)
    cur.close()
    db.close()
