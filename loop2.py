# emulate a do while structure
acc = 0.0
choice = 'n'
while True:
    num = float(input("Enter a value to accumulate: "))
    acc = acc + num
    choice = int(input("Do you want to continue adding 1: yes/2: no?: "))
    if choice == 2:
        break

print("accumulated value: ", acc)