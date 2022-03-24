def HexToDec(x):
    sum = 0
    for i in range(len(x)):
        if (x[i] == '1'):
            sum = sum + (1 * (16**(len(x)-1-i)))
        elif (x[i] == '2'):
            sum = sum + (2 * (16**(len(x)-1-i)))
        elif (x[i] == '3'):
            sum = sum + (3 * (16**(len(x)-1-i)))
        elif (x[i] == '4'):
            sum = sum + (4 * (16**(len(x)-1-i)))
        elif (x[i] == '5'):
            sum = sum + (5 * (16**(len(x)-1-i)))
        elif (x[i] == '6'):
            sum = sum + (6 * (16**(len(x)-1-i)))
        elif (x[i] == '7'):
            sum = sum + (7 * (16**(len(x)-1-i)))
        elif (x[i] == '8'):
            sum = sum + (8 * (16**(len(x)-1-i)))
        elif (x[i] == '9'):
            sum = sum + (9 * (16**(len(x)-1-i)))
        elif (x[i] == 'A') or (x[i] == 'a'):
            sum = sum + (10 * (16**(len(x)-1-i)))
        elif (x[i] == 'B') or (x[i] == 'b'):
            sum = sum + (11 * (16**(len(x)-1-i)))
        elif (x[i] == 'C') or (x[i] == 'c'):
            sum = sum + (12 * (16**(len(x)-1-i)))
        elif (x[i] == 'D') or (x[i] == 'd'):
            sum = sum + (13 * (16**(len(x)-1-i)))
        elif (x[i] == 'E') or (x[i] == 'e'):
            sum = sum + (14 * (16**(len(x)-1-i)))
        elif (x[i] == 'F') or (x[i] == 'f'):
            sum = sum + (15 * (16**(len(x)-1-i)))
    
    return (sum)

a = str(input())
result = HexToDec(a)
print(result)