inputFile = open("input", "r")
total = 0
def get_slack(l, w, h): 
    a = l * w
    b = w * h
    c = h * l

    return min(a, b, c)

for line in inputFile: 
    [l, w, h] = line.split("x")
    l = int(l)
    w = int(w)
    h = int(h)
    area = 2 * l * w + 2 * l * h + 2 * w * h
    slack = get_slack(l, w, h)
    total = total + area + slack

print ("Solution is " + str(total))