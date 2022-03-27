Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import turtle
tao = turtle.Pen()
tao.shape('turtle')
turtle.bgcolor("blue")
tao.color("red")

def pretty(t):
    for i in range(12):
        n=10
        while n <=t:
            tao.circle(n)
            n=n+15
            tao.right(25)

            
pretty(60)
