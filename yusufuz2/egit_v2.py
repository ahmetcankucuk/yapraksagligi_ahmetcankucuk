from ultralytics import YOLO

# Windows'ta multiprocessing hatası almamak için zorunlu blok
if __name__ == '__main__':
    
    # Görüntü sınıflandırma için YOLOv8 Small modelini yüklüyoruz (-cls uzantısına dikkat)
    model = YOLO('yolov8s-cls.pt')

    # Modeli eğitiyoruz
    results = model.train(
        data='C:/yusufuz2/dataset',  # Oluşturduğumuz bölünmüş verilerin ana klasörü
        epochs=50,                   # 50 tur başlangıç için iyi bir seviye
        imgsz=224,                   # Sınıflandırma modelleri için standart ve en hızlı çözünürlük 224'tür
        device='0',                  # Ekran kartını kullan
        batch=32,                    # Ekran kartının hafızası geniş olduğu için 32'ye çıkardık, daha hızlı eğitir
        project='C:/yusufuz2/runs',  
        name='plantvillage_model'    
    )