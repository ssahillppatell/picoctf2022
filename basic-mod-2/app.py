encStr = "268 413 110 190 426 419 108 229 310 379 323 373 385 236 92 96 169 321 284 185 154 137 186"

encArr = [int(i) for i in encStr.split(" ")]

def invmod(a,b): return 0 if a==0 else 1 if b%a==0 else b - invmod(b%a,a)*b//a

for i in encArr:
    modval = invmod(i % 41, i)
    # print(modval, end=" ")
    if modval < 27:
        print(chr(ord('a') + modval - 1), end="")
    elif modval >= 27 and modval < 37:
        print(chr(ord('0') + modval - 27), end="")
    elif modval == 37:
        print("_", end="")
    # print()