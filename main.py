length = int(input("Length: "))
symbol = input("Symbol: ")

if length < 0:
    print("Unknown operation number ")
else:
    line = symbol * length
    print(line)