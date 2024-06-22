#!/usr/bin/python3
"""
comment
"""
import MySQLdb as d
from sys import argv as a
try:
    with d.Connect(user=a[1], passwd=a[2], db=a[3], port=3306) as db:
        with db.cursor() as cursor:
            query = f"""SELECT c.name
            FROM cities c JOIN states s
            ON c.state_id = s.id
            WHERE s.name = '{a[4]}'
            ORDER BY c.id"""
            cursor.execute(query)
            rows = cursor.fetchall()
            strrep = ", ".join(row[0] for row in rows)
            print(strrep)
except Exception as e:
    print(e)
