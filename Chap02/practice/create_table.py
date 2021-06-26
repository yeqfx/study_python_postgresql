import psycopg2 as pg
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import info

MAKE_USERS_SQL = '''CREATE TABLE users (
            user_pk INTEGER,
            user_id VARCHAR(80),
            user_pw VARCHAR(12),
            register_date DATE
)''' 

MAKE_BOARD_SQL = '''CREATE TABLE board (
            board_pk INTEGER,
            board_user INTEGER,
            register_date DATE,
            title VARCHAR(30),
            description VARCHAR(3000),
            likes INTEGER,
            image_name VARCHAR(50)
)''' 

try:
    with pg.connect(info.CONNECT_INFO) as conn, conn.cursor() as cur:
        cur.execute(MAKE_USERS_SQL)
        cur.execute(MAKE_BOARD_SQL)

except Exception as e:
    print('postgresql table create error')
    print(e)
  
else:
    print('Table users, board created')

finally:
    if conn:
        conn.close()