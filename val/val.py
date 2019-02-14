import math

'''
def PrimeSieve(n, lastPrime):
    while(len(primes) < n):
        if(isPrime(lastPrime)):
            primes.append(lastPrime)
        lastPrime += 2
'''      
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
chars = []
#primes = [1,2,3]
#for line in inputFile:
for word in line.split():
    for c in range (len(word)):
        chars.append(ord(word[c].lower()) - 97)
#PrimeSieve(len(chars),5)
print(line)
i = 0
lastPrime = 1
for char in line:
    if char == " " or char == "." or char == ",":
        print(char, end="")
    else :
        while(not isPrime(lastPrime)):
            lastPrime += 2
        print((chr(((chars[i] + lastPrime)%26)+97)), end="")
        #print(lastPrime)
        if(lastPrime < 3):
            lastPrime -= 1
        lastPrime += 2
        i += 1
