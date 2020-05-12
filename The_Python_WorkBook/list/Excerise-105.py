# Reverse Order
# Write a program that reads integers from the user and stores them in a list. Use 0 as sentinel value to mark the end
# of the input. Once all of the values have been read your prgram should display(except for the 0) in reverse order,
# with one value appearing on each line.
from audioop import reverse

l = []
for i in range(10000000000):
    value = int(input("Enter the integer: "))
    if value == 0:
        break
    else:
        l.append(value)
for i in reversed(l):
    print(i)