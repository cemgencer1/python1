print("**************** HESAP MAKİNESİ ****************")

print("1-Toplama İşlemi\n2-Çıkarma İşlemi\n3-Çarpma İşlemi\n4-Bölme İşlemi")
print("*******************************")
işlem = int(input("Yapacağınız İşlemi Giriniz :"))
a = int(input("1.Sayıyı Giriniz :"))
b = int(input("2.Sayıyı Giriniz :"))
print("*******************************")
if (işlem==1):
    c = a+b
    print("İşlem Sonucunuz :",c )
elif (işlem==2):
    c=a-b
    print("İşlem Sonucunuz :",c )
elif (işlem==3):
    c=a*b
    print("İşlem Sonucunuz :",c)
elif (işlem==4):
    c=a/b
    print("İşlem Sonucunuz :",c)
else:
    print("Hatalı İşlem Seçtiniz ...")
print("Hoşçakalın ...")
