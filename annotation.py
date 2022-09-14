import os
import cv2

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
    
    #Crop selected roi from raw image
    roi_cropped = img_raw[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]

    #show cropped image
    cv2.imwrite('cropped.jpg',roi_cropped)
    cv2.imshow(name, roi_cropped)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


directory = 'frames/'
number_of_files = len([item for item in os.listdir(directory) if os.path.isfile(os.path.join(directory, item))])

for i in range(1):
    
    labeling('frames/frame{}.jpg'.format(i))
