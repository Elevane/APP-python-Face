import cv2
import sys
from datetime import datetime
import LogInCsv

cascadePath = sys.argv[1]
faceCascade = cv2.CascadeClassifier(cascadePath)
cap = cv2.VideoCapture(0)
frame = cap.read()
video_capture = cv2.VideoCapture(0)


""""
the while loop turn until key "q" is pressed to exit or "y" is pressed to save the screenshots.
It search for faces as well with the library OpenCV and draw a rectangle around the faces it finds.
"""
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    #   define the input frame/images, in our case, a web cam
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #   define th parameters of detector
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # save on pressing 'y'
    if cv2.waitKey(1) & 0xFF == ord('y'):
        #   get the actual date
        time = datetime.today().strftime("%d%m%Y%H%M%S")
        #   the file path
        filepath = "images/" + str(time) + ".jpg"
        #    log the file name
        print(filepath)
        # call the add method to log it
        LogInCsv.add(filepath)
        #   save the file into the given directory
        cv2.imwrite(filepath, frame)

    #   break the loop on "q" key pressed. Close window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# if the while loop break, release the capture
video_capture.release()
cv2.destroyAllWindows()
