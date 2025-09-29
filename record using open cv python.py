import cv2
import numpy as np
import time
cap = cv2.VideoCapture(0)

format = cv2.VideoWriter_fourcc(*'mp4v')
output = cv2.VideoWriter('record file1.mp4',format,200.0,(640,480))

start_time = time.time()
record_seconds = 10

while True:
    suc,frame = cap.read()
    if not suc:
        frame = np.zeros((480,640,3),dtype=np.uint8)
        cv2.putText(frame,'NO SIGNAL !!!',(180,240),cv2.FONT_HERSHEY_COMPLEX,1.5,(0,0,255),2)

        output.write(frame)
        cv2.imshow('record web cam',frame)
        if time.time() - start_time > record_seconds:
            break
output.release()
cap.release()
cv2.destroyAllWindows()