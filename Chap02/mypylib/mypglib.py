import psycopg2 as pg

def connect_NoDB():
    CONNECT_INFO = 'host=db user=postgres password=postgres'
    return pg.connect(CONNECT_INFO)

def connect_Postgres():
    CONNECT_INFO = 'host=db dbname=postgres user=postgres password=postgres'
    conn = pg.connect(CONNECT_INFO)
    return conn.cursor()

def connect_book_store():
    CONNECT_INFO = 'host=db dbname=book_store user=postgres password=postgres'
    conn = pg.connect(CONNECT_INFO)
    return conn.cursor()

