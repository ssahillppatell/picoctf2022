encStr = "268 413 110 190 426 419 108 229 310 379 323 373 385 236 92 96 169 321 284 185 154 137 186"

encArr = [int(i) for i in encStr.split(" ")]

def modInverse(a, m):
 
    g = gcd(a, m)
 
    if (g != 1):
        print("Inverse doesn't exist")
        return 0
 
    else:
        return power(a, m - 2, m)
 
 
 
def power(x, y, m):
    if (y == 0):
        return 1
 
    p = power(x, y // 2, m) % m
    p = (p * p) % m
 
    if(y % 2 == 0):
        return p
    else:
        return ((x * p) % m)
 
 
def gcd(a, b):
    if (a == 0):
        return b
    return gcd(b % a, a)

for i in encArr:
    modval = modInverse(i % 41, 41)
    # print(modval, end=" ")
    if modval < 27:
        print(chr(ord('a') + modval - 1), end="")
    elif modval >= 27 and modval < 37:
        print(chr(ord('0') + modval - 27), end="")
    elif modval == 37:
        print("_", end="")
    # print()