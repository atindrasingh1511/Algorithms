# Write a program that reads integers from the user and stores them in a list. Your program  should continue reading
# values until the user enters 0 in order from smallest to largest with one value appearing on each line. Use either
# sort method or the sorted function to sort the list.

l = []
for i in range(10000000000):
    value = int(input("Enter the integer: "))
    if value == 0:
        break
    else:
        l.append(value)
for i in sorted(l):
    print(i)


