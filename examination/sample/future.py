import datetime
import re

print('——————未来星期几——————')
now = datetime.datetime.now()
week_day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
match = re.search(r'(\d{4}-\d{2}-\d{2})', str(now))
# print(match.groups())
date = match.group(0).split('-')

print('今天是:')
print('%s年%s月%s日 %s' % (date[0], date[1], date[2], week_day[now.weekday()]))

days = int(input('请输入未来天数:\n'))

future = now + datetime.timedelta(days=days)
match = re.search(r'(\d{4}-\d{2}-\d{2})', str(future))
future_date = match.group(0).split('-')

print('未来是:')
print('%s年%s月%s日 %s' % (future_date[0], future_date[1], future_date[2], week_day[future.weekday()]))
