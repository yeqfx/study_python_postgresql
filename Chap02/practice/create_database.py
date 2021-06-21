import psycopg2 as pg
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

CONNECT_INFO = 'host=db user=postgres password=postgres'

try:
    conn = pg.connect(CONNECT_INFO)

    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    cur = conn.cursor()

    SQL = "CREATE DATABASE community_board"
    cur.execute(SQL)

except Exception as e:
    print('postgresql database create error')
    print(e)
  
else:
    print('Database community_board created')

finally:
    if cur:
        cur.close()
    if conn:
        conn.close()