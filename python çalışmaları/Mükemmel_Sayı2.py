def mükemmelsayıbulma(sayı):
    toplam=0
    for i in range (1,sayı):
        if (sayı % i == 0):
            toplam += i
    print("Sayıların Toplamı :",toplam)
    if (sayı==toplam):
        print("Sayı Mükemmel Sayıdır...")
    else :
        print("Sayı Mükemmel Sayı Değildir ...")
    return toplam
while True:
    sayı = input("Sayı Giriniz :")
    if (sayı == "q"):
        print("Program Sonlandırılıyor ...")
        break
    sayı = int(sayı)
    if (sayı < 0 and sayı > 1000):
        print("Girilen Sayı Limit Dışıdır...")
        break
    else :
        print(mükemmelsayıbulma(sayı))
