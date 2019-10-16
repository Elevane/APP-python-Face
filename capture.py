import cv2


def capture():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # video capture source camera (Here web-cam of laptop)
    ret, frame = cap.read()  # return a single frame in variable `frame`
    if not cap.isOpened():  # si la camera ne s'ouvre pas
        raise IOError("Cannot open webcam")


    cap.release()
    cv2.destroyAllWindows()
