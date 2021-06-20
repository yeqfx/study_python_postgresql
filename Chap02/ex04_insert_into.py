import psycopg2

CONNECT_INFO = "host=db dbname=book_store user=postgres password=postgres"
conn = psycopg2.connect(CONNECT_INFO)

cur = conn.cursor()

SQL = "INSERT INTO develop_book VALUES (%s, %s, %s);"
BOOK_ID = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
DATE = ['2019-12-17', '2019-12-25', '2020-01-03', '2020-01-24', '2020-02-04', '2020-02-15', '2020-03-10', '2020-04-01', '2020-04-07', '2020-04-17']
NAME = ['맛있는 MongoDB', '''자바''', 'HTML/CSS', 'Python', 'C언어', 'C++언어', 'mySQL', 'Go언어', 'PHP', 'Ruby']

for i in range(len(BOOK_ID)):
    cur.execute(SQL, (BOOK_ID[i], DATE[i], NAME[i],))

conn.commit()
# cur.execute("INSERT INTO develop_book VALUES(1, '2019-12-17', '맛있는 MongoDB');")

cur.execute("SELECT * FROM develop_book;")
print(cur.fetchall())
cur.close()
conn.close()