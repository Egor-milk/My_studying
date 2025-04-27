from autotest import take_input_output_values, take_all_files
from datetime import datetime, timedelta


def main(inp_values, out_values):
    for inp, out in zip(inp_values, out_values):
        exec(inp)
        print(*out)
        print()

def is_available_date(booked_dates, date_for_booking):
    def lets_format_date(dates):
        new_dates = []
        for i in dates:
            if len(i.split('-')) == 2:
                start, end = datetime.strptime(i.split('-')[0], '%d.%m.%Y'), datetime.strptime(i.split('-')[1], '%d.%m.%Y')
                while start <= end:
                    new_dates.append(start)
                    start += timedelta(days=1)
            else:
                new_dates.append(datetime.strptime(i, '%d.%m.%Y'))
        return new_dates
    booked_dates = lets_format_date(booked_dates)
    date_for_booking = lets_format_date([date_for_booking])
    return all(map(lambda x: True if x not in booked_dates else False, date_for_booking))

input_values, output_values = take_input_output_values(take_all_files())
main(input_values, output_values)


