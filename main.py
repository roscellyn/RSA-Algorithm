import time

def is_prime(a):
    a_prime = True
    if(a > 1):
        i = 2
        while(a_prime and i <= a//2):
            if(a % i == 0):
                a_prime = False
            i += 1
    else:
        a_prime = False

    return a_prime

def fpb(a, b):
    if(b == 0):
        return a
    else:
        return fpb(b, a % b)

# Memilih nilai p dan q
p = int(input("p = "))
while(is_prime(p) == False):
    p = int(input("p = "))
q = int(input("q = "))
while(is_prime(q) == False):
    q = int(input("q = "))

# Menghitung nilai n dan totient
n = p * q
totient = (p-1) * (q-1)

# Memilih nilai e
e = int(input("e = "))
while(fpb(totient, e) != 1):
    e = int(input("e = "))
    
# Menghitung kunci
k = 1
d = 0.1
while(d%1 != 0):
    d = (1 + k * totient)/e
    k += 1
d = int(d)
print(d)

f=open("troll.jpg","rb")
file_bytes = f.read()
f.close()
print(file_bytes)
for byte in file_bytes:
    print(byte)

start_time = time.time()
end_time = time.time()
print("Waktu: " + str(round(end_time - start_time, 2)))