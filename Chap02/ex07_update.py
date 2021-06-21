import psycopg2

CONNECT_INFO = "host=db dbname=book_store user=postgres password=postgres"
conn = psycopg2.connect(CONNECT_INFO)
cur = conn.cursor()

SQL1 = "UPDATE develop_book SET name = 'java' WHERE book_id = 2 RETURNING *;"
SQL2 = "UPDATE develop_book SET name = 'C' WHERE book_id = 5 RETURNING *;"
SQL3 = "UPDATE develop_book SET name = 'C++' WHERE book_id = 6 RETURNING *;"
SQL4 = "UPDATE develop_book SET name = 'Go' WHERE book_id = 8 RETURNING *;"
cur.execute(SQL1)
cur.execute(SQL2)
cur.execute(SQL3)
cur.execute(SQL4)
conn.commit()
print(cur.fetchall())

cur.close()
conn.close()