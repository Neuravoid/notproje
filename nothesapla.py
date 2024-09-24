import random

def ogrenci_ekle():
    lis1 = []
    sayac = 0
    ogrenci_numaralari = set()  # Benzersiz öğrenci numaraları için set

    while sayac == 0:
        ad = input("Öğrencinin adını giriniz: ")
        soyad = input("Öğrencinin soyadını giriniz: ")
        vize = float(input("Öğrencinin vize notunu giriniz: "))
        final = float(input("Öğrencinin final notunu giriniz: "))
        
        ao = vize * 0.4 + final * 0.6
        unique = random.randint(1, 1000)

        # Benzersiz öğrenci numarasını kontrol et
        while unique in ogrenci_numaralari:
            unique = random.randint(1, 1000)
        ogrenci_numaralari.add(unique)

        bilgi1 = {"Ad": ad, "Soyad": soyad, "Vize": vize, "Final": final, "Ağırlıklı Ortalama": ao}
        bilgi2 = {unique: bilgi1}
        lis1.append(bilgi2)
        print(f"Yeni öğrenci eklendi: {bilgi2}")
        
        karar = input("Başka bir öğrenci eklemek ister misiniz? (e/h): ")
        if karar.lower() == 'h':
            sayac += 1

    # Eklenen öğrencileri dosyaya kaydet
    with open("nothesapla.txt", "a", encoding="utf-8") as file:
        for i in bilgi2:
            kaynak = bilgi2[i]
            file.write(f"Öğrenci No: {i}, Ad Soyad: {kaynak['Ad']} {kaynak['Soyad']}, Vize: {kaynak['Vize']}, Final: {kaynak['Final']}, Ağırlıklı Ortalama: {kaynak['Ağırlıklı Ortalama']:.2f}\n")

    print("Öğrenci bilgileri başarıyla kaydedildi!")

def ogrenci_listesi():
    with open("nothesapla.txt", "r", encoding="utf-8") as file:
        print("Öğrenci Listesi:")
        for line in file:
            print(line.strip())

def ogrenci_sorgula():
    with open("nothesapla.txt", "r", encoding="utf-8") as file:
        no = int(input("Öğrenci No giriniz: "))
        liste = file.readlines()
        
        for line in liste:
            if int(line.split(",")[0].split(":")[1].strip()) == no:
                print("Öğrenci Bilgileri:", line.strip())
                return
        print("Bu numaraya sahip bir öğrenci bulunamadı.")

def harf_notu():
    isim = input("Aktarmak istediğiniz belgenin ismini giriniz: ")
    notlar = {}
    with open("nothesapla.txt", "r", encoding="utf-8") as file:
        for line in file:
            parts = line.split(",")
            ogr_no = int(parts[0].split(":")[1].strip())
            ao = float(parts[-1].split(":")[1].strip())
            notlar[ogr_no] = ao
    
    # Harf notlarını ve ağırlıklı ortalamaları yazma işlemi
    with open(isim, "a+", encoding="utf-8") as file:
        for ogr_no, ao in notlar.items():
            if ao >= 90:
                harf = "AA"
            elif ao >= 85:
                harf = "AB"
            elif ao >= 80:
                harf = "BA"
            elif ao >= 75:
                harf = "BB"
            elif ao >= 70:
                harf = "BC"
            elif ao >= 65:
                harf = "CC"
            elif ao >= 60:
                harf = "CD"
            elif ao >= 50:
                harf = "DD"
            else:
                harf = "FF"
            file.write(f"Öğrenci No: {ogr_no}, Ağırlıklı Ortalama: {ao:.2f}, Harf Notu: {harf}\n")
    
    # Dosyadaki içeriği yazdır
    print("Harf Notları Belgesi:")
    with open(isim, "r", encoding="utf-8") as file:
        for line in file:
            print(line.strip())

# Ana menü
while True:
    print("\nAna Menü")
    print("1. Öğrenci Ekle")
    print("2. Öğrenci Listesi")
    print("3. Öğrenci Sorgula")
    print("4. Harf Notu Oluştur")
    print("5. Çıkış")

    a = input("Lütfen bir seçenek seçiniz (1/2/3/4/5): ")
    
    if a == '1':
        ogrenci_ekle()
    elif a == '2':
        ogrenci_listesi()
    elif a == '3':
        ogrenci_sorgula()
    elif a == '4':
        harf_notu()
    elif a == '5':
        print("Programdan çıkılıyor...")
        break
    else:
        print("Geçersiz bir seçenek girdiniz, lütfen tekrar deneyin.")
