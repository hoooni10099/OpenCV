import cv2 as cv

cap = cv.VideoCapture(0) # 600X480
if not cap.isOpened():
    print("camera open failed")
    exit()
while True:
    ret, img = cap.read()
    if not ret:
        print("Can't read camera")
        break

    cv.imshow('PC_camera', img)
    if cv.waitKey(1) == ord('c'): # 스페이스바 아스키코드 32
        img_captured = cv.imwrite('img_captured.png', img)
    

        src = cv.imread('img_captured.png', cv.IMREAD_COLOR)
        gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

        sobel = cv.Sobel(gray, cv.CV_8U, 1, 0, 3)

        cv.imshow("Sobel", sobel)

        img_cap = cv.imwrite('img_cap.png', sobel)

    if cv.waitKey(1) == ord('q'):
        break


cap.release()
cv.destroyAllWindows()
