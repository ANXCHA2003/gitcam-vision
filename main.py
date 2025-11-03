import cv2

def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("ไม่สามารถเปิดกล้องได้")
        return

    print("กด 's' เพื่อบันทึกเฟรม, '0' เพื่อออก.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("ไม่สามารถอ่านเฟรมได้")
            break

        cv2.imshow('กล้อง', frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('s'):
            cv2.imwrite('captured_frame.jpg', frame)
            print("บันทึกเฟรมเป็น 'captured_frame.jpg'")
        elif key == ord('0'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()