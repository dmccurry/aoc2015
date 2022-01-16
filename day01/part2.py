inputFile = open("input", "r")
data = inputFile.read()
floors = 0
index = 1

for letter in data:
    if letter == "(":
        floors = floors + 1
    else:
        floors = floors - 1

    if (floors < 0):
        print("Solution is " + str(index))
        break

    index = index + 1
    

