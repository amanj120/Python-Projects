import math
def isPrime(n):
    for div in range (3,math.ceil(math.sqrt(n)) + 2, 2):
        if(n % div == 0):
            return False
    return True
iF = open("input.txt" , "r")
oF = open("output.txt" , "w+")
last = 2
for line in iF:
    for c in line.lower():
        while(not(last == 2 or last == 3 or isPrime(last))):
            last += 2
        oF.write((c) if (ord(c) < 97 or ord(c) > 122) else chr(((ord(c) - 97 + last)%26)+97))
        last += (2 if last != 2 else 1)
iF.close()
oF.close()
