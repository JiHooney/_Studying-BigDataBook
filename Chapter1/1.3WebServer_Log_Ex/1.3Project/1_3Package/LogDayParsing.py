import pandas as pd

#파일 불러오기, 날짜를 datetime형식으로 가져온다.
df1 = pd.read_csv( 'access_log.csv', parse_dates=['time'] )

#시간을 인덱스로 지정한다.
df2 = df1.set_index( 'time' )

#인덱스에 의한 시간을 필터링한다. 2015.05.17 ~2015.05.19
df3 = df2.loc['2015-05-17':'2015-05-19']

#1일분의 액세스 수를 카운트한다.
print( df3.resample( '1d' ).size() )