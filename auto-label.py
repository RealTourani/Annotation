import os
import cv2
from imutils.object_detection import non_max_suppression # pip install imutils
import numpy as np
import pybboxes as pbx

names = [x for x in input("Enter the name of categories : ").split()]
with open('frames/classes.txt', mode='w') as myfile:
    myfile.write('\n'.join(names))

def semi(img_path):
    details = []
    # Load the image and template
    image = cv2.imread(img_path)
    name , ext = img_path.split('.')  # Split the image name and the extension
    template = cv2.imread('cropped.jpg')
    h = image.shape[0]
    w = image.shape[1]
    channels = image.shape[2]
    # Perform template matching 
    result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)

    # Filter results to only good ones
    threshold = 0.90 # Larger values have less, but better matches.
    (yCoords, xCoords) = np.where(result >= threshold)

    # Perform non-maximum suppression.
    template_h, template_w = template.shape[:2]
    rects = []
    for (x, y) in zip(xCoords, yCoords):
        rects.append((x, y, x + template_w, y + template_h))
    pick = non_max_suppression(np.array(rects))

    # Optional: Visualize the results
    for (startX, startY, endX, endY) in pick:
        cv2.rectangle(image, (startX, startY), (endX, endY),(0, 255, 0), 2)
        
    a = (startX, startY, endX, endY)
    ROItoYolo = pbx.convert_bbox(a, from_type="voc", to_type="yolo", image_size=(w,h))

    for i in ROItoYolo:
        details.append(i) # Append Yolo format coordinates to a list

    upperx = details[0]
    uppery = details[1]
    bottomx = details[2]
    bottmy = details[3]

    f = open('frames/classes.txt', 'r')
    data = f.read()
    lines = data.splitlines()
    class_idx = None
    for idx,line in enumerate(lines):
        if current_class == line:
            class_idx = idx

    # Append coordinates to a txt file
    f = open(name+".txt", "w")
    f.write(str(class_idx) + " " + str(upperx) + " "+ str(uppery) + " "+ str(bottomx)+ " "+ str(bottmy))
    f.close

    print(ROItoYolo)
    cv2.imshow('Results', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

directory = 'frames/'
number_of_files = len([item for item in os.listdir(directory) if os.path.isfile(os.path.join(directory, item))])

for i in range(10):
    current_class = input("Enter your current category name : ")
    semi('frames/frame{}.jpg'.format(i))