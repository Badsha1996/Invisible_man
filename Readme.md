# *Invisible suit* 
This is a simple project based on `python` library `opencv`. Open the project, run it with python IDE. the give it some time to capture the backgroud. Use a red cloth to make yourself invisible.
## [Demo link] (https://www.linkedin.com/posts/badsha-laskar_opencv-python-project-ugcPost-6845981055690903552-8-US)
## Algorithm
The concept for this project is simple. 
* **step:**
1. Capture the video image
2. Create a mask
3. New video start
4. Replace it with the first video capture
5. marks = marks1+marks2

## Requirements
For running the project you need numpy, opencv and python3 installed in your 
system. First go to the python [website](https://www.python.org/). After downloading Pyhton3 open command line in your machine. Type `pip install numpy` and `pip install opencv-python`.
## Creating masks
```python
    import cv2
    import numpy as np
    ...................
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
```
