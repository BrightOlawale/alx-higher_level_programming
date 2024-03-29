#!/usr/bin/python3
"""function"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities\
    JOIN states ON cities.state_id = states.id\
    WHERE states.name = %s\
    ORDER BY cities.id ASC", (argv[4],))
    rows = cur.fetchall()
    cities_list = []
    for row in rows:
        cities_list.append(row[0])
    print(', '.join(cities_list))
    cur.close()
    db.close()
