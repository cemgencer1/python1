
def tambolenbulma(sayı):
    tam_bolenler=[]
    for i in range (1,sayı+1):
        if (sayı % i == 0):
            tam_bolenler.append(i)
    return tam_bolenler
while True:
    sayı = input("Bir Sayı Giriniz :")
    if (sayı == "q"):
        print("Program Sonlandırılıyor ...")
        break
    else :
        sayı = int(sayı)
        print("Girilen Sayının Tam Bölenleri :",tambolenbulma(sayı))