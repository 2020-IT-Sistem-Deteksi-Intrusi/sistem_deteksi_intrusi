import cv2
import numpy as np
import os
import datetime
import logging
import time
import imutils
from imutils.video import FPS
import pyautogui

def known():
    # Buat send known
    pyautogui.write("Andrew Detected")
    time.sleep(2)
    pyautogui.press("enter")

def unknown():
    # Buat send unknown
    pyautogui.write("Intruder Detected")
    time.sleep(2)
    pyautogui.press("enter")

def setup_whatsapp():
    # setup page whatsapp
    # os.system("chromium web.whatsapp.com")
    pyautogui.moveTo(786,763)
    pyautogui.click()
    time.sleep(30)
    pyautogui.moveTo(286,209)
    time.sleep(2)
    pyautogui.click()

def prototype_photo():
    # Select Attach
    time.sleep(2)
    pyautogui.moveTo(562,681)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    # Select Image
    time.sleep(2)
    pyautogui.moveTo(561,615)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    # Select Documents
    time.sleep(2)
    pyautogui.moveTo(343,270)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    # Select Machine Learning
    time.sleep(2)
    pyautogui.moveTo(494,129)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    # Select home
    time.sleep(2)
    pyautogui.moveTo(681,112)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    # Select Facial Recog
    time.sleep(2)
    pyautogui.moveTo(861,167)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    # Select Log
    time.sleep(2)
    pyautogui.moveTo(835,257)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    # Select Known
    time.sleep(2)
    pyautogui.moveTo(839,133)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    # Select Image
    time.sleep(2)
    pyautogui.moveTo(862,111)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.press("enter")
    # unknown
    # pyautogui.moveTo(326,149)
    # time.sleep(1)
    # pyautogui.click()
    # pyautogui.click()
    # Send
    # pyautogui.moveTo(335,127)
    # time.sleep(1)
    # pyautogui.click()
    # pyautogui.click()
    # Write
    time.sleep(2)
    pyautogui.write("Andrew Detected")
    time.sleep(3)
    pyautogui.press("enter")

def prototype_photo_unknown():
    # Select Attach
    time.sleep(2)
    pyautogui.moveTo(562,681)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    # Select Image
    time.sleep(2)
    pyautogui.moveTo(561,615)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    # Select Documents
    time.sleep(2)
    pyautogui.moveTo(343,270)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    # Select Machine Learning
    time.sleep(2)
    pyautogui.moveTo(494,129)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    # Select home
    time.sleep(2)
    pyautogui.moveTo(681,112)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    # Select Facial Recog
    time.sleep(2)
    pyautogui.moveTo(861,167)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    # Select Log
    time.sleep(2)
    pyautogui.moveTo(835,257)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    # Select unknown
    time.sleep(2)
    pyautogui.moveTo(847,148)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    # Select Image
    time.sleep(2)
    pyautogui.moveTo(862,111)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.press("enter")
    # unknown
    # pyautogui.moveTo(326,149)
    # time.sleep(1)
    # pyautogui.click()
    # pyautogui.click()
    # Send
    # pyautogui.moveTo(335,127)
    # time.sleep(1)
    # pyautogui.click()
    # pyautogui.click()
    # Write
    time.sleep(2)
    pyautogui.write("Intruder Detected")
    time.sleep(3)
    pyautogui.press("enter")



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


recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
font = cv2.FONT_HERSHEY_SIMPLEX
#iniciate id counter
id = 0
# names related to ids: example ==> Marcelo: id=1,  etc
names = ['Andrew', 'Blank', 'Blank', 'Blank', 'Blank', 'Blank']
# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video widht
cam.set(4, 480) # set video height
# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)
setup_whatsapp()
while True:
    ret, img =cam.read()
    img = cv2.flip(img, 1) # Flip vertically
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )
    for(x,y,w,h) in faces:
        ret, frame = cam.read()
        frame = imutils.resize(frame, width=450)
        frame = cv2.flip(frame,1)
        timer=datetime.datetime.now().strftime("%d %m %Y %H:%M %S")
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

        # If confidence is less them 100 ==> "0" : perfect match
        if (confidence < 100):
            time.sleep(3)
            id = names[id]
            count = 0
            confidence = "  {0}%".format(round(100 - confidence))
            # print("Andrew" + " " + "Detected" +'\t' + timer)
            # write("Andrew" + " " + "Detected" +'\t\t' + timer ,logfile)
            # known()
            # cv2.imwrite("log/Andrew - {}.png".format(datetime.datetime.now().strftime("%d %B %y %I:%M %p"), frame))
            # c="log/Andrew_{}.png".format(datetime.datetime.now().strftime("%d %B %y %I:%M %p"))
            for a in names:
                format_time_string = datetime.datetime.now().strftime("%d-%m-%Y %H.%M.%S")
                extension = ".jpg"
                newfile = format_time_string;
                count += 1
                c="log/known/Andrew " + str(count) + " " + newfile + " Detected.jpg"
                cv2.imwrite(c,frame)
                print("Andrew" + " " + "Detected" +'\t' + timer)
                write("Andrew" + " " + "Detected" +'\t\t' + timer ,logfile)
                #known()
                prototype_photo()
                time.sleep(60)
                
        else:
            time.sleep(3)
            count = 0
            id = "Unknown"
            confidence = "  {0}%".format(round(100 - confidence))
            # for a in confidence:
            #     count += 1
            #     cv2.imwrite("log/Intruder - " + str(count) + ".jpg", gray[y:1080,x:1080])
            # print("Unknown" + " " + "Detected" +'\t' + timer)
            # write("Unknown" + " " + "Detected" +'\t\t' + timer ,logfile)
            # unknown()
            # cv2.imwrite("log/Intruder - {}.jpg".format(datetime.datetime.now().strftime("%d %B %y %I:%M %p"), frame))
            # c="log/Intruder_{}.png".format(datetime.datetime.now().strftime("%d %B %y %I:%M %p"))
            for a in names:
                format_time_string = datetime.datetime.now().strftime("%d-%m-%Y %H.%M.%S")
                extension = ".jpg"
                newfile = format_time_string;
                count += 1
                c="log/unknown/Intruder "+ str(count) + " " + newfile +  " Detected.jpg"
                cv2.imwrite(c,frame)
                print("Unknown" + " " + "Detected" +'\t' + timer)
                write("Unknown" + " " + "Detected" +'\t\t' + timer ,logfile)
                unknown()
                # prototype_photo_unknown()
                time.sleep(60)


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
