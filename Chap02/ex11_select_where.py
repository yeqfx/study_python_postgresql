import psycopg2

CONNECT_INFO = "host=db dbname=book_store user=postgres password=postgres"
conn = psycopg2.connect(CONNECT_INFO)
cur = conn.cursor()

SQL = "SELECT * FROM develop_book WHERE book_id = 1;"
cur.execute(SQL)
print(cur.fetchall())

SQL = "SELECT * FROM develop_book WHERE book_id <> 1;"
cur.execute(SQL)
print(cur.fetchall())

SQL = "SELECT * FROM develop_book WHERE book_id > 3;"
cur.execute(SQL)
print(cur.fetchall())

cur.close()
conn.close()