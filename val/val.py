import math

def isPrime(n):
    if(n == 1 or n == 2 or n == 3):
        return True
    for div in range (3,math.ceil(math.sqrt(n)) + 2):
        if(n % div == 0):
            return False
        div += 1
    return True

#inputFile = open("input.txt" , "r")
line = "Hi  dweb pee lol"
print(line)
#for line in inputFile:
lastPrime = 1
for char in range (len(line)):
    c = line[char]
    if c == " " or c == "." or c == ",":
        print(c, end = "")
    else:
        while(not isPrime(lastPrime)):
            lastPrime += 2
        print((chr((((ord(c.lower()) - 97) + lastPrime)%26)+97)), end = "")
        if(lastPrime < 3):
            lastPrime -= 1
        lastPrime += 2
