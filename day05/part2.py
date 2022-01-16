def is_nice(s):
    i = 0 
    has_double = False
    has_split = False
    for c in s:
        if i < len(s) - 1:
            cs = c + s[i+1]
            if cs in s[i+2::]:
                has_double = True

        if i < len(s) - 2:
            if c == s[i+2]:
                has_split = True
        i = i + 1
    
    return has_double and has_split

input_file = open("input", "r")
nice = 0
for line in input_file:
    if is_nice(line):
        nice = nice + 1

print("Solution is " + str(nice))

print(is_nice("qjhvhtzxzqqjkmpb"))
print(is_nice("xxyxx"))
print(is_nice("uurcxstgmygtbstg"))
print(is_nice("ieodomkazucvgmuy"))
print(is_nice("yzsmlbnftftgwadz"))