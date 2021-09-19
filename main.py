import cv2
import numpy as np
import time


# Storing the 0th camera's data in the object
video_object = cv2.VideoCapture(0)
time.sleep(3)

# code for creating a replica
replica = 0
for index in range(40):
    ret, replica = video_object.read()
replica = np.flip(replica, axis=1)
# code for opening the webcam
while True:
    # storing the frame rate
    ret, frame = video_object.read()
    frame = np.flip(frame, axis=1)
    # Creating a mask for merging
    # color detection and range defining
    # hsv = > color source
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    blur = cv2.GaussianBlur(hsv, (35, 35), 0)

    lower_range = np.array([0, 120, 70])
    upper_range = np.array([10, 255, 255])
    mask_1 = cv2.inRange(hsv, lower_range, upper_range)

    lower_red_range = np.array([170, 120, 70])
    upper_red_range = np.array([180, 255, 255])
    mask_2 = cv2.inRange(hsv, lower_red_range, upper_red_range)

    mask = mask_1 + mask_2
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    frame[np.where(mask == 255)] = replica[np.where(mask == 255)]

    # For setting it as full screen
    cv2.namedWindow('INVISIBLE @Badshalaskar', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('INVISIBLE @Badshalaskar', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow('INVISIBLE @Badshalaskar', frame)
    # cv2.imshow('REPLICA', replica)
    # cv2.imshow('MASK 1', mask_1)
    key = cv2.waitKey(1)
    # "x" is the terminating key
    if key == ord('x'):
        break
video_object.release()
cv2.destroyAllWindows()
