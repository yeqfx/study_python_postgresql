from psycopg2 import connect
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

conn = connect(host="db", user="postgres", password="postgres")

conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

cur = conn.cursor()

# SQL = "CREATE TABLE develop_book (book_id INTEGER, date DATE, name VARCHAR(80));"

# cur.execute(SQL)

SQL = "CREATE DATABASE book_store"

cur.execute(SQL)

cur.close()
conn.close()