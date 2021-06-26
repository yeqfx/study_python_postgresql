import os
import psycopg2
import pandas as pd
import info

os.chdir(os.curdir + '/Chap02/practice')

usersData = pd.read_csv('user.csv', index_col=False)
usersTuple = [tuple(x) for x in usersData.to_numpy()]
usersCols = ','.join(list(usersData.columns))
# ['user_pk', 'user_id', 'user_pw', 'register_date']

boardData = pd.read_csv('post.csv')
boardTuple = [tuple(x) for x in boardData.to_numpy()]
boardCols = ','.join(list(boardData.columns))
# print(boardCols)
# print(['board_pk', 'board_user', 'register_date', 'title', 'description', 'likes', 'image_name'])


INSERT_USERS_SQL = "INSERT INTO %s (%s) VALUES (%%s, %%s, %%s, %%s)" % ('users', usersCols)
INSERT_BOARD_SQL = "INSERT INTO %s (%s) VALUES (%%s, %%s, %%s, %%s, %%s, %%s, %%s)" % ('board', boardCols)

conn = None

try:
    with psycopg2.connect(info.CONNECT_INFO) as conn, conn.cursor() as cur:
        cur.executemany(INSERT_USERS_SQL, usersTuple)
        # cur.executemany(INSERT_BOARD_SQL, boardTuple)
        conn.commit()

except Exception as e:
    print('postgresql insert data error')
    print(e)
  
else:
    print('insert data to users, board table successed')

finally:
    if conn:
        conn.close()