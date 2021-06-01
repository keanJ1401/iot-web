import psycopg2

conn = psycopg2.connect("dbname=SmartHome user=postgres password=user", host = "127.0.0.1", port = "5432")

cur = conn.cursor()
cur.execute('SELECT * FROM DEVICES;')

rows = cur.fetchall()

print(rows)

conn.close()