import cv2
import numpy as np



filename = '1.png'
img = cv2.imread(filename)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, maxCorners=100, qualityLevel=0.01, minDistance=10)

# 返回的结果是 [[ 311., 250.]] 两层括号的数组。
corners = np.int0(corners)
tmx1=0
tmy1=0
tmx2=10000
tmy2=10000
for i in corners:
    x, y = i.ravel()
    cv2.circle(img, (x, y), 3, 255, -1)
    if tmx1<x:
        tmx1=x
    if tmy1<y:
        tmy1=y
    if tmx2>x:
        tmx2=x
    if tmy2>y:
        tmy2=y

cv2.rectangle(img, (tmx1,tmy1), (tmx2,tmy2), (0, 255, 0), 3)
cv2.imshow('dst', img)

print(tmx1,tmy1,tmx2,tmy2)
