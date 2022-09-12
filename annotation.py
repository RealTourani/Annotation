import cv2
import numpy as np
import pybboxes as pbx


#image_path
img_path="2.jpg"

#read image
img_raw = cv2.imread(img_path)

h = img_raw.shape[0]
w = img_raw.shape[1]
channels = img_raw.shape[2]

#select ROI function
roi = cv2.selectROI(img_raw)

#print rectangle points of selected roi
print(roi)

a = pbx.convert_bbox(roi, from_type="coco", to_type="yolo", image_size=(w,h))
print(a)
#Crop selected roi from raw image
roi_cropped = img_raw[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]

#show cropped image
cv2.imshow("ROI", roi_cropped)

cv2.imwrite("crop.jpeg",roi_cropped)

#hold window
cv2.waitKey(0)