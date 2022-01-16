import hashlib
key = "yzbqklnj"
done = False
num = 1

while done == False:
    st = key + str(num)
    num_hash = hashlib.md5(st.encode())
    if num_hash.hexdigest().startswith("000000") == True:
        done = True
        print("Solution is " + str(num))
    
    num = num + 1
