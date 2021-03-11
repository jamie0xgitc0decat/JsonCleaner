'''
    A python3 program that can clear json file values. Reset all nested values to defined data type.
'''

import json 

json_file = ''

def nested_check(field):
    if isinstance(field, dict):
        return {key : nested_check(val) for key,val in field.items()}
    elif isinstance(field, float):
        return 0.0
    elif isinstance(field, int):
        return 0
    elif isinstance(field, list):
        return []
    elif isinstance(field, str):
        return ""
    else:
        return None
    
with open(json_file) as file:
    json_data = {key : nested_loop(val) for key,val in json.load(file).items()}

with open(json_file, 'w') as outfile:
     json.dump(json_data, outfile, sort_keys = True, indent = 4,
               ensure_ascii = False)

    
