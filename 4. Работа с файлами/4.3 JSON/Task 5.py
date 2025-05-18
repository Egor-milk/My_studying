from autotest import take_all_files, take_input_output_values
import json
from datetime import datetime

def main(inp_values, out_values):
    for inp_value, out_value in zip(inp_values, out_values):
        exec(inp_value)
        print(*out_value, sep='\n')
        print()

def is_correct_json(json_str):
    try:
        json.loads(json_str)
        return True
    except json.decoder.JSONDecodeError:
        return False



inp, out = (take_input_output_values(take_all_files()))
main(inp, out)
#print(game(sys.stdin.read()))