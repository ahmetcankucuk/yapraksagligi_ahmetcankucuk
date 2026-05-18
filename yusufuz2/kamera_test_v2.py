import cv2
from ultralytics import YOLO

if __name__ == '__main__':
    # Eğittiğin yeni sınıflandırma modelini yükle
# Eski hatalı yol buydu: 'C:\\yusufuz2\\runs\\plantvillage_model\\weights\\best.pt'

# Başına 'r' koyarak yeni güncel yolu yaz:
    model_yolu = r"C:\yapraksagligi\yusufuz2\runs\plantvillage_model\weights\best.pt"
    
    model = YOLO(model_yolu)

    # Kamerayı başlat
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Kamera açılamadı!")
        exit()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Görüntüyü modele ver
        results = model(frame)

        # Sınıflandırma modellerinde plot() fonksiyonu tahmin edilen hastalığın adını ve olasılığını sol üst köşeye yazar
        annotated_frame = results[0].plot()

        cv2.imshow("PlantVillage Hastalik Sınıflandırma", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()