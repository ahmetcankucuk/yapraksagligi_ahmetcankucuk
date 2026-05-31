"Projenin ilk aşamasında, birinci veri seti kullanılarak %85 eğitim (train) ve %15 doğrulama (val/test) oranında bir bölünme gerçekleştirilmiş ve 50 epoch (tekrar) boyunca YOLOv8n-cls (Nano) modeli eğitilmiştir. Ancak elde edilen test ve doğrulama sonuçları hedeflenen başarı kriterlerini karşılayamamıştır.

Bu performans darboğazını aşmak amacıyla, literatürde bitki hastalıkları için standart kabul edilen PlantVillage veri setine geçiş yapılmıştır. Veri seti kalitesinin artırılmasına ek olarak, modelin öğrenme kapasitesini (kapasitansını) yükseltmek adına daha derin bir mimari olan YOLOv8s-cls (Small) modeli tercih edilmiştir. Bu stratejik değişiklik, eğitim metriklerinde ve modelin genelleme yeteneğinde çok daha başarılı ve kararlı sonuçlar doğurmuştur."

Grafik Analizi (Raporuna Ekleyebileceğin Yeni Paragraf)
results.png dosyasında yer alan 50 epoch'luk eğitim ve doğrulama grafiklerinin teknik analizi şu şekildedir:

📉 Kayıp (Loss) Grafikleri Analizi
train/box_loss, train/cls_loss, train/dfl_loss: Eğitim sürecindeki kutu (box), sınıflandırma (cls) ve dağılım odaklı (dfl) kayıp değerlerinin tamamı 50 epoch boyunca istikrarlı bir şekilde aşağı doğru ivmelenmiştir. Bu durum, modelin eğitim verisindeki özellikleri başarıyla öğrendiğini gösterir.

val/box_loss, val/cls_loss, val/dfl_loss: Doğrulama (validation) kayıpları ilk birkaç epoch'taki dalgalanmanın ardından kararlı bir düşüş trendine girmiştir. Özellikle sınıflandırma kaybının (val/cls_loss) taban seviyelerde (1.5 civarı) düzleşmesi ve yukarı doğru keskin bir kırılma yapmaması, modelde kritik bir aşırı öğrenme (overfitting) problemi olmadığını kanıtlamaktadır.

📊 Başarı (Metric) Grafikleri Analizi
Precision ve Recall: Keskinlik (Precision) grafiği %55 seviyelerine, Duyarlılık (Recall) grafiği ise %50 civarına kararlı bir salınımla ulaşmıştır. İlk veri setindeki başarısızlığa kıyasla modelin pozitif sınıfları ayırt etme yeteneği net bir şekilde yükselmiştir.

mAP50 ve mAP50-95 Başarısı: Modelin asıl kalitesini gösteren Ortalama Ortalama Hassasiyet (mAP) değerleri oldukça tatminkar bir eğri çizmektedir. metrics/mAP50(B) metriği %52 seviyesini aşarak plato çizmeye başlamıştır. Daha katı bir değerlendirme kriteri olan metrics/mAP50-95(B) ise %35'in üzerine çıkarak eğitim sonuna kadar artış eğilimini korumuştur.

.<img width="2400" height="1200" alt="results" src="https://github.com/user-attachments/assets/f2381613-9ab7-4abc-81bb-673bc89a2cf6" />
