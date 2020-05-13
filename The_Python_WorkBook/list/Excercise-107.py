# Avoiding Duplicates
# Create a program that reads words from the user until the enters a blank line. After the user enters a blank line
# your program should display each word entered by the user exactly once.

words =[]
word = input("Enter a word(or blank line to quit):")

while word != "":
    if word not in words:
        words.append(word)
    word = input("Enter a word(or blank line to quit):")

for word in words:
    print(word)


