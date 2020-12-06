import numpy as np
import cv2

def main():
    file_path = input("Enter the file path")
    cap = cv2.VideoCapture("C:\\Users\\Bharathwaj\\Documents\\Tiliter\\data\\video_1.mp4")

    #reading then frame 1
    ret,frame1 = cap.read()
    cv2.imshow('Frame1',frame1)

    #reading the frame 2
    while(cap.isOpened()):
        
        ret,frame2 = cap.read()
        
        cv2.imshow('Frame2',frame2)
        #extract the foreground mask
        foregmask = cv2.absdiff(frame1, frame2)

        #apply the threshold
        _, thresh = cv2.threshold(foregmask,10,255,cv2.THRESH_BINARY)
        cv2.imshow('Foreground Mask', thresh)
        
        frame1 = frame2

        #colr = cv2.cvtColor(thresh,cv2.COLOR_RGB2GRAY)
        #cv2.imshow('color', colr)
        #wait until any key pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    #release video capture
    cv2.destroyAllWindows()
    cap.release()
