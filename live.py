import cv2
import sys
from datetime import datetime
import LogInCsv

cascPath = sys.argv[1]
faceCascade = cv2.CascadeClassifier(cascPath)
cap = cv2.VideoCapture(0)
frame = cap.read()
video_capture = cv2.VideoCapture(0)
run = True
while run:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
        # flags=cv2.CV_HAAR_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('y'):  # save on pressing 'y'
        time = datetime.today().strftime("%d_%m_%Y%H%M%S")
        fileName = "images/" + str(time) + ".jpg"
        print(fileName)
        LogInCsv.add(fileName)
        cv2.imwrite(fileName, frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        run = False
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
cv2.destroyWindow(frame)
