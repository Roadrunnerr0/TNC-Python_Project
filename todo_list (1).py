"""
================================================================================
TO-DO LIST (GÖREV YÖNETİM) UYGULAMASI
================================================================================
PROJE AÇIKLAMASI
================================================================================
Bu uygulama, kullanıcıların görevlerini yönetmelerine olanak tanıyan basit bir
To-Do List (Görev Yönetim) uygulamasıdır. Uygulama, Python programlama dili
kullanılarak geliştirilmiştir ve temel programlama kavramlarını içermektedir.

================================================================================
TEMEL ÖZELLİKLER
================================================================================
1. Görev Ekleme: Yeni görevler eklenebilir (boş görev eklenemez)
2. Görev Listeleme: Mevcut görevler numaralı şekilde listelenir
3. Görev Düzenleme: Görevler numaralarına göre düzenlenebilir
4. Görev Silme: Görevler numaralarına göre silinebilir
5. Dosya İşlemleri: Görevler UTF-8 kodlamasıyla metin dosyasına kaydedilir
6. Hata Kontrolü: Kullanıcı girdileri try-except blokları ile kontrol edilir
7. Otomatik Kaydetme: Her değişiklikten sonra görevler otomatik kaydedilir

================================================================================
"""

import os

# Dosya adı
DOSYA_ADI = "gorevler.txt"

def gorevleri_yukle():
    """
    Görevleri dosyadan yükler.
    Eğer dosya yoksa veya okunamazsa boş liste döner.
    """
    gorevler = []
    try:
        if os.path.exists(DOSYA_ADI):
            with open(DOSYA_ADI, "r", encoding="utf-8") as dosya:
                gorevler = [satir.strip() for satir in dosya.readlines() if satir.strip()]
            return gorevler, True
        else:
            return gorevler, False
    except Exception as e:
        return gorevler, False

def gorevleri_kaydet(gorevler):
    """
    Görevleri dosyaya kaydeder.
    """
    try:
        with open(DOSYA_ADI, "w", encoding="utf-8") as dosya:
            for gorev in gorevler:
                dosya.write(gorev + "\n")
        return True
    except Exception as e:
        print(f"Dosya yazma hatası: {e}")
        return False

def gorevleri_listele(gorevler):
    """
    Görevleri numaralandırılmış şekilde listeler.
    """
    if not gorevler:
        print("Henüz görev bulunmamaktadır.")
    else:
        print("\n--- GÖREV LİSTESİ ---")
        for i, gorev in enumerate(gorevler, 1):
            print(f"{i}. {gorev}")

def yeni_gorev_ekle(gorevler):
    """
    Kullanıcıdan yeni görev alır ve listeye ekler.
    Boş görev eklenmesine izin verilmez.
    """
    yeni_gorev = input("Yeni görev: ").strip()
    
    if not yeni_gorev:
        print("Boş görev eklenemez!")
        return False
    
    gorevler.append(yeni_gorev)
    gorevleri_kaydet(gorevler)
    print(f"'{yeni_gorev}' görevi eklendi ve kaydedildi.")
    return True

def gorev_duzenle(gorevler):
    """
    Kullanıcıdan görev numarası alır ve görevi düzenler.
    Geçersiz numara veya boş görev kontrolü yapar.
    """
    if not gorevler:
        print("Henüz görev bulunmamaktadır.")
        return False
    
    gorevleri_listele(gorevler)
    
    try:
        gorev_numarasi = input("\nDüzenlemek istediğiniz görevin numarası: ").strip()
        gorev_numarasi = int(gorev_numarasi)
        
        if gorev_numarasi < 1 or gorev_numarasi > len(gorevler):
            print("Geçersiz görev numarası!")
            return False
        
        mevcut_gorev = gorevler[gorev_numarasi - 1]
        yeni_gorev = input(f"Yeni görev metni ({mevcut_gorev}): ").strip()
        
        if not yeni_gorev:
            print("Boş görev eklenemez!")
            return False
        
        gorevler[gorev_numarasi - 1] = yeni_gorev
        gorevleri_kaydet(gorevler)
        print("Görev başarıyla güncellendi ve kaydedildi.")
        return True
            
    except ValueError:
        print("Lütfen bir sayı girin!")
        return False
    except Exception as e:
        print(f"Hata oluştu: {e}")
        return False

def gorev_sil(gorevler):
    """
    Kullanıcıdan görev numarası alır ve görevi siler.
    Geçersiz numara kontrolü yapar.
    """
    if not gorevler:
        print("Henüz görev bulunmamaktadır.")
        return False
    
    gorevleri_listele(gorevler)
    
    try:
        gorev_numarasi = input("\nSilmek istediğiniz görevin numarası: ").strip()
        gorev_numarasi = int(gorev_numarasi)
        
        if gorev_numarasi < 1 or gorev_numarasi > len(gorevler):
            print("Geçersiz görev numarası!")
            return False
        
        silinen_gorev = gorevler.pop(gorev_numarasi - 1)
        gorevleri_kaydet(gorevler)
        print(f"'{silinen_gorev}' görevi silindi ve kaydedildi.")
        return True
            
    except ValueError:
        print("Lütfen bir sayı girin!")
        return False
    except Exception as e:
        print(f"Hata oluştu: {e}")
        return False

def ana_menu_goster():
    """
    Ana menüyü ekrana yazdırır.
    """
    print("\n--- TO-DO LIST UYGULAMASI ---")
    print("1. Görevleri Listele")
    print("2. Yeni Görev Ekle")
    print("3. Görev Düzenle")
    print("4. Görev Sil")
    print("5. Çıkış")

def main():
    """
    Ana program fonksiyonu.
    """
    print("To-Do List Uygulamasına Hoş Geldiniz!")
    
    # Görevleri yükle
    gorevler, _ = gorevleri_yukle()
    
    # Ana döngü
    while True:
        ana_menu_goster()
        secim = input("\nSeçiminiz (1-5): ").strip()
        
        if secim == "1":
            gorevleri_listele(gorevler)
        elif secim == "2":
            yeni_gorev_ekle(gorevler)
        elif secim == "3":
            gorev_duzenle(gorevler)
        elif secim == "4":
            gorev_sil(gorevler)
        elif secim == "5":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim! Lütfen 1-5 arası bir sayı girin.")

if __name__ == "__main__":
    main()

