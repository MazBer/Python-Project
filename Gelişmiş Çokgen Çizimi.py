# Ekler
import turtle
import random
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

# Program fonksiyona gönderilen parametreler ile çokgen çizer.
# Uzunluk paremetresi girilerek herbir kenarın uzunluğu belirlenir.
# Çizim x ve y parametrelerine girilen koordinat noktalarından başlar.
# Bir sonraki parametre çizimin kenar rengini belirler. (Varsayılan değer olarak siyah).
# Çizilen çokgenin içine dolgu olup olmayacağı belirlenir(Varsayılan False).

def Cokgen(kenarSayisi, uzunluk, x, y, renk="black", dolgu=False):
    turtle.penup()
    turtle.setposition(x, y)
    turtle.pendown()
    turtle.color(renk)
    if dolgu:
        turtle.begin_fill()
    for i in range(kenarSayisi):
        turtle.forward(uzunluk)
        turtle.left(360//kenarSayisi)
    if dolgu:
        turtle.end_fill()

# Giriş
print(Fore.RED + """
|=====================================|
|                                     |
|     Gelişmiş Çokgen Çizme Aracı     |
|              Sürüm 1.2              |
|                                     |
|=====================================|
""")

# Veri Alınması
print(Fore.BLUE + "===Kenar Sayısı======================")
KenarSayisi2 = int(input(Fore.LIGHTWHITE_EX + "Kenar sayısı giriniz:"))
print(Fore.BLUE + "=====================================")
print(" ")
print(Fore.BLUE + "===Kenar Uzunluğu====================")
Uzunluk2 = float(input(Fore.LIGHTWHITE_EX + "Kenar uzunluğu giriniz:"))
print(Fore.BLUE + "=====================================")
print(" ")
print(Fore.BLUE + "===Renk==============================")
Renk2 = str(input(Fore.LIGHTWHITE_EX + "Renk giriniz:"))
print(Fore.BLUE + "=====================================")
print(" ")
print(Fore.BLUE + "===Dolgu=============================")
Dolgu2 = str(input(Fore.LIGHTWHITE_EX + "Dolgu olsun mu:"))
print(Fore.BLUE + "=====================================")
print(" ")

Cokgen(KenarSayisi2, Uzunluk2, 0, 0, Renk2, Dolgu2) 

turtle.update()
turtle.hideturtle()
turtle.exitonclick() # Fare tuşuna tıklandığında çıkış işlemi yapılacaktır.

# Veriler
alan = (1/4) * KenarSayisi2 * Uzunluk2 * Uzunluk2
cevre = KenarSayisi2 * Uzunluk2
print(Fore.BLUE + "===Veriler===========================")
print(Fore.LIGHTWHITE_EX + "Alan  =",alan)
print(Fore.LIGHTWHITE_EX + "Çevre =",cevre)
print(Fore.BLUE + "=====================================")

# Bitirme
print(Fore.RED + """
|=====================================|
|                                     |
|         Mazhar Berk AYDOĞDU         |
|            Made in Turkey           |
|                                     |
|=====================================|
""")