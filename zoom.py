import cv2
import time
import imutils
import numpy as np


cap = cv2.VideoCapture('videos/tennis_play_1.mp4')
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('result.mp4',fourcc,25,(1920,1080))

def make_1080():
    cap.set(3,1920)
    cap.set(4,1080)

def make_720p():
    cap.set(3,1280)
    cap.set(4,720)

def make_480p():
    cap.set(3,640)
    cap.set(4,480)

def rescale_frame(frame,percent=75):
    scale_percent = 75 
    width = int(frame.shape[1] *scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)
    dim = (width, height)
    print(dim)
    return cv2.resize(frame,dim,interpolation=cv2.INTER_AREA)

def shift_frame(frame):
    num_rows, num_cols = frame.shape[:2]
    translation_matrix = np.float32([[1,0,70],[0,1,110]])
    print(translation_matrix)
    img_translation = cv2.warpAffine(frame,translation_matrix,(num_cols,num_rows))
    return img_translation

# make_480p()
# make_720p()
# make_1080()

resolution = [make_480p,make_720p,make_1080]

def zoomin(video,speed,x,y,w,h):
    ret,frame = cap.read() 
    rows,cols,rgb = frame.shape
    stop = frame[w:,h:].shape
    original = frame.shape   
    while True:
        if frame.shape[0] > stop[0] and frame.shape[1] > stop[1]:
            frame = frame[speed:x,speed:y]
            resized = cv2.resize(frame, (original[0]//2, original[1]//6))
        else:
            frame = frame
            resized = cv2.resize(frame,(original[0]//2,original[1]//6))
        out.write(frame)
        cv2.imshow("frame", resized)
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
        rows,cols,rgb = frame.shape
        
        

zoomin(cap,10,2156,5034,2000,2000)
# release the cap object
out.release()
cap.release() 
# close all windows 
cv2.destroyAllWindows() 