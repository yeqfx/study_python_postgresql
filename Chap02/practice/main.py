import psycopg2 as pg

try:
    CONNECT_INFO = 'host=db dbname=postgres user=postgres password=postgres'
    with pg.connect(CONNECT_INFO) as conn:
        with conn.cursor() as cur:
            
