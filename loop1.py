count = int(input("Enter how many numbers you want to add: "))
sum = 0

while count > 0:
    num = float(input("Enter a number to accumulate: "))
    sum += num
    count = count -1

print("Accumulated value = ", sum)