import psycopg2
import pandas as pd

conn_params_dic = {
    "host"      : "db",
    "database"  : "irisdb",
    "user"      : "postgres",
    "password"  : "postgres"
}

conn = None

try:
    conn = psycopg2.connect(**conn_params_dic)
except Exception as e:
    print('Error : ', e)
else:
    print('Connetion successful......')
    conn.autocommit = True

if conn != None:
    try:
        cur = conn.cursor()
        cur.execute("DROP TABLE IF EXISTS iris;")
        SQL = '''CREATE TABLE iris (
            sepal_length DECIMAL(2,1) NOT NULL,
            sepal_width DECIMAL(2,1) NOT NULL,
            petal_length DECIMAL(2,1) NOT NULL,
            petal_width DECIMAL(2,1) NOT NULL,
            species CHAR(11) NOT NULL
        )'''
        cur.execute(SQL)

    except Exception as e:
        print('Error : ', e)
        conn = None
    else:
        print('iris table is created successfully .......')
    finally:
        cur.close()
        conn.close()

irisData = pd.read_csv('https://raw.githubusercontent.com/Muhd-Shahid/Learn-Python-Data-Access/main/iris.csv',index_col=False)

tpls = [tuple(x) for x in irisData.to_numpy()]
cols = ','.join(list(irisData.columns))

print(irisData.columns)
print(cols)
SQL = "INSERT INTO %s(%s) VALUES (%%s, %%s, %%s, %%s, %%s)" % ('iris', cols)
print(SQL)