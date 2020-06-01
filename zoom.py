import cv2
import time
import imutils
import numpy as np


cap = cv2.VideoCapture('videos/tennis_play_1.mp4')

# Define the codec and create VideoWriter object 
fourcc = cv2.VideoWriter_fourcc(*'XVID') 
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480)) 
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))

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
    ret,frame = video.read() 
    rows,cols,rgb = frame.shape
    stop = frame[w:,h:].shape 

    shift = 0 
    while True:
        ret,frame = video.read() 
        if rows > stop[0] and cols > stop[1]:
            # frame = frame[shift:x,shift:y]
            # resized = cv2.resize(frame,(int(cap.get(3)), int(cap.get(4))))
            shift += speed
            # rows, cols, rgb = frame.shape
        frame = frame[shift:x,shift:y]
        resized = cv2.resize(frame,(int(cap.get(3)), int(cap.get(4))))
        rows, cols, rgb = frame.shape
        out.write(resized)
        cv2.imshow("frame", resized)
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
 
        
zoomin(cap,21,2156,5034,2000,2000)
# release the cap object
out.release()
cap.release() 
# close all windows 
cv2.destroyAllWindows() 