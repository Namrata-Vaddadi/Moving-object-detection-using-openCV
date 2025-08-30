import cv2
import imutils
import time

vs = cv2.VideoCapture(0)
time.sleep(1)
fgbg = cv2.createBackgroundSubtractorMOG2()
area = 500

while True:
    ret, img = vs.read()
    if not ret:
        break
    img = imutils.resize(img, width=500)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (21, 21), 0)

    fgmask = fgbg.apply(blur)

    thresh = cv2.threshold(fgmask, 244, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)

    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    text = "Normal"
    for c in cnts:
        if cv2.contourArea(c) < area:
            continue

        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        text = "Moving object detected"
        print(text)

    cv2.putText(img, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    cv2.imshow("Video Stream", img)
    cv2.imshow("Foreground Mask", fgmask)
    cv2.imshow("Threshold", thresh)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

vs.release()
cv2.destroyAllWindows()

