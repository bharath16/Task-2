import numpy as np
import cv2


def main():
    file_path = input()
    fps = int(input())
    monochrome = bool(input())
    cap = cv2.VideoCapture(file_path)
    frame = fps
    if monochrome == True:
        while(cap.isOpened()):
            ret, frame=cap.read()
            gray=cv2.cv2tColor(frame,cv2.COLOR_RGB2GRAY)
            if ret == True:
                cv2.imshow('Frame',gray)            
                if cv2.waitKey(25) or 0xFF == ord('q'):
                    break
                if cv2.waitKey(1) or 0xFF == ord('p'):
                    cv2.waitKey(-1)
                    if cv2.waitkey(1) or 0xFF == ord('b'):
                        cv2.set(cv2.cv2_CAP_PROP_POS_FRAMES(2, previous_frame))
            else:
                break
        cap.release()
        cv2.destroyAllWindows()
    else:
        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret == True:
                cv2.imshow('Frame', frame)
                if cv2.waitKey(25) or 0xFF == ord('q'):
                    break
                if cv2.waitKey(1) or 0xFF == ord('p'):
                    cv2.waitKey(-1)
                    if cv2.waitkey(1) or 0xFF == ord('b'):
                        cv2.set(cv2.cv2_CAP_PROP_POS_FRAMES(2))
            else:
                break
        cap.release()
        cv2.destroyAllWindows()