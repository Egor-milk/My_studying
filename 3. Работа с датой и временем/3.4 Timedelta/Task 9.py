from autotest import take_input_output_values, take_all_files
from datetime import datetime, timedelta


def main(inp_values, out_values):
    for inp, out in zip(inp_values, out_values):
        print(*rep_math(inp), sep=' ')
        print(*out)
        print()

def rep_math(lst):
    lst = [datetime.strptime(i, '%H:%M') for i in lst]
    start_lesson, end_of_day = lst[0], lst[1]
    end_lesson = start_lesson + timedelta(minutes=45)
    school_break = timedelta(minutes=10)
    answer = []
    while end_lesson <= end_of_day:
        answer.append(f'{str(start_lesson.hour).rjust(2, '0')}:{str(start_lesson.minute).rjust(2, '0')} - '
                      f'{str(end_lesson.hour).rjust(2, '0')}:{str(end_lesson.minute).rjust(2, '0')}')
        start_lesson = end_lesson + school_break
        end_lesson = start_lesson + timedelta(minutes=45)
    return answer


input_values, output_values = take_input_output_values(take_all_files())
main(input_values, output_values)


