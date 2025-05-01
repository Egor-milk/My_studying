from time import strftime
from turtledemo.clock import current_day

from autotest import take_all_files, take_input_output_values
from datetime import datetime, time, timedelta

def main(inp_values, out_values):
    for inp_value, out_value in zip(inp_values, out_values):
        print(days_before_the_course_release(inp_value[0]))
        print(*out_value)
        print()

def days_before_the_course_release(our_date):
    format_to_print = {'days': ['день', 'дня', 'дней'],
                       'hours': ['час', 'часа', 'часов'],
                       'minutes': ['минута', 'минуты', 'минут'],}
    course_release_date = datetime(2022, 11, 8, 12, 0)
    current_date = datetime.strptime(our_date, '%d.%m.%Y %H:%M')
    if current_date >= course_release_date:
        return 'Курс уже вышел!'
    else:
        time_to_course_release = course_release_date - current_date
        minute, seconds = divmod(time_to_course_release.seconds, 60)
        hour, minute = divmod(minute, 60)
        if time_to_course_release.days == 0:
            if hour == 0:
                return f'До выхода курса осталось: {minute} {choose_plural(minute, format_to_print['minutes'])}'
            elif minute == 0:
                return f'До выхода курса осталось: {hour} {choose_plural(hour, format_to_print['hours'])}'

            else:
                return (f'До выхода курса осталось: {hour} {choose_plural(hour, format_to_print['hours'])} и '
                        f'{minute} {choose_plural(minute, format_to_print['minutes'])}')
        else:
            if hour == 0:
                return (f'До выхода курса осталось: {time_to_course_release.days} '
                        f'{choose_plural(time_to_course_release.days, format_to_print['days'])}')
            else:
                return (f'До выхода курса осталось: {time_to_course_release.days} '
                        f'{choose_plural(time_to_course_release.days, format_to_print['days'])} '
                        f'и {hour} {choose_plural(hour, format_to_print['hours'])}')


def choose_plural(amount, declension): # []/я/ей
    amount = str(amount)
    if int(amount[-2:]) in range(11, 15) or int(amount[-1:]) in list(range(5, 11)) + [0]:
        form = declension[2]
    elif int(amount[-1:]) == 1:
        form = declension[0]
    else:
        form = declension[1]
    return form

inp, out = (take_input_output_values(take_all_files()))
main(inp, out)