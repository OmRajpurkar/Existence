import os
import cv2
import time

cap = cv2.VideoCapture(0)

run = True
getname= True

no = 0
path = '/home/divya/FaceRecognition/dataset/'  

while(getname):
    name = input('Enter your name :')
    if not os.path.exists(path+name):
        os.mkdir(path+name)
        getname = False
    else:
        print('Name Taken')

while(run):
    ret,frame = cap.read()
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, str(no), (600, 20), font, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.imshow('Capture',frame)
    inputkey = cv2.waitKey(1)
    location = path +"/" + name + "/" + str(no) + ".jpg"
    if inputkey == 27:
        run = False
    if inputkey == ord('q'):
        print(location)
        cv2.imwrite(location, frame)
        no = no + 1
    
 
cap.release()
cv2.destroyAllWindows()
