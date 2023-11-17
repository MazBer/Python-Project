# Giriş
print("""
|===============================|
|                               |
|      Dörtgen Çizme Aracı      |
|           Sürüm 1.1           |
|                               |
|===============================|
""")

# Kullanıcıdan Veri Alınması
print("===Seçim=======================")
uzunluk = int(input("Uzunluk giriniz:"))
yukseklik = int(input("Yükseklik giriniz:"))
uzunluk2 = uzunluk
print("===============================")
print(" ")
print(" ")

# Dörtgen Hakkında Bilgiler
print("===Bilgiler====================")
print("Çevre:",(uzunluk+yukseklik)*2)
print("Alan:",uzunluk*yukseklik)
print("===============================")
print(" ")
print(" ")

# Üst Kenarı Çizme
print(" ",end="")
while uzunluk > 0:
    print("=",end="")
    uzunluk = uzunluk - 1
    if uzunluk == 1:
        print("=")
        break

# Sağ ve Sol Kenarları Çizme
while yukseklik > 0:
    print("|" , " " * (uzunluk2-2) , "|")
    yukseklik = yukseklik - 1

# Alt Kenarı Çizme
print(" ",end="")
while uzunluk2 > 0:
    print("=",end="")
    uzunluk2 = uzunluk2 - 1
    if uzunluk2 == 1:
        print("=")
        break

# Bitirme
print(" ")
print("""
|===============================|
|                               |
|      Mazhar Berk AYDOĞDU      |
|         Made in Turkey        |
|                               |   
|===============================|
""")