import sys
import psycopg2
from psycopg2 import OperationalError, errorcodes, errors
import psycopg2.extras
import pandas as pd
import info

irisData = pd.read_csv('https://github.com/Muhd-Shahid/Write-Raw-File-into-Database-Server/raw/main/iris.csv',index_col=False)

TPLS = [tuple(x) for x in irisData.to_numpy()]

COLS = ','.join(list(irisData.columns))

SQL = "INSERT INTO %s (%s) VALUES (%%s, %%s, %%s, %%s, %%s)" % ('iris', COLS)

conn = None

try:
    with psycopg2.connect(**info.CONN_PARAMS_DIC) as conn, conn.cursor() as cur:
        psycopg2.extras.execute_batch(cur, SQL, TPLS, 150)
        conn.commit()

except OperationalError as err:
    err_type, err_obj, traceback = sys.exc_info()
    line_n = traceback.tb_lineno
    print("\npsycopg2 ERROR:", err, "on line number:", line_n)
    print("psycopg2 traceback:", traceback, "-- type:", err_type)
    print("\nextensions.Diagostics:", err.diag)
    print("pgerror:", err.pgerror)
    print("pgcode:", err.pgcode, "\n")

else:
    print("Data inserted using execute_batch() successfully...")
finally:
    if conn:
        conn.close()