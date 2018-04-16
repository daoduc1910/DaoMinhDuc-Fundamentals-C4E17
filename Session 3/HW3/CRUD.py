items = ['T-Shirt', 'Sweater']

while True:

    print("Welcome to our shop, what do u want?")
    print("We have: ", end='')
    print(*items, sep=',')


    C = input("Enter new item: ")
    items.append(C)
    print("We have: ", end="")
    print(*items, sep=',')

    D = int(input("Type item number you want to delete "))
    del items[D]
    print("We have: ", end="")
    print(*items, sep=",")

    U = int(input("value Update: "))
    i = input("Type item you want to update: ")
    items[U] = i
    print("Our items: ", end = "")
    print(*items, sep=',')
