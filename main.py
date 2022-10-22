import argparse
import cPickle as pickle
import cv2
import numpy as np
import time
import serial


ser = serial.Serial('COM3', 9600)
time.sleep(5)
flag_sensor = 0
int(flag_sensor)


def dibujarAma (maskv, color):
  _,contornos,_ = cv2.findContours(maskv, cv2.RETR_EXTERNAL,
      cv2.CHAIN_APPROX_SIMPLE)
  for c in contornos:
    area = cv2.contourArea(c)

    flag_sensor = ser.read()

    if area > 3000:
      M = cv2.moments(c)
      if (M["m00"]==0): M["m00"]=1
      x = int(M["m10"]/M["m00"])
      y = int(M['m01']/M['m00'])
      nuevoContorno = cv2.convexHull(c)
      cv2.circle(frame,(x,y),7,(0,255,0),-1)
      cv2.putText(frame,'Vaso Volteado'.format(x,y),(x+10,y), font, 0.75,(0,255,0),1,cv2.LINE_AA)
      cv2.drawContours(frame, [nuevoContorno], 0, color, 3)
      print (1)
      if flag_sensor == '2':
        ser.write(b'3')

    #else:
      #if flag_sensor == '2':
        #ser.write(b'3')




cap = cv2.VideoCapture(1)



amarillob = np.array([20,100,20],np.uint8)
amarilloa = np.array([38,255,255],np.uint8)



font = cv2.FONT_HERSHEY_SIMPLEX

while True:
  ret,frame = cap.read()
  if ret == True:
    frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)


    maskYellow1 = cv2.inRange(frameHSV, amarillob, amarilloa)
    dibujarAma (maskYellow1, (0, 0, 255))

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('s'):
      break
cap.release()
cv2.destroyAllWindows()
