from autotest import take_all_files, take_input_output_values
import csv

def main(inp_values, out_values):
    for inp_value, out_value in zip (inp_values, out_values):
        print(csv_columns(inp_value))
        print(out_value, sep='\n')
        print()

def csv_columns(d_reader):
    new_dict = {}
    for row in d_reader:
        for key, value in row.items():
            new_dict[key] = new_dict.get(key, []) + [value]
    return new_dict

inp, out = (take_input_output_values(take_all_files(), csv_in=True))
main(inp, out)
#print(game(sys.stdin.read()))