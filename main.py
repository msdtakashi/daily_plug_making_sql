import datetime
from datetime import datetime as dt

tstr = '2016-07-21'
tdatetime = dt.strptime(tstr, '%Y-%m-%d')
for i in range(11):
    dd = tdatetime + datetime.timedelta(days=i)s
    print("""
    select 
        uid
    from
    　intemidate.unique_user
    where log_date = """,end='')
    print("'"+dd.strftime('%Y')+"-"+dd.strftime('%m')+"-"+dd.strftime('%d')+"'")