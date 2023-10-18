# I find that you can use RTPS:

cv2.VideoCapture('rtsp://username:password@169.254.167.2/axis-media/media.amp')

# or using HTTP:
rtsp://root:root@192.168.0.42/axis-media/media.amp

cv2.VideoCapture('http://username_password@169.254.167.2/axis-media/media.amp')


http://root_root@192.168.0.42/axis-media/media.amp
# Before trying this solution in your code, I recommend that you (as Adrien mentioned) make sure the link is working in VLC. You can do this by:

# Open VLC
# Right-click in VLC
# Open Media > Open Network
# Paste link mentioned above.
# Press play.
# (If required) - Enter credentials for your Camera.
# Press play.
# Your video stream should now be displayed in VLC.


http://www.ispyconnect.com/camera/axis#

# This link helped me to generate the correct link to access your camera model: 
# ispyconnect.com/man.aspx?n=Axis#. For example for my camera model Axis P1357 link
# generated using the above website: 
# "rtsp://<username:password>@<ip addres>/axis-media/media.amp". 
# This link worked with 
# cv::VideoCapture source("rtsp://<username:password>@<ip addres>/axis-media/media.amp")


# https://www.chiefdelphi.com/t/how-to-get-image-from-axis-camera-to-a-python-program/147021/6

import cv2
import urllib
import numpy as np

stream=urllib.urlopen('http://10.58.54.108/mjpg/video.mjpg')
bytes=''  
while True:
    bytes+=stream.read(1024)
    a = bytes.find('\xff\xd8')
    b = bytes.find('\xff\xd9')
    if a!=-1 and b!=-1:
        jpg = bytes[a:b+2]
        bytes= bytes**
        i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.CV_LOAD_IMAGE_COLOR)
        i = cv2.cvtColor(i, cv2.COLOR_BGR2HSV)
        cv2.imshow('i',i)
        if cv2.waitKey(1) == 27:
            exit(0)
