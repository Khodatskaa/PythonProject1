begin = int(input(": "))
end = int(input(": "))

while begin <= end:
    if begin % 7 == 0:
        print(begin)
    begin += 1
print()