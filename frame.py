import cv2
import os

count = 0
path = 'frames'

isExist = os.path.exists(path)
if not isExist:
  os.makedirs(path)

cap = cv2.VideoCapture('1.mp4')
success, image = cap.read()

while success:
  cv2.imwrite("frames/frame%d.jpg" % count, image)    
  success, image = cap.read()
  print('Read a new frame: ', success)
  count += 1

  Total_frame = count

print("Total frame : ", Total_frame)

