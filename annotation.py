import os
import cv2
import pybboxes as pbx



def labeling(img_path):
    details = []
    img_raw = cv2.imread(img_path)  # Read image
    name , ext = img_path.split('.')  # Split the image name and the extension
    
    # Getting width, height and channels of image
    h = img_raw.shape[0]
    w = img_raw.shape[1]
    channels = img_raw.shape[2]

    #select ROI function
    roi = cv2.selectROI(img_raw)

    #print rectangle points of selected roi

    # Convert ROI coordinates to YOLO v3 format
    ROItoYolo = pbx.convert_bbox(roi, from_type="coco", to_type="yolo", image_size=(w,h))

    #Crop selected roi from raw image
    roi_cropped = img_raw[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]

    for i in ROItoYolo:
        details.append(i) # Append Yolo format coordinates to a list


    upperx = details[0]
    uppery = details[1]
    bottomx = details[2]
    bottmy = details[3]

    
    # Append coordinates to a txt file
    f = open(name+".txt", "w")
    f.write(str(upperx) + " "+ str(uppery) + " "+ str(bottomx)+ " "+ str(bottmy))
    f.close

    #show cropped image
    cv2.imshow("ROI", roi_cropped)

    cv2.imwrite("crop.jpeg",roi_cropped)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


directory = 'frames/'
number_of_files = len([item for item in os.listdir(directory) if os.path.isfile(os.path.join(directory, item))])

for i in range(number_of_files):

    labeling('frames/frame{}.jpg'.format(i))
        
