import datetime as dt
#
# t1=datetime.timedelta(hours=1,minutes=45)
# t2=datetime.timedelta(hours=2,minutes=30)
# t3=t1+t2
# print(t3)
from datetime import datetime, date, time
timeobj = time(12, 45)
print(type(timeobj))
t1=datetime.combine(date.min, timeobj) - datetime.min
t2=dt.timedelta(hours=2,minutes=30)
t3=t1+t2
# datetime.timedelta(0, 45900)
print(t3)
print(type(t1))
