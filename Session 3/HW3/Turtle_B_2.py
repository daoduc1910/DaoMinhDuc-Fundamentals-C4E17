from turtle import*

speed(0)
colors = ['red', 'blue', 'brown', 'yellow', 'gray']

for a in range(5):
    color(colors[a])
    begin_fill()
    for b in range(2):
        forward(60)
        lt(90)
        forward(120)
        lt(90)
    forward(60)
    end_fill()











mainloop()
