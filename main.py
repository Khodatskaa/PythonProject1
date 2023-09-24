begin = int(input('begin->'))
end = int(input('end->'))

while begin <= end:
    print(begin, end="\t")
    if begin % 5 == 0:
        print(f"| % 5", end=" ")
    if begin % 7 == 0:
        print(f"| % 7", end=" ")
    print()
    begin += 1
