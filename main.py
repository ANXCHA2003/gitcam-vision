import cv2

def main():
    # โหลดโมเดล Haar Cascade จาก OpenCV โดยตรง
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    )

    # เปิดกล้อง
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    if not cap.isOpened():
        print("❌ ไม่สามารถเปิดกล้องได้")
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

        # วาดกรอบรอบใบหน้า
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # แสดงจำนวนใบหน้าที่ตรวจพบ
        cv2.putText(frame, f"Faces: {len(faces)}", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow('GitCam Face Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('0'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
