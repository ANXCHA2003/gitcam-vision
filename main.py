import cv2

def main():
    # โหลดโมเดลตรวจจับหน้า
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    # เปิดกล้อง
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    if not cap.isOpened():
        print("ไม่สามารถเปิดกล้องได้")
        return

    print("ระบบตรวจจับใบหน้าเริ่มทำงาน (กด '0' เพื่อออก)")

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        # แปลงภาพเป็นขาวดำ
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # ตรวจจับใบหน้า
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        # วาดกรอบรอบใบหน้าที่ตรวจจับได้
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # แสดงผลภาพ
        cv2.imshow('กล้อง', frame)

        # กด 0 เพื่อออก
        if cv2.waitKey(1) & 0xFF == ord('0'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()