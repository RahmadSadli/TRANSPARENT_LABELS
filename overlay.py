"""
Written by: Rahmad Sadli
Website : https://machinelearningspace.com
If you want to redistribute it, just keep the author's name.
"""
import cv2
import numpy as np
def PutText(image, 
            text,
            pos=(0,0),
            text_color=(255,255,255), 
            bg_color=(255,255,255),             
            scale=1,
            thickness=1,
            margin=2,
            transparent=False, 
            font=cv2.FONT_HERSHEY_SIMPLEX, 
            alpha=0.5):
    
    txt_size = cv2.getTextSize(text, font, scale, thickness)
    w_text, h_text= txt_size[0][0], txt_size[0][1]

    x1_text = pos[0] + margin
    y1_text = pos[1] + h_text
    x1_rect = pos[0]
    y1_rect = pos[1] 
    x2_rect = x1_rect + w_text + margin
    y2_rect = y1_rect + h_text + margin
        
    if transparent:    
        mask = image.copy()
        cv2.rectangle(mask, (x1_rect, y1_rect), (x2_rect, y2_rect), bg_color, -1)
        image = cv2.addWeighted(image, 1 - alpha, mask, alpha, 0)        
        cv2.putText(image, text, (x1_text,y1_text), font, scale, text_color, thickness, cv2.LINE_AA)
    else:
        cv2.rectangle(image, (x1_rect, y1_rect), (x2_rect, y2_rect), bg_color, -1)        
        cv2.putText(image, text, (x1_text,y1_text), font, scale, text_color, thickness, cv2.LINE_AA)
    
    return image