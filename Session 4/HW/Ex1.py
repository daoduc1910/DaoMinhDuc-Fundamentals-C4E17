from collections import Counter

numbers = [1, 6, 8, 1, 2, 1, 5, 6]

a = int(input("Enter a number on the list: "))
b = numbers.count(a)
message = "{0} appear {1} time in the list".format(a,b)
print(message)
