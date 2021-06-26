import psycopg2
import pandas as pd
import info

with psycopg2.connect(**info.CONN_PARAMS_DIC) as conn, conn.cursor() as cur:
    SQL = "SELECT * FROM iris"
    cur.execute(SQL)
    tuples = cur.fetchall()
    cols = ["sepal_length", "sepal_width", "petal_length", "petal_width", "width"]
    irisdf = pd.DataFrame(tuples, columns=cols)
    print(irisdf)
    