import cv2
import os

total_frame = 0
path = 'frames'

isExist = os.path.exists(path)
if not isExist:
  os.makedirs(path)

cap = cv2.VideoCapture('1.mp4')
success, image = cap.read()

while success:
  cv2.imwrite("frames/frame%d.jpg" % total_frame, image)    
  success, image = cap.read()
  print('Read a new frame: ', success)
  total_frame += 1


print("Total frame : ", total_frame)

