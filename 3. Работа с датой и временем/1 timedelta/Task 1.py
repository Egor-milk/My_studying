#Дополните приведенный ниже код, чтобы он прибавил к объекту datetime(2021, 11, 4, 13, 6)
# одну неделю и 12 часов и вывел результат в формате DD.MM.YYYY HH:MM:SS.

from datetime import datetime, timedelta

dt = datetime(2021, 11, 4, 13, 6) + timedelta(weeks=1, hours=12)

print(datetime.strftime(dt,'%d.%m.%Y %H:%M:%S'))


#Дополните приведенный ниже код, чтобы он вывел количество дней (целое число) между датами today и birthday.

from datetime import date, timedelta

today = date(2021, 11, 4)
birthday = date(2022, 10, 6)

days = today - birthday

print(days)


