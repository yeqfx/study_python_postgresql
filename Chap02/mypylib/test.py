import psqlpandas as pp

# pp.create_database('testdb')

sql = '''CREATE TABLE testtable (
    user_pk INTEGER,
    user_id VARCHAR(80),
    user_pw VARCHAR(12),
    register_date DATE
)'''
pp.create_table('testdb', 'testtable', sql)



