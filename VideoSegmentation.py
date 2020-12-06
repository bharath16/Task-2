# Method 2
import numpy as np
import cv2

def main():
    file_path = input("Enter the file path")
    cap = cv2.VideoCapture(file_path)

    #initialize the cv2- background subtractor for KNN and MOG2
    BS_knn = cv2.createBackgroundSubtractorKNN()
    BS_MOG2 = cv2.createBackgroundSubtractorMOG2()

    while(cap.isOpened()):
        ret, frame = cap.read() # frame reader
        if ret == True:
            #extract Knn method for foreground mask
            
            knn_foregmask = BS_knn.apply(frame)
            cv2.imshow('KNN Method', knn_foregmask)

            #extract MOG2 method for foreground mask
            mog2_foregmask = BS_MOG2.apply(frame)
            cv2.imshow('MOG2 Method', mog2_foregmask)   

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
    #release video capture
    cv2.destroyAllWindows()
    cap.release()