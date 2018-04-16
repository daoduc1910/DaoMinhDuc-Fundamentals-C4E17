from turtle import *

speed(0)

colors = ['red', 'blue', 'brown', 'yellow', 'gray']
for i in range(5):
    color(colors[i])
    for j in range(i + 3):
        forward(120)
        left(360/(i+3))

mainloop()
