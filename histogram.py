import cv2 as cv
import numpy as np

src = cv.imread("cropped.png")
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
result = np.zeros((src.shape[0], 256), dtype=np.uint8)

hist = cv.calcHist([gray], [0], None, [256], [0, 40])
cv.normalize(hist, hist, 0, result.shape[0], cv.NORM_MINMAX)

for x, y in enumerate(hist):
    cv.line(result, (int(x), result.shape[0]), (int(x), result.shape[0] - int(y)), 255)

cropped_hair = np.hstack([gray, result])

cv.imshow("ch", cropped_hair)
cv.waitKey(0)
cv.destroyAllWindows()
