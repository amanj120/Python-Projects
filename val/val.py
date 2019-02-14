import math

def PrimeSieve(n, lastPrime):
    while(len(primes) < n):
        if(isPrime(lastPrime)):
            primes.append(lastPrime)
        lastPrime += 2
        
def isPrime(n):
    for div in range (3,math.ceil(math.sqrt(n)) + 2):
        if(n % div == 0):
            return False
        div += 1
    return True

#inputFile = open("input.txt" , "r")
line = "Hi  dweb pee lol"
chars = []
primes = [1,2,3]
#for line in inputFile:
for word in line.split():
    for c in range (len(word)):
        chars.append(ord(word[c].lower()) - 97)
PrimeSieve(len(chars),5)
print(line)
i = 0
for char in line:
    if char == " " or char == "." or char == ",":
        print(char, end="")
    else :
        print((chr(((chars[i] + primes[i])%26)+97)), end="")
        i += 1
