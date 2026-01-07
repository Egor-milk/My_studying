import calendar


number_of_month = input()
try:
    number_of_month = int(number_of_month)
except ValueError:
    print('Введено некорректное значение')
else:
    if 0 < number_of_month < 13:
        print(calendar.month_name[number_of_month])
    else:
        print('Введено число из недопустимого диапазона')
