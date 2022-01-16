def is_nice(s): 
    if "ab" in s or "cd" in s or "pq" in s or "xy" in s:
        return False
    
    num_vowels = 0
    has_double = False
    for a in s:
        if a == "a" or a == "e" or a == "i" or a == "o" or a == "u":
            num_vowels = num_vowels + 1
        st = a + a
        if st in s:
            has_double = True

    if num_vowels < 3:
        return False
    
    return has_double

input_file = open("input", "r")
nice = 0
for line in input_file:
    if is_nice(line):
        nice = nice + 1

print("Solution is " + str(nice))