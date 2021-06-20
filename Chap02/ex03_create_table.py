import psycopg2

CONNECT_INFO = "host=db dbname=book_store user=postgres password=postgres"

conn = psycopg2.connect(CONNECT_INFO)
cur = conn.cursor()

SQL = "CREATE TABLE develop_book (book_id INTEGER, date DATE, name VARCHAR(80));"

cur.execute(SQL)

SQL = "SELECT * FROM information_schema.tables WHERE table_schema = 'public' ORDER BY table_name;"

cur.execute(SQL)

conn.commit()
print(cur.fetchall())

cur.close()
conn.close()