from autotest import take_all_files, take_input_output_values
from datetime import datetime, time, timedelta

def main(inp_values, out_values):
    for inp_value, out_value in zip(inp_values, out_values):
        print(store_is_open(*inp_value))
        print(*out_value)
        print()

def store_is_open(our_date):
    work_schedule = {0: (time(9, 0), time(21, 0)),
                     1: (time(9, 0), time(21, 0)),
                     2: (time(9, 0), time(21, 0)),
                     3: (time(9, 0), time(21, 0)),
                     4: (time(9, 0), time(21, 0)),
                     5: (time(10, 0), time(18, 0)),
                     6: (time(10, 0), time(18, 0))}
    our_date = datetime.strptime(our_date, '%d.%m.%Y %H:%M')
    store_open, store_close = work_schedule[our_date.weekday()]
    if store_close > our_date.time() > store_open:
        return (datetime.combine(our_date.date(),store_close) - our_date).seconds / 60
    else:
        return 'Магазин не работает'


inp, out = (take_input_output_values(take_all_files()))
main(inp, out)