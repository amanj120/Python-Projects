import math

def PrimeSieve(n):
    i = 0;
    lastPrime = 15;
    while(len(prime) < n):
        primeFound = True
        while(primeFound):
            for div in range (2,math.ceil(math.sqrt(lastPrime)) + 2):
                print(str(lastPrime) + " being divided by " + str(div))
                if(lastPrime % div == 0):
                    lastPrime += 2
                    div = 2
                    break
            primeFound = False
            prime.append(lastPrime)
            lastPrime += 2
        i += 1
    for p in prime:
        print(p)

inputFile = open("input.txt" , "r")
chars = []
prime = [1,2,3,5,7,11,13]
for line in inputFile:
    for word in line.split():
        for c in range (len(word)):
            chars.append(word[c])
            #print(word[c])
PrimeSieve(20)



