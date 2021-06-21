import psycopg2

CONNECT_INFO = "host=db dbname=book_store user=postgres password=postgres"
conn = psycopg2.connect(CONNECT_INFO)

cur = conn.cursor()
SQL = "SELECT * from develop_book LIMIT 6 OFFSET 1;"
cur.execute(SQL)
print(cur.fetchall())

cur.close()
conn.close()