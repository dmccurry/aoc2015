s = "3113322113"

out = ""
i = 0
iterations = 50
current_iteration = 0

while current_iteration < iterations:

    while i < len(s):
        current = s[i]
        count = 1
        if (i < len(s)):
            i = i + 1
            while i < len(s) and s[i] == current:
                count = count + 1
                i = i + 1
        out = out + str(count) + str(current)
    s = out
    i = 0
    out = ""
    current_iteration = current_iteration + 1
    print(current_iteration)
print("Solution is " + str(len(s)))