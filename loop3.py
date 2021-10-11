# for loop
acc = 0.0
for i in range(0, 5):
    num = float(input("Enter a number to accumulate: "))
    acc = acc + num

print("Th accumulated value = ", acc)

l = ["Greek", "Latin", "French", "Italian", "Spanish"]
for i in l:
    print(i)