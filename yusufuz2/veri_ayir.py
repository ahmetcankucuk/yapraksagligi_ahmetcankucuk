import splitfolders

# ham_veri klasöründeki fotoğrafları alıp, 'dataset' adında yeni bir klasöre bölecek
girdi_klasoru = "C:/yusufuz2/ham_veri"
cikti_klasoru = "C:/yusufuz2/dataset"

print("Veriler ayrılıyor, lütfen bekleyin...")

# Veriyi %80 eğitim (train), %20 doğrulama (val) olarak ayırıyoruz
splitfolders.ratio(girdi_klasoru, output=cikti_klasoru, seed=42, ratio=(0.8, 0.2), group_prefix=None)

print("İşlem tamamlandı! Veriler 'dataset' klasörüne başarıyla bölündü.")