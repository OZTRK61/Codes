import json # Sözlükleri metne, metinleri sözlüğe çevirir
def rehberi_kaydet():
    with open("rehberim.json", "w", encoding="utf-8") as dosya:
        # json.dump -> Sözlüğü dosyaya yazar
        # indent=4 -> Dosyanın içinde verileri güzelce hizalar
        json.dump(rehber, dosya, indent=4, ensure_ascii=False)
    print("Rehber 'rehberim.json' dosyasına kaydedildi!")
def rehberi_yukle():
    global rehber # Fonksiyon dışındaki rehber değişkenini güncellemek için
    try:
        with open("rehberim.json", "r", encoding="utf-8") as dosya:
            # json.load -> Dosyadaki metni tekrar sözlüğe çevirir
            rehber = json.load(dosya)
        print("Veriler dosyadan başarıyla yüklendi.")
    except FileNotFoundError:
        # Eğer dosya henüz yoksa (ilk çalıştırma), boş bir sözlükle başla
        rehber = {}
        print("Kayıtlı dosya bulunamadı, yeni bir rehber oluşturuldu.")