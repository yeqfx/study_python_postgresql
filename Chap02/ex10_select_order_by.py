import psycopg2

CONNECT_INFO = "host=db dbname=book_store user=postgres password=postgres"
conn = psycopg2.connect(CONNECT_INFO)
cur = conn.cursor()

SQL = "SELECT * FROM develop_book ORDER BY book_id ASC;"
cur.execute(SQL)
print(cur.fetchall())

SQL = "SELECT * FROM develop_book ORDER BY book_id DESC;"
cur.execute(SQL)
print(cur.fetchall())

SQL = "SELECT * FROM develop_book ORDER BY date, name;"
cur.execute(SQL)
print(cur.fetchall())

SQL = "SELECT date, name FROM develop_book ORDER BY 2, 1;"
cur.execute(SQL)
print(cur.fetchall())

cur.close()
conn.close()