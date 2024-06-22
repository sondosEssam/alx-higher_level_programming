#!/usr/bin/python3
"""
comment
"""
import MySQLdb
import sys 
try:
    with MySQLdb.Connect(user=sys.argv[1],passwd=sys.argv[2], db=sys.argv[3], port=3306) as db:
        with db.cursor() as cursor:
            query="SELECT * FROM states ORDER BY id ASC;"
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
except Exception as e:
    print(e)
