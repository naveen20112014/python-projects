from PIL import ImageGrab
import numpy as np
import cv2
time_start = datetime.datetime.now().strftime('%y-%m-%d %H-%M-%S')
print(time_stamp)
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
captured_video = cv2.VideoWriter('output.mp4',fourcc, 20.0, (1280, 720 ))
while True:
    img =ImageGrab.grab(bbox=(0, 0, 1280, 720 ))
    img_np = np.array(img)
    img_final =cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    cv2.imshow('Secret Capture', img_final)
    captured_video.write(img_final)
    if cv2.waitKey(10) == ord('q'):
        break