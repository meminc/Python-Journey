import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

data_of_birt = dt.datetime(year=1995, month=10, day=16)
print(data_of_birt.weekday())