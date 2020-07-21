import cv2
first_frame = None

video=cv2.VideoCapture(0)

while True:
    check,frame=video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21,21),0)

    if first_frame is None:
        first_frame=gray
        continue
    delta_frame = cv2.absdiff(first_frame,gray)
    thresh_delta = cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1]
    thresh_delta = cv2.dilate(thresh_delta,None,iterations=0)
    contours, hierarchy = cv2.findContours(thresh_delta.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
       if cv2.contourArea(contour)<1000:
         continue

       (x,y,w,h) = cv2.boundingRect(contour)
       frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 200), 3)


    cv2.imshow("Capture",frame)
    cv2.imshow("Gray", gray)
    cv2.imshow("Del", delta_frame)
    cv2.imshow("thresh", thresh_delta)


    if cv2.waitKey(1) == ord('q'):
        break

video.release()
cv2.destroyAllWindows()