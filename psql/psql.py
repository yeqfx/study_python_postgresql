import sys
from typing import final      # 세부적인 예외 정보를 위해
import psycopg2
from psycopg2 import OperationalError, errorcodes, errors

class Database:
    def __init__(self):
        self.conn_params_dic = {
            "host"      : "db",
            "user"      : "postgres",
            "password"  : "postgres"
        }
        print("Postgresql 접속 준비를 마쳤습니다...")

    def create(self, dbName):
        conn = self.connect(self.conn_params_dic)
        conn.autocommit = True
        if conn!=None:
            try:
                cursor = conn.cursor()
                # 데이터베이스 생성
                cursor.execute(f"CREATE DATABASE {dbName};")
                
            except OperationalError as err:
                # 예외 함수 호출
                self.show_psycopg2_exception(err)
                # 예외 발생시 커넥션을 None으로 설정
                conn = None

            else:
                print(f"{dbName} 데이터베이스가 성공적으로 생성되었습니다!!!!!")

            finally:
                # 커서와 접속정보 닫기
                cursor.close()
                conn.close()

    def dblist(self):
        """데이터베이스 리스트 보여주기"""
        conn = self.connect(self.conn_params_dic)
        conn.autocommit = True
        if conn!=None:
            try:
                cursor = conn.cursor()
                sql = 'SELECT datname FROM pg_database'
                cursor.execute(sql)
                
            except OperationalError as err:
                # 예외 함수 호출
                self.show_psycopg2_exception(err)
                # 예외 발생시 커넥션을 None으로 설정
                conn = None

            else:
                print("데이터베이스 목록입니다.")
                print(cursor.fetchall())

            finally:
                # 커서와 접속정보 닫기
                cursor.close()
                conn.close()

    # 데이터베이스 삭제
    def delete(self, dbName):
        """데이터베이스 삭제하기"""
        conn = self.connect(self.conn_params_dic)
        conn.autocommit = True
        if conn!=None:
            try:
                cursor = conn.cursor()
                sql = f'DROP DATABASE {dbName}'
                cursor.execute(sql)
                
            except OperationalError as err:
                # 예외 함수 호출
                self.show_psycopg2_exception(err)
                # 예외 발생시 커넥션을 None으로 설정
                conn = None

            else:
                print(f"{dbName} 데이터베이스를 삭제하였습니다.")

            finally:
                # 커서와 접속정보 닫기
                cursor.close()
                conn.close()

    # psycopg2 예외 처리 함수
    def show_psycopg2_exception(self, err):
        # 예외 세부 정보 취득
        # err_type, err_obj, traceback = sys.exc_info()
        err_type, _, traceback = sys.exc_info()
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
    def connect(self, conn_params_dic):
        conn = None
        # print(self.conn)
        try:
            print('PostgreSQL에 접속하고 있습니다............')
            conn = psycopg2.connect(**conn_params_dic)
            # print(self.conn)
            print("접속 성공!!!!!")
            
        except OperationalError as err:
            # 예외 처리함수 호출
            self.show_psycopg2_exception(err)
            # 예외 발생시 연결을 None으로 설정
            conn = None
        
        return conn


class Table(Database):
    def __init__(self, dbName):
        self.dbName = dbName
        super(Table, self).__init__()
        self.conn_params_dic["database"] = self.dbName

    def create(self, tableName, sql):        
        conn = self.connect(self.conn_params_dic)
        conn.autocommit = True
        if conn!=None:
            try:
                # 테이블이 이미 존재할 경우 테이블 삭제
                # cursor.execute(f"DROP TABLE IF EXISTS {tableName};")
                                  
                cursor = conn.cursor()
                # 테이블 생성
                cursor.execute(sql)
                print(f"{tableName} 테이블이 생성되었습니다!!!!!")
                
            except OperationalError as err:
                # 예외 함수 호출
                self.show_psycopg2_exception(err)
                # 예외 발생시 커넥션을 None으로 설정
                conn = None

            else:
                print(f"{tableName} 테이블이 성공적으로 생성되었습니다!!!!!")

            finally:
                # 커서와 접속정보 닫기
                cursor.close()
                conn.close()

    def tablelist(self, tableName='*'):
        """데이터베이스 리스트 보여주기"""
        conn = self.connect(self.conn_params_dic)
        conn.autocommit = True
        if conn!=None:
            try:
                cursor = conn.cursor()
                sql = f'SELECT schemaname, tablename FROM pg_tables'
                cursor.execute(sql)
                
            except OperationalError as err:
                # 예외 함수 호출
                self.show_psycopg2_exception(err)
                # 예외 발생시 커넥션을 None으로 설정
                conn = None

            else:
                print("테이블 목록입니다.")
                print(cursor.fetchall())

            finally:
                # 커서와 접속정보 닫기
                cursor.close()
                conn.close()

    # cursor.executemany() 함수를 이용한 데이터프레임 입력 : 
    # insert_executemany(데이버베이스명, 테이블명, 데이터프레임)
    def insertMany(self, tableName, datafrm):

        conn = self.connect(self.conn_params_dic)
        conn.autocommit = True
        
        if conn!=None:

            try:
                # 데이터프레임으로부터 튜플의 리스트 생성
                datafrm = datafrm.where(datafrm.notnull(), None)
                tpls = [tuple(x) for x in datafrm.to_numpy()]
            
                # 데이터프레임 컬럼을 문자열로 생성dataframe columns with Comma-separated
                cols = ','.join(list(datafrm.columns))
            
                # 데이터 삽입 SQL 쿼리 생성
                s = '%%s,'
                s = s * len(datafrm.columns)
                s = s[:-1]
                sql = f"INSERT INTO %s(%s) VALUES({s})" % (tableName, cols)

                print('---------------------------')
                print(s)
                print(cols)
                print(len(datafrm.columns))
                print(sql)
                print(tpls)
                print('---------------------------')

                cursor = conn.cursor()
                cursor.executemany(sql, tpls)

            except (Exception, psycopg2.DatabaseError) as err:
                # 예외처리함수 호출
                self.show_psycopg2_exception(err)
                # 예외 발생시 커넥션을 None으로 설정
                conn = None

            else:
                print(f"{tableName} 테이블에 데이터가 입력되었습니다.")

            finally:
                # 커서와 커넥션 삭제
                cursor.close()
                conn.close()

    # 테이블로부터 모든 데이터 추출
    def selectAll(self, tableName):

        conn = self.connect(self.conn_params_dic)
        conn.autocommit = True
        
        if conn!=None:

            try:
                sql = f"SELECT * FROM {tableName}"
                cursor = conn.cursor()
                cursor.execute(sql)

            except (Exception, psycopg2.DatabaseError) as err:
                # 예외처리함수 호출
                self.show_psycopg2_exception(err)
                
            else:
                print(f"{tableName} 테이블의 데이터 목록입니다.")
                data = cursor.fetchall()
                print(data)
                return data

            finally:
                # 커서와 커넥션 삭제
                cursor.close()
                conn.close()

    # 테이블 삭제
    def delete(self, tableName):
        """테이블 삭제하기"""
        conn = self.connect(self.conn_params_dic)
        conn.autocommit = True
        if conn!=None:
            try:
                cursor = conn.cursor()
                sql = f'DROP TABLE {tableName}'
                cursor.execute(sql)
                
            except OperationalError as err:
                # 예외 함수 호출
                self.show_psycopg2_exception(err)
                # 예외 발생시 커넥션을 None으로 설정
                conn = None

            else:
                print(f"{tableName} 테이블을 삭제하였습니다.")

            finally:
                # 커서와 접속정보 닫기
                cursor.close()
                conn.close()

    # 테이블로부터 모든 데이터 삭제
    def deleteAll(self, tableName):

        conn = self.connect(self.conn_params_dic)
        conn.autocommit = True
        
        if conn!=None:

            try:
                sql = f"DELETE FROM {tableName}"
                cursor = conn.cursor()
                cursor.execute(sql)

            except (Exception, psycopg2.DatabaseError) as err:
                # 예외처리함수 호출
                self.show_psycopg2_exception(err)
                
            else:
                print(f"{tableName} 테이블의 데이터가 모두 삭제되었습니다.")
                try:
                    cursor.fetchall()
                except (Exception, psycopg2.ProgrammingError) as err:
                    print(f'{tableName}에 데이터가 없습니다.')


            finally:
                # 커서와 커넥션 삭제
                cursor.close()
                conn.close()