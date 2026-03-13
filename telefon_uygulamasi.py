tel_rehberi = dict()

def tel_no_ekle(x):

    print("-"*30)
    print("Kayıt Ekranına Hoşgeldiniz")
    print("-"*30)

    numara_isim_al = input("Kaydedilecek Kişinin Adını Girin: ")
    numara_no_al = int(input("Telefon Numarasını Girin: "))
  
    x = tel_rehberi.setdefault(numara_isim_al,numara_no_al)
    print(f"{numara_isim_al} Adlı Kişi Rehbere Eklendi.")


def tel_rehber_göster(x):
    print("-"*30)
    print("REHBER")
    print("-"*30)

    for i,d in x.items():
        print(i,":",d)


def tel_no_sil(x):
    print("-"*30)
    print("Kişi Silme Ekranına Hoşgeldiniz")
    print("-"*30)

    sil_kisi = input("Silinicek Kişiyi Girin: ")
    x = tel_rehberi.pop(sil_kisi)

    print(f"{sil_kisi} Adlı Kişi Silindi.")

while True:
    print("-"*30)
    print("HOŞGELDİNİZ")
    print("-"*30)
    print("Bir İşlem Seçiniz")
    secim = int(input("1-Kayıt\n2-Kişi Silme\n3-Rehberi Görüntüle\n4-Çıkış\n"))

    if secim == 1:
        tel_no_ekle(tel_rehberi)

    elif secim == 2:
        tel_no_sil(tel_rehberi)

    elif secim == 3:
        tel_rehber_göster(tel_rehberi)
        
    elif secim == 4:
        print("Çıkış Yapıldı...")
        break