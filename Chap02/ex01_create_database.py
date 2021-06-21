from mypylib.mypglib import connect_NoDB
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

conn = connect_NoDB()

conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

cur = conn.cursor()

SQL = "CREATE DATABASE book_store"

cur.execute(SQL)

cur.close()
conn.close()