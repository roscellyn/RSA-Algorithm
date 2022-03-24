#Nama    : Jacelyn Felisha
#NIM     : 18219097
#Kelas	 : K01
#Program : Konversi Desimal, Oktal, Biner, dan Hexagonal

#Program Mengkonversi Antar Decimal, Octal, Binary, dan Hexadecimal

#Prosedur mengubah bilangan decimal ke binary
#Asumsi : binary dengan 32 bit
def decimalToBinary(a):
    arrayB = [0 for i in range(32)]
    for i in range(31):
        arrayB[i] = a%2 
        a = int(a//2)
    for i in range(31, -1, -1):
        print(arrayB[i], end='')

#Prosedur mengubah bilangan decimal ke octal
#Asumsi : jumlah digit octal maks 10
def decimalToOctal(a):
    arrayB = [0 for i in range(10)]
    for i in range(9):
        arrayB[i] = a%8
        a = int(a//8)
    for i in range(9, -1, -1):
        print(arrayB[i], end='')

#Prosedur antara untuk mengubah bilangan decimal ke hexadecimal
def betweenDTH(a):
    if (a==10):
        print('A', end='')
    elif (a==11):
        print('B', end='')
    elif (a==12):
        print('C', end='')
    elif (a==13):
        print('D', end='')
    elif (a==14):
        print('E', end='')
    elif (a==15):
        print('F', end='')
    else:
        print(a, end='')

#Prosedur mengubah bilangan decimal ke hexadecimal
def decimalToHexadecimal(a):
    arrayH = [0 for i in range(6)]
    if (a>=0) and (a<16):
        betweenDTH(a)
    elif (a>=16):
        for i in range(5):
            arrayH[i] = a%16
            a = int(a//16)
        for i in range(5, -1, -1):
            betweenDTH(arrayH[i])
    else:
        print('Masukkan tidak valid.')

#Fungsi mengubah bilangan binary ke decimal
def binaryToDecimal(a):
    a = str(a)
    panjang = len(a)-1
    sum = 0
    for i in range(0, panjang+1):
        sum += int(a[i])*2**(panjang)
        panjang -= 1
    return(sum)

#Prosedur mengubah bilangan binary ke octal
def binaryToOctal(a):
	decimalToOctal(binaryToDecimal(a))
	
#Prosedur mengubah bilangan binary ke hexadecimal 
def binaryToHexadecimal(a):
    a = str(a)
    arrayH = [0 for j in range(6)]
    panjang = len(a)-1
    kuadrat = 0
    j=0
    for i in range(panjang, -1, -1):
        if(kuadrat <= 3):
            if (a[i] == '1'):
                arrayH[j] += 2**(kuadrat)
            kuadrat += 1
        else:
            j += 1
            kuadrat = 0
            if (a[i] == '1'):
                arrayH[j] += 2**(kuadrat)
            kuadrat += 1
    for j in range(5, -1, -1):
        betweenDTH(arrayH[j])

#Fungsi mengubah bilangan octal ke decimal
def octalToDecimal(a):
    a = str(a)
    panjang = len(a)-1
    sum = 0
    for i in range(0, panjang+1):
        sum += int(a[i])*8**(panjang)
        panjang -= 1
    return(sum)

#Prosedur mengubah bilangan octal ke binary
def octalToBinary(a):
    decimalToBinary(octalToDecimal(a))

#Prosedur mengubah bilangan octal ke hexadecimal
def octalToHexadecimal(a):
    decimalToHexadecimal(octalToDecimal(a))

#Fungsi mengubah bilangan hexadecimal ke decimal
def hexadecimalToDecimal(a):
    sum = 0
    panjang = len(a)-1
    for i in range(0, panjang+1):
        if (a[i] == 'A' or a[i] == 'a'):
            sum += 10*(16**panjang)
        elif (a[i] == 'B' or a[i] == 'b'):
            sum += 11*(16**panjang)
        elif (a[i] == 'C' or a[i] == 'c'):
            sum += 12*(16**panjang)
        elif (a[i] == 'D' or a[i] == 'd'):
            sum += 13*(16**panjang)
        elif (a[i] == 'E' or a[i] == 'e'):
            sum += 14*(16**panjang)
        elif (a[i] == 'F' or a[i] == 'f'):
            sum += 15*(16**panjang)
        else :
            sum += int(a[i])*(16**panjang)
        panjang -= 1
    return(sum)

#Prosedur mengubah bilangan hexadecimal ke binary
def hexadecimalToBinary(a):
    decimalToBinary(hexadecimalToDecimal(a))

#Prosedur mengubah bilangan hexadecimal ke octal
def hexadecimalToOctal(a):
    decimalToOctal(hexadecimalToDecimal(a))


#KAMUS UTAMA
# jenisInput : string
# jenisOutput : string
# a = int
# b : string 

#ALGORITMA PROGRAM UTAMA
#Menampilkan pilihan jenis bilangan input/output
print("Jenis bilangan input/output : Decimal / Binary / Octal / Hexadecimal")
print()
#Menerima input jenis bilangan yang ingin dikonversi (Decimal, Octal, Binary, atau Hexadecimal)
jenisInput = input("Masukkan jenis input : ")
#Menerima input jenis bilangan yang menjadi hasil konversi (Decimal, Octal, Binary, atau Hexadecimal)
jenisOutput = input("Masukkan jenis output : ")

#Asumsi : masukan bilangan yang ingin dikonversi valid
if (jenisInput == "Decimal"):
    a = int(input("Masukkan bilangan yang ingin dikonversi : "))
    if (jenisOutput == "Binary"):
        decimalToBinary(a)
    elif (jenisOutput == "Octal"):
        decimalToOctal(a)
    elif (jenisOutput == "Hexadecimal"):
        decimalToHexadecimal(a)
    else :
        print("Masukkan jenis tidak valid.")
elif (jenisInput == "Binary"):
    a = int(input("Masukkan bilangan yang ingin dikonversi : "))
    if (jenisOutput == "Decimal"):
        print(binaryToDecimal(a))
    elif (jenisOutput == "Octal"):
        binaryToOctal(a)
    elif (jenisOutput == "Hexadecimal"):
        binaryToHexadecimal(a)
    else :
        print("Masukkan jenis tidak valid.")
elif (jenisInput == "Octal"):
    a = int(input("Masukkan bilangan yang ingin dikonversi : "))
    if (jenisOutput == "Decimal"):
        print(octalToDecimal(a))
    elif (jenisOutput == "Binary"):
        octalToBinary(a)
    elif (jenisOutput == "Hexadecimal"):
        octalToHexadecimal(a)
    else :
        print("Masukkan jenis tidak valid.")
elif (jenisInput == "Hexadecimal"):
    b = input("Masukkan bilangan yang ingin dikonversi : ")
    if (jenisOutput == "Decimal"):
        print(hexadecimalToDecimal(b))
    elif (jenisOutput == "Binary"):
        hexadecimalToBinary(b)
    elif (jenisOutput == "Octal"):
        hexadecimalToOctal(b)
    else :
        print("Masukkan jenis tidak valid.")
else :
    print("Masukkan jenis tidak valid.")
