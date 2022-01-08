import datetime
week_day_dict = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday',
}
print('今天是:')
today = datetime.datetime.today()
print('%d年%d月%d日 %s' % (today.year, today.month, today.day, week_day_dict.get(today.weekday())))
days = int(input('请输入未来天数:\n'))
future = today + datetime.timedelta(days=days)
print('未来是：')
print('%d年%d月%d日 %s' % (future.year, future.month, future.day,week_day_dict.get(future.weekday())))

