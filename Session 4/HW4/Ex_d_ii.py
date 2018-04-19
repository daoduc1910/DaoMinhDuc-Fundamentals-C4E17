n = int(input("Enter a number: "))

a = 1
b = 0

for i in range(n):
    for j in range(n):
        if i % 2 == 0:
            print(a, b, end=" ")
        else:
            print(b, a, end=" ")
    print(end='\n')
