from turtle import*


bgcolor("black")
speed(0)
hideturtle()

for i in range(120):
 color("white")
 circle(i)
 color("green")
 circle(i*0.8)
 color("orange")
 circle(i*1.2)
 right(3)
 forward(3)
done()
