#  Python veri tipleri:
#     •	Integer : Sayisal veriler.
#     •	String : Metinsel veya karakter tipleri.
#     •	Float : Ondalikli sayi tipleri.
#     •	Boolean : True ve false değer döndürür.
#     •	List : Birden çok ögeyi tutan yapidir "[]" kullanilir.
#     •	Dictionary: Key ve values çiftinden oluşur ve "{}" kullanilir.
# Kodlama.io sitesinde değişken olarak kullanildiğini düşündüğünüz verileri, veri tipleriyle birlikte örneklendiriniz:
#     •	Kategori ve eğitimler listedir.
#     •	Ders tamamlama yüzdeleri integerdır.
#     •	Kurs programi listedir.
#     •	Kurs isimleri stringdir.


email_address="oguzhan@gmail.com"
password=12345

email=input("please enter your e-mail address:")
password1=int(input("please enter your password:"))

if email_address==email and password==password1:
    print ("login successsful")
else:
    print("email or password is wrong try again")

#pythonda ders adları string değerlere sahiptir.
#dersteki ilerleme ise integer değere sahiptir.
#dersteki ilerlemeyi de şart bloğu gibi düşünebiliriz.
derssayisi=100
bitirilenderssayisi=80
yuzde="80%"
print("ders ilerlemeniz="+yuzde)