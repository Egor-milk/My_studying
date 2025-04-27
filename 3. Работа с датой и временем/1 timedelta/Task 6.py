from autotest import take_input_output_values, take_all_files
from datetime import datetime, timedelta


def main(inp_values, out_values):
    for inp, out in zip(inp_values, out_values):
        print(*day_to_work(inp[0]), end=' ')
        print()
        print(*out)
        print()

def day_to_work(start_date):
    date1 = datetime.strptime(start_date, '%d.%m.%Y')
    answer = []
    plus = timedelta(days=2)
    for i in range(10):
        answer.append(datetime.strftime(date1, '%d.%m.%Y'))
        date1 = date1 + plus
        plus += timedelta(days=1)
    return answer



input_values, output_values = take_input_output_values(take_all_files())
main(input_values, output_values)


