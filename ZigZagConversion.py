s = "PAYPALISHIRING"
rows = 4

if rows == 1:
    print([s])
else:
    counter=0
    flag = False
    output = [""]*rows

    for ch in s:
        output[counter]+=ch
        if counter==0 or counter==rows-1:
            flag = not flag

        counter= counter + 1 if flag else counter - 1

    print(output)
