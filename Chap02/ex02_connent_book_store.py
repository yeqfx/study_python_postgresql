from psycopg2 import connect

CONNECT_INFO = "host=db dbname=book_store user=postgres password=postgres"

conn = connect(CONNECT_INFO)

cur = conn.cursor()

cur.close()
conn.close()