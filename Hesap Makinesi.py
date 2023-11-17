# Ekler
import math
import sys
import turtle
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

# Toplama Fonksiyonu
def Topla(x,y):
   return x + y
 
# Çıkarma Fonksiyonu
def Cikar(x,y):
   return x - y
 
# Çarpma Fonksiyonu
def Carp(x,y):
   return x * y
 
# Bölme Fonksiyonu
def Bol(x,y):
   return x / y

# Daire Çevre Fonksiyonu
def Cevre(x):
   return x * 2 * 3.14

# Daire Alan Fonksiyonu
def D_Alan(x):
   return x * x * 3.14

# Üçgen Alan Fonksiyonu
def U_Alan(x,y):
    return x * y / 2

# Üs Alma Fonksiyonu
def Us(x,y):
    return x ** y

# Faktöriyel Hesaplama Fonksiyonu
def Fak(x):
    factorial = 1
    if x >= 0:
        for i in range(1, x+1):
            factorial *= i
        return factorial
    else:
        return None
    
# Poligon Alan Hesaplama Fonksiyonu
def Pol_Alan(x,y):
    return (1/4) * x * y * y

# Poligon Çevre Hesaplama Fonksiyonu
def Pol_Alan(x,y):
    return x * y

# Kare Kök Fonksiyonu
def Kare_Kok(x):
    return math.sqrt(x)

# Hipotenüs Hesaplama
def Hipo(x,y):
    return math.sqrt(x * x + y * y)

# Ardışık Sayıların Toplamı
def Ard_Top(x,y,z):
    return ((y - x) / z + 1) * ((y + x) / 2)

# Ardışık Sayıların Çarpımı
def Ard_Carp(x,y,z):
    sonuc = x
    for i in range(x+z,y+1,z):
        sonuc *= i
    return sonuc

# Onluk Sistemden İkilik Sisteme Çevirme
def On_Iki(x):
    return bin(x)[2:]

# İkilik Sistemden Onluk Sisteme Çevirme
def Ikı_On(x):
    return int(str(x), 2)

# Açıklama
print(Fore.LIGHTRED_EX + """
|================================================|
|                                                |
|                  Hesap Makinesi                |
|                 Sürüm 2.0 Beta 7               |
|                                                |                                
|================================================|
""")
print(Fore.LIGHTBLUE_EX + "===Açıklama======================================")
print(Fore.LIGHTWHITE_EX + "Yapılacak İşlemi Seçin:")
print(Fore.LIGHTWHITE_EX + "1-  Serbest Mod")
print(Fore.LIGHTWHITE_EX + "2-  Toplama")
print(Fore.LIGHTWHITE_EX + "3-  Çıkarma")
print(Fore.LIGHTWHITE_EX + "4-  Çarpma")
print(Fore.LIGHTWHITE_EX + "5-  Bölme")
print(Fore.LIGHTWHITE_EX + "6-  Daire Çevre Hesaplama")
print(Fore.LIGHTWHITE_EX + "7-  Daire Alan Hesaplama")
print(Fore.LIGHTWHITE_EX + "8-  Üçgen Alan Hesaplama")
print(Fore.LIGHTWHITE_EX + "9-  Üs Alma")
print(Fore.LIGHTWHITE_EX + "10- Faktöriyel Hesaplama")
print(Fore.LIGHTWHITE_EX + "11- Poligon Alan Hesaplama")
print(Fore.LIGHTWHITE_EX + "12- Poligon Çevre Hesaplama")
print(Fore.LIGHTWHITE_EX + "13- Kare Kök Alma")
print(Fore.LIGHTWHITE_EX + "14- Hipotenüs Hesaplama")
print(Fore.LIGHTWHITE_EX + "15- Ardışık Sayıların Toplamı")
print(Fore.LIGHTWHITE_EX + "16- Ardışık Sayıların Çarpımı")
print(Fore.LIGHTWHITE_EX + "17- Onluk Sistemden İkilik Sisteme Çevirme")
print(Fore.LIGHTWHITE_EX + "18- İkilik Sistemden Onluk Sisteme Çevirme")
print(Fore.LIGHTBLUE_EX + "==================================================")

while True:
    # Kullanıcıdan Seçim İsteme
    print(" ")
    print(Fore.LIGHTGREEN_EX + "===Seçim==========================================")
    secim = input(Fore.LIGHTWHITE_EX + "Seçiminiz: ")
    print(Fore.LIGHTGREEN_EX + "==================================================")

    # Serbest Mod
    if secim == '1' or secim == 'Serbest' or secim == 'serbest' or secim == 'Free' or secim == 'Free':
        while True:
            print(" ")
            print(Fore.YELLOW + "===Serbest Mod====================================")
            sayi1 = float(input("Sayı 1: "))
            islem = str(input("İşlem: "))
            sayi2 = float(input("Sayi 2: "))
            if islem == '-1' or islem == 'Bitir' or islem == 'bitir' or islem == 'End' or islem == 'end':
                break
            if islem == '+':
                print("Sonuç:",Fore.RED + str(sayi1+sayi2))
            if islem == '-':
                print("Sonuç:",Fore.RED + str(sayi1-sayi2))
            if islem == 'x' or islem == '.' or islem == '*':
                print("Sonuç:",Fore.RED + str(sayi1*sayi2))
            if islem == '/':
                print("Sonuç:",Fore.RED + str(sayi1/sayi2))
            if islem == '//':
                print("Sonuç:",Fore.RED + str(sayi1//sayi2))
            if islem == '%':
                print("Sonuç:",Fore.RED + str(sayi1%sayi2))
            if islem == '**':
                print("Sonuç:",Fore.RED + str(sayi1**sayi2))
            print(Fore.YELLOW + "==================================================")
    
    # Toplama İşlemi
    if secim == '2' or secim == 'Toplama' or secim == 'toplama':
        print(" ")
        print(Fore.YELLOW + "===Toplama========================================")
        sayi1 = float(input(Fore.LIGHTWHITE_EX + "1. Sayı: "))
        sayi2 = float(input(Fore.LIGHTWHITE_EX + "2. Sayı: "))
        print(sayi1,"+",sayi2,"=",end=" ")
        print(Fore.RED + str(Topla(sayi1,sayi2)))
        print(Fore.YELLOW + "==================================================")

    # Çıkarma İşlemi
    if secim == '3' or secim == 'Çıkarma' or secim == 'çıkarma':
        print(" ")
        print(Fore.YELLOW + "===Çıkarma========================================")
        sayi1 = float(input(Fore.LIGHTWHITE_EX + "1. Sayı: "))
        sayi2 = float(input(Fore.LIGHTWHITE_EX + "2. Sayı: "))
        print(sayi1,"-",sayi2,"=",end=" ")
        print(Fore.RED + str(Cikar(sayi1,sayi2)))
        print(Fore.YELLOW + "==================================================")

    # Çarpma İşlemi
    if secim == '4' or secim == 'Çarpma' or secim == 'çarpma':
        print(" ")
        print(Fore.YELLOW + "===Çarpma=========================================")
        sayi1 = float(input(Fore.LIGHTWHITE_EX + "1. Sayı: "))
        sayi2 = float(input(Fore.LIGHTWHITE_EX + "2. Sayı: "))
        print(sayi1,"*",sayi2,"=",end=" ")
        print(Fore.RED + str(Carp(sayi1,sayi2)))
        print(Fore.YELLOW + "==================================================")

    # Bölme İşlemi
    if secim == '5' or secim == 'Bölme' or secim == 'bölme':
        print(" ")
        print(Fore.YELLOW + "===Bölme==========================================")
        sayi1 = float(input(Fore.LIGHTWHITE_EX + "1. Sayı: "))
        sayi2 = float(input(Fore.LIGHTWHITE_EX + "2. Sayı: "))
        print(sayi1,"/",sayi2,"=",end=" ")
        print(Fore.RED + str(Bol(sayi1,sayi2)))
        print(Fore.YELLOW + "==================================================")

    # Daire Çevre Hesaplama
    if secim == '6' or secim == 'Daire Çevre Hesaplama' or secim == 'daire çevre hesaplama':
        print(" ")
        print(Fore.YELLOW + "===Dairede Çevre==================================")
        sayi1 = float(input(Fore.LIGHTWHITE_EX + "YarıÇap: "))
        print(sayi1,"*","2","*","3,14","=",end=" ")
        print(Fore.RED + str(Cevre(sayi1)))    
        print(Fore.YELLOW + "==================================================")

    # Daire Alan Hesaplama
    if secim == '7' or secim == 'Daire Alan Hesaplama' or secim == 'daire alan hesaplama':
        print(" ")
        print(Fore.YELLOW + "===Dairede Alan===================================")
        sayi1 = float(input(Fore.LIGHTWHITE_EX + "YarıÇap: "))
        print(sayi1,"*",sayi1,"*","3,14","=",end=" ")
        print(Fore.RED + str(D_Alan(sayi1))) 
        print(Fore.YELLOW + "==================================================")

    # Üçgen Alan Hesaplama
    if secim == '8' or secim == 'Üçgen Alan Hesaplama' or secim == 'üçgen alan hesaplama':
        print(" ")
        print(Fore.YELLOW + "===Üçgende Alan===================================")
        sayi1 = float(input(Fore.LIGHTWHITE_EX + "Taban: "))
        sayi2 = float(input(Fore.LIGHTWHITE_EX + "Yükseklik: "))
        print(sayi1,"*",sayi2,"/","2","=",end=" ")
        print(Fore.RED + str(U_Alan(sayi1,sayi2))) 
        print(Fore.YELLOW + "==================================================")
    
    # Üs Alma
    if secim == '9' or secim == 'Üs Alma' or secim == 'üs alma':
        print(" ")
        print(Fore.YELLOW + "===Üs Alma========================================")
        sayi1 = float(input(Fore.LIGHTWHITE_EX + "Taban: "))
        sayi2 = float(input(Fore.LIGHTWHITE_EX + "Üs: "))
        print(sayi1,"**",sayi2,"=",end=" ")
        print(Fore.RED + str(Us(sayi1,sayi2))) 
        print(Fore.YELLOW + "==================================================")

    # Faktöriyel Hesaplama
    if secim == '10' or secim == 'Faktöriyel Hesaplama' or secim == 'faktöriyel hesaplama':
        print(" ")
        print(Fore.YELLOW + "===Faktöriyel=====================================")
        sayi1 = int(input(Fore.LIGHTWHITE_EX + "Sayı: "))
        if sayi1 < 0:
            print("Lütfen negatif bir tam sayı girmeyiniz.")
            print(Fore.YELLOW + "==================================================")
            continue
        else:
            print(sayi1,end=("!"))
            print(" =",end=" ")
            print(Fore.RED + str(Fak(sayi1)))
        print(Fore.YELLOW + "==================================================")

    # Poligon Alan Hesaplama
    if secim == '11' or secim == 'Poligon Alan Hesaplama' or secim == 'poligon alan hesaplama':
        print(" ")
        print(Fore.YELLOW + "===Poligonda Alan=================================")
        sayi1 = float(input(Fore.LIGHTWHITE_EX + "Kenar Sayısı: "))
        sayi2 = float(input(Fore.LIGHTWHITE_EX + "Kenar Uzunluğu: "))
        print("(1/4) *", sayi1,"*",sayi2,"*",sayi2,"=",end=" ")
        print(Fore.RED + str(Pol_Alan(sayi1,sayi2))) 
        print(Fore.YELLOW + "==================================================")

    # Poligon Çevre Hesaplama
    if secim == '12' or secim == 'Poligon Çevre Hesaplama' or secim == 'poligon çevre hesaplama':
        print(" ")
        print(Fore.YELLOW + "===Poligonda Çevre================================")
        sayi1 = int(input(Fore.LIGHTWHITE_EX + "Kenar Sayısı: "))
        sayi2 = float(input(Fore.LIGHTWHITE_EX + "Kenar Uzunluğu: "))
        print(sayi1,"*",sayi2,"=",end=" ")
        print(Fore.RED + str(Pol_Alan(sayi1,sayi2)))
        print(Fore.YELLOW + "==================================================")

    # Kare Kök Alma
    if secim == '13' or secim == 'Kare Kök' or secim == 'kare kök':
        print(" ")
        print(Fore.YELLOW + "===Kare Kök=======================================")
        sayi1 = float(input(Fore.LIGHTWHITE_EX + "Sayı: "))
        print(sayi1,"karekökü","=",end=" ")
        print(Fore.RED + str(Kare_Kok(sayi1)))
        print(Fore.YELLOW + "==================================================")

    # Hipotenüs Hesaplama
    if secim == '14' or secim == 'Hipotenüs Hesaplama' or secim == 'hipotenüs hesaplama':
        print(" ")
        print(Fore.YELLOW + "===Hipotenüs Hesaplama============================")
        sayi1 = int(input(Fore.LIGHTWHITE_EX + "A Kenarı: "))
        sayi2 = int(input(Fore.LIGHTWHITE_EX + "B Kenarı: "))
        print(sayi1,"²","+",sayi2,"²","=",end=" ")
        print(Fore.RED +  str(Hipo(sayi1,sayi2)),"²")
        print(Fore.YELLOW + "==================================================")

    # Ardışık Sayıların Toplamı
    if secim == '15' or secim == 'Ardışık Sayıların Toplamı' or secim == 'ardışık sayıların toplamı':
        print(" ")
        print(Fore.YELLOW + "===Ardışık Sayıların Toplamı======================")
        sayi1 = float(input(Fore.LIGHTWHITE_EX + "İlk Terim: "))
        sayi2 = float(input(Fore.LIGHTWHITE_EX + "Son Terim: "))
        sayi3 = float(input(Fore.LIGHTWHITE_EX + "Ardışık İki Terim Arası Fark: "))
        print("((",sayi2,"-",sayi1," ) /",sayi3,"+ 1) * ((",sayi2,"+",sayi1,") / 2 ) =",end=" ")
        print(Fore.RED +  str(Ard_Top(sayi1,sayi2,sayi3)))
        print(Fore.YELLOW + "==================================================")

    # Ardışık Sayıların Çarpımı
    if secim == '16' or secim == 'Ardışık Sayıların Toplamı' or secim == 'ardışık sayıların toplamı':
        print(" ")
        print(Fore.YELLOW + "===Ardışık Sayıların Çarpımı======================")
        sayi1 = int(input(Fore.LIGHTWHITE_EX + "İlk Terim: "))
        sayi2 = int(input(Fore.LIGHTWHITE_EX + "Son Terim: "))
        sayi3 = int(input(Fore.LIGHTWHITE_EX + "Ardışık İki Terim Arası Fark: "))
        print("Sonuç:",end=" ")
        print(Fore.RED +  str(Ard_Carp(sayi1,sayi2,sayi3)))
        print(Fore.YELLOW + "==================================================")

    # Onluk Sistemden İkilik Sisteme Çevirme
    if secim == '17' or secim == 'Onluk Sistemden İkilik Sisteme Çevirme' or secim == 'onluk sistemden ikilik sisteme çevirme':
        print(" ")
        print(Fore.YELLOW + "===Onluk Sistemden İkilik Sisteme=================")
        sayi1 = int(input(Fore.LIGHTWHITE_EX + "Decimal (Onlu): "))
        print("Binary (İkili):",end=" ")
        print(Fore.RED +  str(On_Iki(sayi1)))
        print(Fore.YELLOW + "==================================================")

    # İkilik Sistemden Onluk Sisteme Çevirme
    if secim == '18' or secim == 'İkilik Sistemden Onluk Sisteme Çevirme' or secim == 'ikilik sistemden onluk sisteme çevirme':
        print(" ")
        print(Fore.YELLOW + "===İkilik Sistemden Onluk Sisteme=================")
        sayi1 = int(input(Fore.LIGHTWHITE_EX + "Binary (İkili): "))
        print("Decimal (Onlu):",end=" ")
        print(Fore.RED +  str(Ikı_On(sayi1)))
        print(Fore.YELLOW + "==================================================")

    # Yardım
    if secim == 'yardım' or secim == 'help' or secim == 'Yardım' or secim == 'Help' or secim == '-2':
        print(" ")
        print(Fore.LIGHTBLUE_EX + "===Açıklama=======================================")
        print(Fore.LIGHTWHITE_EX + "Yapılacak İşlemi Seçin:")
        print(Fore.LIGHTWHITE_EX + "1-  Serbest Mod")
        print(Fore.LIGHTWHITE_EX + "2-  Toplama")
        print(Fore.LIGHTWHITE_EX + "3-  Çıkarma")
        print(Fore.LIGHTWHITE_EX + "4-  Çarpma")
        print(Fore.LIGHTWHITE_EX + "5-  Bölme")
        print(Fore.LIGHTWHITE_EX + "6-  Daire Çevre Hesaplama")
        print(Fore.LIGHTWHITE_EX + "7-  Daire Alan Hesaplama")
        print(Fore.LIGHTWHITE_EX + "8-  Üçgen Alan Hesaplama")
        print(Fore.LIGHTWHITE_EX + "9-  Üs Alma")
        print(Fore.LIGHTWHITE_EX + "10- Faktöriyel Hesaplama")
        print(Fore.LIGHTWHITE_EX + "11- Poligon Alan Hesaplama")
        print(Fore.LIGHTWHITE_EX + "12- Poligon Çevre Hesaplama")
        print(Fore.LIGHTWHITE_EX + "13- Kare Kök Alma")
        print(Fore.LIGHTWHITE_EX + "14- Hipotenüs Hesaplama")
        print(Fore.LIGHTWHITE_EX + "15- Ardışık Sayıların Toplamı")
        print(Fore.LIGHTWHITE_EX + "16- Ardışık Sayıların Çarpımı")
        print(Fore.LIGHTWHITE_EX + "17- Onluk Sistemden İkilik Sisteme Çevirme")
        print(Fore.LIGHTWHITE_EX + "18- İkilik Sistemden Onluk Sisteme Çevirme")
        print(Fore.LIGHTBLUE_EX + "==================================================")
        continue

    # Bitirme
    if secim == 'bitir' or secim == 'Bitir' or secim == 'end' or secim == 'End' or secim == '-1':
        print(Fore.LIGHTCYAN_EX + """
              
|==================Teşekkürler===================|
|                                                |
|              Mustafa Emre KILIÇ                |
|               Ahmet Talha KAÇAR                |
|                  Mualla AŞIK                   |
|                                                |
|================================================|
""")
        print(Fore.LIGHTRED_EX + """
|================================================|
|                                                |
|               Mazhar Berk AYDOĞDU              |
|                  Made in Turkey                |
|                                                |
|================================================|
""")
        break