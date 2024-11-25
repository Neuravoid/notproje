# 📘 Öğrenci Yönetim Sistemi

Bu Python projesi, öğrenci yönetimi için basit bir sistem sunar. Kullanıcı, öğrenci ekleme, listeleme, sorgulama ve harf notu hesaplama gibi işlemleri gerçekleştirebilir. Öğrenci bilgileri yerel bir dosyaya kaydedilir.

---

## 📋 Özellikler

1. **Öğrenci Ekleme**
   - Yeni bir öğrenci eklenir, benzersiz bir öğrenci numarası oluşturulur.
   - Ad, soyad, vize ve final notları girilir. Ağırlıklı ortalama (vize %40, final %60) hesaplanır.
   - Öğrenciler `nothesapla.txt` dosyasına kaydedilir.

2. **Öğrenci Listesi**
   - Kayıtlı tüm öğrenciler `nothesapla.txt` dosyasından okunarak listelenir.

3. **Öğrenci Sorgulama**
   - Öğrenci numarasına göre bir öğrencinin bilgileri sorgulanabilir.

4. **Harf Notu Hesaplama**
   - Öğrenci ağırlıklı ortalamaları `nothesapla.txt` dosyasından alınır.
   - Harf notları belirlenir ve kullanıcı tarafından belirtilen bir dosyaya kaydedilir.

5. **Çıkış**
   - Program kullanıcı isteğiyle sonlandırılabilir.

---

## 🛠️ Gereksinimler

- Python 3.6 veya üzeri
- `nothesapla.txt` dosyasının oluşturulabilir olması

---

## 🚀 Kullanım

1. Projeyi bir dosya (ör. `ogrenci_yonetim.py`) olarak kaydedin.
2. Programı çalıştırmak için terminalde şu komutu çalıştırın:
   ```bash
   python ogrenci_yonetim.py
