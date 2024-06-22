#!/usr/bin/python3
"""
comment
"""
if __name__ == "__main__":
    import MySQLdb as d
    from sys import argv as a
    try:
        with d.Connect(user=a[1], passwd=a[2], db=a[3], port=3306) as db:
            with db.cursor() as cursor:
                new = a[4].replace("'", "")
                new = new.replace('"', '')
                query = """SELECT * FROM states WHERE name
                LIKE BINARY '{}' ORDER BY id""".format(new)
                cursor.execute(query)
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
    except Exception as e:
        print(e)
