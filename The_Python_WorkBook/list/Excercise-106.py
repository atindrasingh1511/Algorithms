# Remove Outliers
# Write a function that takes a list of values and an non-negative integer, n, as its parameters
# the function should create a new copy of the list with the n largest elements and the n smallest elements removed
# Then it should return the new copy of the list as the function's only result.


def removeOutliers(data, num_outliers):
    retval = sorted(data)

    for i in range(num_outliers):
        retval.pop()

    for i in range(num_outliers)      :
        retval.pop(0)

    return retval

def main():
    l = []
    for i in range(10000000000):
        value = int(input("Enter the integer: "))
        if value == 0:
            break
        else:
            l.append(value)
    print("Values in the list",l)
    n = int(input("Enter the value of positive n to remove largest and smallest elements: "))
    if len(l) < 2*n :
        print("You didn't enter enough values:")
    else:
        print("With the Outliers removed", removeOutliers(l, n))

if __name__ == '__main__':
    main()
