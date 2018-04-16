print("Hello my name is Duc and here is my sheep size:")
sheep_size = [5, 7, 300, 90, 24, 50, 75]
print(sheep_size)

for i in range (3):
    print ("month", i+1, ":")
    for j in range (len(sheep_size)):
        sheep_size[j] = sheep_size[j] + 50
    print ("One month has passed, now here is my flock", sheep_size)
    print ("Now my biggest sheep has size", max(sheep_size), "let's shear it")
    a = sheep_size.index(max(sheep_size))
    sheep_size[a] = 8
    print ("After shearing it, here is my flock", sheep_size)

total = sum (sheep_size)
print ("My flock has size in total:", total)
money = total * 2
print ("I would get", money, "$")
