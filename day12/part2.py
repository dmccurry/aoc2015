import json
import re
    
def cleanup(obj):
    new_json = []
    if isinstance(obj, dict) and ("red" in obj.values()) == True:
        return new_json
    elif isinstance(obj, dict):
        for key, value in obj.items():
            if isinstance(value, dict):
                more_json = cleanup(value)
                new_json.append(more_json)
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        more_json = cleanup(item)
                        new_json.append(more_json)
                    elif isinstance(item, list):
                        more_json = cleanup(item)
                        new_json.append(more_json)
                    else:
                        new_json.append(item)
            else:
                new_json.append(value)
    else:
        for value in obj:
            if isinstance(value, dict):
                more_json = cleanup(value)
                new_json.append(more_json)
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        more_json = cleanup(item)
                        new_json.append(more_json)
                    elif isinstance(item, list):
                        more_json = cleanup(item)
                        new_json.append(more_json)
                    else:
                        new_json.append(item)
            else:
                new_json.append(value)
    return new_json



input_file = open("input", "r")

input_text = input_file.read()
input_json = json.loads(input_text)

new_json = []
running_sum = 0

cleaned = cleanup(input_json)
cleaned_str = json.dumps(cleaned)
nums = re.findall('[-0-9]+', cleaned_str)
print(nums)
ints = map(int, nums)
print(sum(ints))
