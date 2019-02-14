import math

def PrimeSieve(n):
    lastPrime = 5;
    while(len(primes) < n):
        if(isPrime(lastPrime)):
            primes.append(lastPrime)
        lastPrime += 2
        
def isPrime(n):
    for div in range (2,math.ceil(math.sqrt(n)) + 2):
        if(n % div == 0):
            return False
    return True

#inputFile = open("input.txt" , "r")
line = "Hi  dweb pee lol"
chars = []
code = []
primes = [1,2,3]
#for line in inputFile:
for word in line.split():
    word = word.lower()
    for c in range (len(word)):
        chars.append(ord(word[c]) - 97)
        #print(word[c])
        #print(chars[-1])
PrimeSieve(len(chars))
print(chars)
print(primes)
i = 0
for char in line:
    if char == " " or char == "." or char == ",":
        code.append(char)
    else :
        code.append(chr(((chars[i] + primes[i])%26)+97))
        i += 1
print(line)
print("".join(code))
