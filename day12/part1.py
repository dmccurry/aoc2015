import re

input_file = open("input", "r")

input_text = input_file.read()

nums = re.findall('[-0-9]+', input_text)
ints = map(int, nums)
print(sum(ints))