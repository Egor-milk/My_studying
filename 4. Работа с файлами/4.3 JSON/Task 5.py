from autotest import take_all_files, take_input_output_values
import json
from datetime import datetime
import sys

def main(inp_values, out_values):
    for inp_value, out_value in zip(inp_values, out_values):
        print(*return_json_string(inp_value), sep='\n')
        print()
        print(*out_value, sep='\n')
        print('\n')

def return_json_string(json_str):
    answer = []
    for key, value in json.loads(json_str).items():
        if type(value) == list:
            value = ', '.join([str(i) for i in value])
        answer.append(f'{key}: {value}')
    return answer


inp, out = (take_input_output_values(take_all_files()))
#print(return_json_string(sys.stdin))
main(inp, out)
#print(game(sys.stdin.read()))