encStr = "54 396 131 198 225 258 87 258 128 211 57 235 114 258 144 220 39 175 330 338 297 288"

encArr = [int(i) for i in encStr.split(" ")]

for i in encArr:
    modval = i % 37
    # print(modval)
    if modval < 26:
        print(chr(ord('a') + modval), end="")
    elif modval >= 26 and modval < 36:
        print(chr(ord('0') + modval - 26), end="")
    else:
        print("_", end="")
    # print()