begin = int(input(":"))
end = int(input(":"))

while begin <= end:
    if begin % 3 == 0:
        print('Fizz')
    if begin % 5 == 0:
        print('Buzz')
    begin += 1
else:
    print(begin)