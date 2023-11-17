import turtle
import math
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

def Hipo(x,y):
    return math.sqrt(x * x + y * y)

print(Fore.YELLOW + "===Hipotenüs Hesaplama============================")
sayi1 = int(input(Fore.LIGHTWHITE_EX + "A Kenarı: "))
sayi2 = int(input(Fore.LIGHTWHITE_EX + "B Kenarı: "))
print(sayi1,"²","+",sayi2,"²","=",end=" ")
print(Fore.RED +  str(Hipo(sayi1,sayi2)),"²")
print(Fore.YELLOW + "==================================================")
math.sin(sayi2 / math.sqrt(sayi1 * sayi1 + sayi2 * sayi2))
if sayi1 + sayi2 < 10:
    turtle.left(180)
    turtle.pensize(5)
    turtle.pencolor("blue")
    turtle.forward(sayi1 * 50)
    turtle.right(90)
    turtle.pencolor("green")
    turtle.forward(sayi2 * 50)
    if sayi1 < sayi2:
        turtle.pencolor("red")
        turtle.right(143)
        turtle.forward(Hipo(sayi1,sayi2) * 50)
        turtle.update()
        turtle.hideturtle()
        turtle.exitonclick()
    elif sayi1 > sayi2:
        turtle.pencolor("red")
        turtle.right(127)
        turtle.forward(Hipo(sayi1,sayi2) * 50)
        turtle.update()
        turtle.hideturtle()
        turtle.exitonclick()