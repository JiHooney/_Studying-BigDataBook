import pandas as pd
import sqlite3

#sqlite3 DB만들기
conn = sqlite3.connect( 'WebLogSQL.db' )

#sqlite3에 연결해서 테이블 만들기
cursor = conn.cursor()
cursor = conn.execute('DROP TABLE IF EXISTS access_log;')
cursor = conn.execute('CREATE TABLE IF NOT EXISTS access_log (time test, request text, status text, bytes text);')

#변수를 이용한 insert 쿼리를 만든다. 
sql_insert = 'INSERT INTO access_log VALUES (?, ?, ?, ?);'

#csv파일을 불러와서 한 줄씩 쿼리를 실행해서 데이터를 insert한다.
f = open( './access_log.csv', 'r', encoding='utf-8' )
res = 0
for row in f.readlines():
    line = row.split(',')
    line = tuple( line )
    try:
        cursor.execute( sql_insert, line )
    except:
        continue
    res += 1
print( '쿼리 입력횟수: ', res )
conn.commit()

#해당 날짜의 데이터수 조회하기
sql_select = '''
SELECT substr( time, 1, 10 ) time, count(*) count
FROM access_log
WHERE time BETWEEN '2015-05-17' AND '2015-05-20'
GROUP BY 1
ORDER BY 1;
'''
df = pd.read_sql( sql_select, conn )
print( df )

#sqlite3연결 끊기
cursor.close()