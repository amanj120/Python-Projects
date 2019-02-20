def gcd(a,b):
    if b == 0:
        return a
    elif  a > b:
        return gcd(b, a%b)
    else :
        return gcd(a, b%a)

print(gcd(8973827, 7761))
