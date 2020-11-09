#iki basamaklı sayılar için
a = int(input("Bir adet sayı giriniz."))
onlar_basamagı = a // 10
print("sayının onlar basamagı = ", onlar_basamagı)
birler_basamagı = a % 10
print("sayının birler basamağı = ", birler_basamagı)
c = birler_basamagı + onlar_basamagı
print("Son iki basamağın toplamı = ", c)