a = 1
b = 0

for i in range(10):
    for j in range(10):
        if i % 2 == 0:
            print(a, b, end=" ")
        else:
            print(b, a, end=" ")
    print(end='\n')
