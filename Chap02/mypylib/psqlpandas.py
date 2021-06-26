import sys      # 세부적인 예외 정보를 위해
import psycopg2
from psycopg2 import OperationalError, errorcodes, errors

# psycopg2 예외 처리 함수
def show_psycopg2_exception(err):
    # 예외 세부 정보 취득
    err_type, err_obj, traceback = sys.exc_info()
    # 예외 발생 행번호
    line_n = traceback.tb_lineno
    # connect() 에러 출력
    print ("\npsycopg2 ERROR:", err, "on line number:", line_n)
    print ("psycopg2 traceback:", traceback, "-- type:", err_type)
    # psycopg2의 extensions.Diagnostics 객체 출력
    print ("\nextensions.Diagnostics:", err.diag)
    # pgcode와 pgerror 예외 출력
    print ("pgerror:", err.pgerror)
    print ("pgcode:", err.pgcode, "\n")

# PostgreSQL 서버 연결 함수
def connect(conn_params_dic):
    conn = None
    try:
        print('PostgreSQL에 접속하고 있습니다............')
        conn = psycopg2.connect(**conn_params_dic)
        print("접속 성공!!!!!")
        
    except OperationalError as err:
        # 예외 처리함수 호출
        show_psycopg2_exception(err)
        # 예외 발생시 연결을 None으로 설정
        conn = None
    
    return conn

# 데이터베이스 생성 : create_database(데이터베이스명)
def create_database(dbName):
    conn_params_dic_for_create_db = {
        "host"      : "db",
        "user"      : "postgres",
        "password"  : "postgres"
    }
    conn = connect(conn_params_dic_for_create_db)
    conn.autocommit = True
    if conn!=None:
   
        try:
            cursor = conn.cursor()
            # 데이터베이스가 이미 존재할 경우 삭제
            # cursor.execute(f'DROP DATABASE IF EXISTS {dbname};')
        
            # 데이터베이스 생성
            cursor.execute(f"CREATE DATABASE {dbName};")
            print(f"{dbName} 데이터베이스가 성공적으로 생성되었습니다!!!!!")
        
            # 커서와 접속정보 닫기
            cursor.close()
            conn.close()
            
        except OperationalError as err:
            # 예외 함수 호출
            show_psycopg2_exception(err)
            # 예외 발생시 커넥션을 None으로 설정
            conn = None

# 테이블 생성 : create_table(데이터베이스명, 테이블명, 테이블생성명령)
def create_table(dbName, tableName, sql):
    conn_params_dic = {
        "host"      : "db",
        "database"  : dbName,
        "user"      : "postgres",
        "password"  : "postgres"
    }

    conn = connect(conn_params_dic)
    conn.autocommit = True
    
    if conn!=None:
        
        try:
            cursor = conn.cursor();
            # 테이블이 이미 존재할 경우 테이블 삭제
            cursor.execute(f"DROP TABLE IF EXISTS {tableName};")
                                  
            # 테이블 생성
            cursor.execute(sql);
            print(f"{tableName} 테이블이 생성되었습니다!!!!!")
        
            # 커서와 커넥션 삭제
            cursor.close()
            conn.close()
            
        except OperationalError as err:
            # 예외 함수 호출
            show_psycopg2_exception(err)
            # 예외 발생시 커넥션을 None으로 설정
            conn = None

# cursor.executemany() 함수를 이용한 데이터프레임 입력 : 
# insert_executemany(데이버베이스명, 테이블명, 데이터프레임)
def insert_executemany(dbName, tableName, datafrm):
    conn_params_dic = {
        "host"      : "db",
        "database"  : dbName,
        "user"      : "postgres",
        "password"  : "postgres"
    }

    conn = connect(conn_params_dic)
    conn.autocommit = True
    
    if conn!=None:
        # 데이터프레임으로부터 튜플의 리스트 생성
        tpls = [tuple(x) for x in datafrm.to_numpy()]
    
        # 데이터프레임 컬럼을 문자열로 생성dataframe columns with Comma-separated
        cols = ','.join(list(datafrm.columns))
    
        # 데이터 삽입 SQL 쿼리 생성
        s = '%%s,'
        s = s * len(datafrm.columns)
        s = s[:-1]
        sql = f"INSERT INTO %s(%s) VALUES({s})" % (tableName, cols)
        cursor = conn.cursor()
        try:
            cursor.executemany(sql, tpls)
            conn.commit()
            print("executemany() 를 이용한 데이터 삽입이 성공적으로 완료되었습니다!!!!!")

            # 커서와 커넥션 삭제
            cursor.close()
            conn.close()

        except (Exception, psycopg2.DatabaseError) as err:
            # 예외처리함수 호출
            show_psycopg2_exception(err)
            cursor.close()
            conn.close()
        
# cursor.executemany() 함수를 이용한 데이터프레임 입력 : 
# insert_executemany(데이버베이스명, 테이블명, 데이터프레임)
def select_all(dbName, tableName):
    conn_params_dic = {
        "host"      : "db",
        "database"  : dbName,
        "user"      : "postgres",
        "password"  : "postgres"
    }

    conn = connect(conn_params_dic)
    conn.autocommit = True
    
    if conn!=None:
        cursor = conn.cursor()
        # 모든 데이터 보기 SQL 쿼리 생성
        sql = f"SELECT * FROM {tableName};"
        tuples = cursor.fetchall()
        print(tuples)
        cursor.close()
        conn.close()
        

    

