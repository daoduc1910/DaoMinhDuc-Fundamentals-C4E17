print("Hello my name is Duc and here is my sheep size:")
sheep_size = [5, 7, 300, 90, 24, 50, 75]
print(sheep_size)

biggest = max(sheep_size)
print("Now my biggest sheep has size", biggest, "let's shear it")

for i in range(len(sheep_size)):
    sheep_size[i]= sheep_size[i] + 50

print("One month has passed, now here is my flocks", sheep_size)
