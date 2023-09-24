begin = int(input("Start of range: "))
end = int(input("End of range: "))

total = 0
count = 0

num = begin

while num <= end:
    total += num
    count += 1
    num += 1

if count > 0:
    average = total / count
else:
    average = 0

print(f"Sum of numbers {begin} to {end} is {total}")
print(f"Average of numbers {average}")