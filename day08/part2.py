import re
input_file = open("input", "r")

full_length = 0
mem_length = 0

hex_re = re.compile(r'\\x[a-f0-9]{2}')

def get_mem_length(s):
    num_quotes = s.count("\"")
    num_slash = s.count("\\")
    return len(s) + 2 + num_quotes + num_slash



for line in input_file:
    full_length = full_length + len(line.strip())
    mem_length = mem_length + get_mem_length(line.strip())

print("Solution is " + str(mem_length - full_length))