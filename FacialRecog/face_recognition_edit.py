import cv2
import numpy as np
import os
import datetime
import logging
import time
import imutils
from imutils.video import FPS

# Import notif bot

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
font = cv2.FONT_HERSHEY_SIMPLEX


def LOG_insert(file, format, text, level):
            infoLog = logging.FileHandler(file)
            infoLog.setFormatter(format)
            logger = logging.getLogger(file)
            logger.setLevel(level)

            if not logger.handlers:
                logger.addHandler(infoLog)
                if (level == logging.INFO):
                    logger.info(text)
                if (level == logging.ERROR):
                    logger.error(text)
                if (level == logging.WARNING):
                    logger.warning(text)
def write(text,file):
    f = open(file,"a")
    f.write("{}\n".format(text))
    return
logfile=r"log/Access.log"

video_capture = cv2.VideoCapture(0)
# cap.set(CV_CAP_PROP_FPS, 50);
fps = FPS().start()
            # infoLog.close()
            # logger.removeHandler(infoLog)

            # return
            # formatLOG = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
            # LOG_insert("log/Access.log", formatLOG , str(names[id]) + "Detected", logging.INFO)

if __name__ == "__main__":
#iniciate id counter
    id = 0
    # names related to ids: example ==> Marcelo: id=1,  etc
    names = ['Andrew','NULL','NULL','NULL']
    # Initialize and start realtime video capture
    cam = cv2.VideoCapture(0)
    cam.set(3, 640) # set video widht
    cam.set(4, 480) # set video height 
    # Define min window size to be recognized as a face
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)

    while True:
        ret, img =cam.read()
        img = cv2.flip(img, 1) # Flip vertically
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor = 1.2,
            minNeighbors = 7,
            minSize = (int(minW), int(minH)),
        )
        for (x,y,w,h) in faces:

            ret, frame = cam.read()
            frame = imutils.resize(frame, width=450)
            frame = cv2.flip(frame,-1)
            timer=datetime.datetime.now().strftime("%d %m %Y %H:%M %S")
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
            id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

            # If confidence is less them 100 ==> "0" : perfect match
            if (confidence < 100):
                id = names[id]
                count = 0
                confidence = "  {0}%".format(round(100 - confidence))
                print("Andrew" + " " + "Detected" +'\t' + timer)
                write("Andrew" + " " + "Detected" +'\t\t' + timer ,logfile)
                # cv2.imwrite("log/Andrew - {}.png".format(datetime.datetime.now().strftime("%d %B %y %I:%M %p"), frame))
                # c="log/Andrew_{}.png".format(datetime.datetime.now().strftime("%d %B %y %I:%M %p"))
                for a in names:
                    format_time_string = datetime.datetime.now().strftime("%d-%m-%Y %H.%M.%S")
                    extension = ".jpg"
                    newfile = format_time_string;
                    count += 1
                    c="log/known/Andrew " + str(count) + " " + newfile + " Detected.jpg"
                    cv2.imwrite(c,frame)
                    time.sleep(5)
                # known()
            else:
                count = 0
                id = "Unknown"
                confidence = "  {0}%".format(round(100 - confidence))
                # for a in confidence:
                #     count += 1
                #     cv2.imwrite("log/Intruder - " + str(count) + ".jpg", gray[y:1080,x:1080])
                print("Unknown" + " " + "Detected" +'\t' + timer)
                write("Unknown" + " " + "Detected" +'\t\t' + timer ,logfile)
                # cv2.imwrite("log/Intruder - {}.jpg".format(datetime.datetime.now().strftime("%d %B %y %I:%M %p"), frame))
                # c="log/Intruder_{}.png".format(datetime.datetime.now().strftime("%d %B %y %I:%M %p"))
                for a in names:
                    format_time_string = datetime.datetime.now().strftime("%d-%m-%Y %H.%M.%S")
                    extension = ".jpg"
                    newfile = format_time_string;
                    count += 1
                    c="log/unknown/Intruder "+ str(count) + " " + newfile +  " Detected.jpg"
                    cv2.imwrite(c,frame)
                    time.sleep(5)

            cv2.putText(
                        img,
                        str(id),
                        (x+5,y-5),
                        font,
                        1,
                        (255,255,255),
                        2
                    )
            cv2.putText(
                        img,
                        str(confidence),
                        (x+5,y+h-5),
                        font,
                        1,
                        (255,255,0),
                        1
                    )

        cv2.imshow('Intrusion Detection System',img)
        k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            break
    # Do a bit of cleanup
    print("\n [INFO] Exiting Program and cleanup stuff")
    cam.release()
    cv2.destroyAllWindows()
