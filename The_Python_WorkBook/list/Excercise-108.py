# Negatives, Zeros and Positive
# Once all the intergers have been read your program should display all of the negative numbers,
# followed by all the zeros, followed by all of the positive numbers
# For example, if the user enters the values 3, -4,1,0,-1,0, and -2
# then your program should output the values -4, -1, -2, 0, 0, 3, and 1. Your program should display each value on its
# own line.

positive = []
zeros = []
negative = []

for i in range(100000000000):
    number = input('Enter the integer(negative or zeros or positive( blank line to quit):')
    if number == '':
        break
    elif int(number) > 0:
        positive.append(int(number))
    elif int(number) < 0:
        negative.append(int(number))
    else:
        zeros.append(int(number))

full_list = negative + zeros + positive

for i in full_list:
    print(i)
