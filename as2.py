#days btw two dates

from dateline import date
date1=date(2018,12,10)
date2=date(2019,01,01)
delta=date2-date1
print(delta.days)