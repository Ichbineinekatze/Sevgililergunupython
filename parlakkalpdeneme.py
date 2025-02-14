import math
import turtle

# Kalp fonksiyonları
def xt(t):
    return 16 * math.sin(t) ** 3

def yt(t):
    return 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)

# Kalp çizimi
def draw_heart():
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.begin_fill()
    t.fillcolor("red")
    for i in range(2550):
        t.goto((xt(i) * 20, yt(i) * 20))
    t.end_fill()

# Mesaj yazma fonksiyonu
def draw_text():
    t.penup()
    t.goto(-150, -30)  # Konumu ayarladım
    t.pendown()
    t.color("white")
    t.write("Seni seviyorum Nehir", font=("Arial", 16, "bold"))

# Ekranı ve turtle'ı ayarla
t = turtle.Turtle()
t.speed(500)
turtle.bgcolor('black')

# Kalp çiz ve yazıyı yaz
draw_heart()
draw_text()

# Pencereyi kapatmaması için
t.hideturtle()
turtle.done()
