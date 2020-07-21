import cv2

#window text data
font = cv2.FONT_HERSHEY_COMPLEX
fontScale=1
color=(0,255,0),
thickness=2


video=cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
a=1
while True:
   a=a+1

   check,frame=video.read()


   faces = face_cascade.detectMultiScale(frame, scaleFactor=1.05, minNeighbors=5)

   for x, y, w, h in faces:
      frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (230, 0, 200), 3)

   # putting text in the window
      frame = cv2.putText(frame, 'Face',(x,y) , font, fontScale, (230, 0, 200), thickness)

   #print(check)

   cv2.imshow("Capture",frame)


   if cv2.waitKey(1) == ord('q'):
      break

video.release()
cv2.destroyAllWindows()