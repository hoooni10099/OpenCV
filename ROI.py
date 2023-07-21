import cv2 as cv
import numpy as np

isDragging = False # 마우스 드래그 상태 저장
x0, y0, w, h = -1, -1, -1, -1 # 영역 선택 좌표 저장
blue, red = (255, 0, 0), (0, 0, 255) # 색상 값

def onMouse(event, x, y, flage, param): # 마우스 이벤트 핸들 함수
    global isDragging, x0, y0, img # 전역 변수 참조
    if event == cv.EVENT_LBUTTONDOWN: # 왼쪽 마우스 버튼 다운, 드래그 시작
        isDragging = True
        x0 = x
        y0 = y

    elif event == cv.EVENT_MOUSEMOVE: # 마우스 움직임
        if isDragging: # 드래그 진행 중
            img_draw = img.copy() # 사각형 그림 표현을 위한 이미지 복제 (매번 같은 이미지에 그려지면 이미지가 더러워짐)
            cv.rectangle(img_draw, (x0, y0), (x, y), blue, 2) # 드래그 진행 영역 표시
            cv.imshow('img', img_draw)

    elif event == cv.EVENT_LBUTTONUP: # 왼쪽 마우스 버튼 업
        if isDragging: # 드래그 중지
            isDragging = False
            w = x - x0 # 드래그 영역 폭 계산
            h = y - y0 # 드래그 영역 높이 계산
            print("x%d, y%d, w%d, h%d" % (x0, y0, w, h))
            if w > 0 and h > 0: # 폭과 높이가 양수이면 드래그 방향이 옳음
                img_draw = img.copy() # 선택 영역에 사각형 그림을 표시할 이미지 복제
                cv.rectangle(img_draw, (x0, y0), (x, y), red, 2) # 선택 영역에 빨간색 사각형 표시
                cv.imshow('img', img_draw) # 빨간색 사각형이 그려진 이미지 화면 출력
                roi = img[y0:y0 + h, x0:x0 + w] # 원본 이미지에서 선택 영역만 ROI로 지정
                cv.imshow('cropped', roi) # ROI 지정 영역을 새 창으로 표시
                cv.moveWindow('cropped', 0, 0) # ROI 영역만 파일로 저장
                cv.imwrite('cropped.png', roi)
                print('cropped')

            else:
            # 드래그 방향이 잘못된 경우 사각형 그림이 없는 원본 이미지 출력
                cv.imshow('img', img)
                print('좌측 상단에서 우측 하단으로 영역을 드래그하세요.')

img = cv.imread('img_cap.png')
roi = cv.imread('cropped.png')
cv.imshow('img', img)
cv.setMouseCallback('img', onMouse) # 마우스 이벤트 등록
cv.waitKey()
cv.destroyAllWindows()
