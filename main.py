"""
Written by: Rahmad Sadli
Website : https://machinelearningspace.com
If you want to redistribute it, just keep the author's name.
"""
import cv2
import numpy as np
from overlay import PutText
import os
import matplotlib.colors as mcolors


def main():
    current_dir = os.getcwd()
    im_path = os.path.join(current_dir,"images","000000049286.jpg")
    ann_path = os.path.join(current_dir,"annotations","000000049286.txt") 
    
    
    image = cv2.imread(im_path)
    annotations = np.loadtxt(ann_path, dtype='str')

    """class_names=["zebra","giraffe"]
    color_list=[(0,0,255),(255,0,0)]"""

    class_names=["cup", "fork", "spoon", "chair", "dining table", "cake"]
    color_list=[(0,0,125),(0,255,0),(255,0,0),(255,125,0),(0,0,255),(0,255,255)]

    for ann in annotations:

        bbox = ann.split(',')
        bbox =  list(map(lambda x: int(float(x)), bbox))
        x, y, w, h, class_id = [int(b) for b in bbox]    
        class_name = class_names[class_id]
        x1y1=(x,y)
        x2y2=(x+w,y+h)
        image = cv2.rectangle(image, (x1y1), (x2y2), color_list[class_id], 2)

        image = PutText(image,
                text=class_name,
                pos=x1y1,     
                text_color=(255,255,255),
                bg_color=color_list[class_id],
                scale=0.7,
                thickness=1,
                margin=2,                   
                transparent=True,
                alpha=0.4)

    cv2.imshow("Transparent Labels",image)
    cv2.waitKey(0)

if __name__ == "__main__":    
    main()
