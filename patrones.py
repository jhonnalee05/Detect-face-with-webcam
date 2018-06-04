import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascades\haarcascade_frontalface_alt.xml')
eye_cascade = cv2.CascadeClassifier('haarcascades\haarcascade_eye.xml')
cap=cv2.VideoCapture(0)

while(True):
	ret,img=cap.read()
	gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	faces=face_cascade.detectMultiScale(gray,1.3,5)

	for(x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(125,255,0),2)
		rol_gray=gray[y:y+h,x:x+w]
		rol_color=img[y:y+h,x:x+w]

		eyes=eye_cascade.detectMultiScale(rol_gray)

		for(ex,ey,ew,eh) in eyes:
			cv2.rectangle(rol_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
	cv2.imshow('img',img)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2-destroyAllWindows()