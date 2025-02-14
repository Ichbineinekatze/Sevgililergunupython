import turtle

# Ekranı açalım
t = turtle.Turtle()
t.speed(3)

# Kalp çizen fonksiyon
def heart():
    t.begin_fill()
    t.fillcolor("red")
    t.left(50)
    t.forward(133)
    t.circle(50, 200)
    t.right(140)
    t.circle(50, 200)
    t.forward(133)
    t.end_fill()


heart()

turtle.done()
