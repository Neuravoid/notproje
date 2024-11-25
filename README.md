# Öğrenci Yönetim Sistemi

Bu Python programı, bir öğrenci yönetim sistemi sağlayarak öğrenci ekleme, listeleme, sorgulama ve harf notu hesaplama gibi işlemleri yapmanıza olanak tanır. Programın amacı, kullanıcı dostu bir arayüzle öğrenci bilgilerini düzenli bir şekilde kaydetmek ve yönetmektir.

---

## 📋 Özellikler

1. **Öğrenci Ekleme**  
   - Yeni bir öğrenci eklenir ve benzersiz bir öğrenci numarası oluşturulur.  
   - Öğrenci bilgileri (ad, soyad, vize, final) girilir ve ağırlıklı ortalama hesaplanır.
   - Öğrenciler `nothesapla.txt` dosyasına kaydedilir.

2. **Öğrenci Listesi**  
   - `nothesapla.txt` dosyasındaki tüm öğrenciler listelenir.

3. **Öğrenci Sorgulama**  
   - Öğrenci numarasına göre bir öğrencinin bilgileri sorgulanır.

4. **Harf Notu Oluşturma**  
   - `nothesapla.txt` dosyasındaki ağırlıklı ortalamalar baz alınarak harf notları hesaplanır ve belirtilen dosyaya kaydedilir.

---

## 🛠️ Kullanım

### Ana Menü
Program çalıştırıldığında aşağıdaki menü görüntülenir:

### Ana Menü
Program çalıştırıldığında aşağıdaki menü görüntülenir:


Ana Menü
1. Öğrenci Ekle
2. Öğrenci Listesi
3. Öğrenci Sorgula
4. Harf Notu Oluştur
5. Çıkış

Seçeneklere göre işlem yapabilirsiniz.

### İşlevlerin Açıklamaları
1. **Öğrenci Ekle**  
   Yeni bir öğrenci eklemek için `1` girilir.  
   Öğrenci bilgilerini girdikten sonra program bu bilgileri kaydeder.

2. **Öğrenci Listesi**  
   Mevcut öğrencileri listelemek için `2` girilir.

3. **Öğrenci Sorgula**  
   Belirli bir öğrenci numarasına ait bilgileri görmek için `3` girilir.

4. **Harf Notu Oluştur**  
   Harf notlarını oluşturmak için `4` girilir. Harf notları belirtilen dosyaya kaydedilir.

5. **Çıkış**  
   Programdan çıkmak için `5` girilir.

---

## 📂 Dosya Yapısı

- **nothesapla.txt**: Öğrenci bilgileri bu dosyaya kaydedilir.
- **Harf Notu Dosyası**: Harf notları belirttiğiniz dosya adına kaydedilir.

---

## 🔧 Gereksinimler

- Python 3.6 veya üzeri
- Bir metin düzenleyici veya IDE

---

## 📝 Notlar

- Öğrenci numaraları benzersiz olarak atanır.
- Harf notu hesaplamasında ağırlıklı ortalama şu şekilde hesaplanır:
- Ağırlıklı Ortalama = Vize * 0.4 + Final * 0.6

- Harf notu aralıkları:
| Ağırlıklı Ortalama | Harf Notu |
|--------------------|-----------|
| 90-100            | AA        |
| 85-89             | AB        |
| 80-84             | BA        |
| 75-79             | BB        |
| 70-74             | BC        |
| 65-69             | CC        |
| 60-64             | CD        |
| 50-59             | DD        |
| 0-49              | FF        |

---

## 🚀 Programı Çalıştırma

1. Programı indirin veya kopyalayın.
2. Komut satırında veya IDE'de çalıştırın:
 ```bash
 python program_adi.py

