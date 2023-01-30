print("""
*******************************
Atm Programına Hoşgeldiniz ...
İşlemler :
1 - Bakiye Sorma 
2 - Para Çekme 
3 - Para Yatırma
Çıkmak İçin 'q' ya basınız ...
*******************************
""")
bakiye = 1000
while True:
    işlem = input("Yapacağınız İşlemi Seçiniz :")
    if(işlem=="q"):
        break
    elif(işlem=="1"):
        print("Bakiyeniz :" , bakiye)
    elif(işlem=="2"):
        x=int(input("Çekilecek Miktarı Giriniz :"))
        if(bakiye-x<0):
            print("Bu Miktar Çekilemez.Bakiyenizden Fazla Miktar Girdiniz...")
            continue
        bakiye-=x
        print("Yeni Bakiyeniz :",bakiye)
    elif(işlem=="3"):
        y=int(input("Yatırılacak Miktarı Giriniz :"))
        bakiye+=y
        print("Yeni Bakiyeniz :",bakiye)
    else:
        print("Hatalı İşlem Seçimi Yaptınız.Tekrar Deneyiniz...")