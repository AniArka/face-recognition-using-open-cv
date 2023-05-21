import os

import cv2
import numpy as np
import face_recognition
#from os import *

path = 'imageattendence'
images = []
classname = []
mylist = os.listdir(path)
print(mylist)

for cl in mylist:
    curimg = cv2.imread(f'{path}/{cl}')
    images.append(curimg)
    classname.append(os.path.splitext(cl)[0])
print(classname)


def findEncoding(images):
    encodelist = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodelist.append(encode)
    return encodelist


encodeListKnown = findEncoding(images)
print("encoding complete")

cap = cv2.VideoCapture(0)

#getting feed from phone
#adress = "url"
#cap.open(adress)

while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS, model="hog")
    encodeCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeface, facceLoc in zip(encodeCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeface,tolerance=0.5)
        facDis = face_recognition.face_distance(encodeListKnown, encodeface)
        print(facDis)
        matchindex = np.argmin(facDis)

        if matches[matchindex]:
            global name5 
            name5 = classname[matchindex].upper()
            print(name5)
            y1, x2, y2, x1 = facceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name5, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)



    cv2.imshow('webcam', img)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

