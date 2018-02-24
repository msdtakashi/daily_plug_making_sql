
from datetime import datetime as dt

#集計期間のスタート
tstr = '2018-01-01'
#集計期間を回す日数
term = 10

#読み込むファイルパス
hoge = open('./Documents/python_path/test.sql','r')
query_code = hoge.readlines()

tdatetime = dt.strptime(tstr, '%Y-%m-%d')

for i in range(term):
    dd = tdatetime + datetime.timedelta(days=i)
    datesring= dd.strftime('%Y')+'-'+dd.strftime('%m')+'-'+dd.strftime('%d')
    for line in query_code:
        print(line.replace(":'target_date'", datesring),end="")
    print("\n")
