import cv2
import numpy as np

img = cv2.imread('anime.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

kernel = np.ones((5, 5), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

cv2.imshow('image', opening)
cv2.waitKey(0)
cv2.destroyAllWindows()

masukan_angka = int (input('masukan angka anda yang ingin di hitung :'))
angka = int(masukan_angka)

for i in range(angka):
    opening = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

cv2.imshow('image', opening)
cv2.waitKey(0)
cv2.destroyAllWindows()