print("""*************************

Girilen Sayıları Toplama

Çıkmak için 'q' ya basınız...

*************************""")
toplam = 0
while True:
    sayı=input("Toplanacak Sayıyı Giriniz :")
    if (sayı=="q"):
        print("Programdan Çıkılıyor ...")
        break
    sayı=int(sayı)
    toplam+=sayı
print("Girilen Sayıların Toplamı :",toplam)
