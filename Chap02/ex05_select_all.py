import psycopg2

CONNECT_INFO = "host=db dbname=book_store user=postgres password=postgres"
conn = psycopg2.connect(CONNECT_INFO)
cur = conn.cursor()

SQL = "SELECT * FROM develop_book;"
cur.execute(SQL)
print(cur.fetchall())

cur.close()
conn.close()