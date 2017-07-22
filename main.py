tstr = '2016-07-01'
tdatetime = dt.strptime(tstr, '%Y-%m-%d')
for i in range(60):
    dd = tdatetime + datetime.timedelta(days=i)
    print(dd.strftime('%Y')+'-'+dd.strftime('%m')+'-'+dd.strftime('%d'))
