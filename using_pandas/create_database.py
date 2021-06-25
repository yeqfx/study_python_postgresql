import psycopg2

conn_params_dic = {
    "host"      : "db",
    "user"      : "postgres",
    "password"  : "postgres"
}

conn = psycopg2.connect(**conn_params_dic)

conn.autocommit = True

if conn != None:
    try:
        cur = conn.cursor()
        cur.execute("DROP DATABASE IF EXISTS irisdb;")
        cur.execute("CREATE DATABASE irisdb;")
    except Exception as e:
        print('Error : ', e)
    else:
        print('irisdb database is created successfully .......')
    finally:
        cur.close()
        conn.close()