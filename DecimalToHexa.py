def DecToHex(x):
    i = 0
    while ((x // 16**i) != 0):
        i += 1

    ArrSize = i
    temp1 = x
    temp2 = x
    Arr = [" " for i in range(ArrSize)]
    
    for i in range(ArrSize-1,-1,-1):
        temp1 = temp1 // 16
        sisa = temp2 % 16
        temp2 = temp1
        if (sisa == 1):
            Arr[i] = 1
        elif (sisa == 2):
            Arr[i] = 2
        elif (sisa == 2):
            Arr[i] = 2
        elif (sisa == 3):
            Arr[i] = 3
        elif (sisa == 4):
            Arr[i] = 4
        elif (sisa == 5):
            Arr[i] = 5
        elif (sisa == 6):
            Arr[i] = 6
        elif (sisa == 7):
            Arr[i] = 7
        elif (sisa == 8):
            Arr[i] = 8
        elif (sisa == 9):
            Arr[i] = 9
        elif (sisa == 10):
            Arr[i] = 'A'
        elif (sisa == 11):
            Arr[i] = 'B'
        elif (sisa == 12):
            Arr[i] = 'C'
        elif (sisa == 13):
            Arr[i] = 'D'
        elif (sisa == 14):
            Arr[i] = 'E'
        elif (sisa == 15):
            Arr[i] = 'F'

    return Arr
    
a = int(input())
result = DecToHex(a)
for i in range(len(result)):
    print(result[i], end ="")