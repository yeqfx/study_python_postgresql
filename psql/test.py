# import unittest
import os
import psql
import pandas as pd

# class TestPsql(unittest.TestCase):
#     def setUp():
#         pass

if __name__ == "__main__":
    # unittest.main()

    os.chdir(os.curdir + '/psql')

    dbName = 'testdb1'
    db = psql.Database()
    # db.create(dbName)
    # db.dblist()
    # db.delete(dbName)
    

    table = psql.Table(dbName)

    # tableName = 'testtable1'
    # sql = f"CREATE TABLE {tableName} (book_id INTEGER, date DATE, name VARCHAR(80));"
    # table.create(tableName, sql)

    # tableName = 'users'
    # sql = '''CREATE TABLE users (
    #     user_pk INTEGER,
    #     user_id VARCHAR(80),
    #     user_pw VARCHAR(12),
    #     register_date DATE
    # )''' 
    # table.create(tableName, sql)

    # tableName = 'board'
    # sql = '''CREATE TABLE board (
    #     board_pk INTEGER,
    #     board_user INTEGER,
    #     register_date DATE,
    #     title VARCHAR(30),
    #     description VARCHAR(3000),
    #     likes INTEGER,
    #     image_name VARCHAR(50)
    # )''' 
    # table.create(tableName, sql)
 
    # tableName = 'users'
    # table.delete(tableName)
    
    # tableName = 'board'
    # table.delete(tableName)

    # tableName = 'users'
    # df = pd.read_csv('user.csv',index_col=False)
    # table.insertMany(tableName, df)

    # tableName = 'users'
    # table.selectAll(tableName)

    tableName = 'board'
    df = pd.read_csv('post.csv',index_col=False)
    table.insertMany(tableName, df)

    tableName = 'board'
    data = table.selectAll(tableName)