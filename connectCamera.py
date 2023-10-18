
"""Access IP Camera in Python OpenCV""" 
import cv2 

# Diferentes maneras que funcionan:
# stream = cv2.VideoCapture('rtsp://admin:Abc12345@192.168.1.101:554/axis-media/media.amp')
# stream = cv2.VideoCapture('rtsp://admin:Abc12345@192.168.1.101/Streaming/Channels/101')#Mainstream
# stream = cv2.VideoCapture('rtsp://admin:Abc12345@192.168.1.101/Streaming/Channels/102')#Substream
# stream = cv2.VideoCapture('rtsp://admin:Abc12345@192.168.1.101/HighResolutionVideo')
# stream = cv2.VideoCapture('rtsp://admin:Abc12345@192.168.1.101/live')
# stream = cv2.VideoCapture('rtsp://admin:Abc12345@192.168.1.101/h264_stream')



# def create_camera (rtsp_username,rtsp_password,channel,width,height,brightness):
#     rtsp = "rtsp://" + rtsp_username + ":" + rtsp_password + "@192.168.1.101:8554/Streaming/channels/" + str(channel) + "02" #change the IP to suit yours
#     cap = cv2.VideoCapture()
#     cap.open(rtsp)
#     cap.set(3, width)  # ID number for width is 3
#     cap.set(4, height)  # ID number for height is 4
#     cap.set(10, brightness)  # ID number for brightness is 10
#     return cap

# rtsp_username = "admin"
# rtsp_password = "Abc12345"
# width = 640
# height = 480
# brightness = 100
# cam_no = 1

cam = cv2.VideoCapture('rtsp://root:intecol.123@169.254.230.27:8554/live')


# cam = create_camera(rtsp_username,rtsp_password,cam_no,width,height,brightness)
fps = cam.get(cv2.CAP_PROP_FPS)
cam.set(3, 512)  # ID number for width is 3
cam.set(4, 384)  # ID number for height is 4
print(fps)
while True:
    success, current_cam = cam.read()
    # dim = (width, height)
    # Full_frame = cv2.resize(current_cam, dim, interpolation=cv2.INTER_AREA)
    cv2.imshow('IP Camera resized',current_cam) 
    print(current_cam.shape)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break