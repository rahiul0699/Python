import cv2 as cv
import os

filename = 'video.mp4'
frames_per_second = 24.0
my_res = '480'

STD_DIMENSIONS = {
    "480p": (640, 480),
    "720p": (1280, 720),
    "1080p": (1920, 1080),
    "4k": (3840, 2160),
}

VIDEO_TYPE = {
    'avi': cv.VideoWriter_fourcc(*'XVID'),
    # 'mp4': cv2.VideoWriter_fourcc(*'H264'),
    'mp4': cv.VideoWriter_fourcc(*'XVID'),
}


def get_video_type(filename):
    filename, ext = os.path.splitext(filename)
    if ext in VIDEO_TYPE:
        return VIDEO_TYPE[ext]
    return VIDEO_TYPE['avi']


def res_change(width, height):
    cap.set(3, width)
    cap.set(4, height)


def get_dims(cap, res='1080p'):
    width, height = STD_DIMENSIONS["480p"]
    if res in STD_DIMENSIONS:
        width, height = STD_DIMENSIONS[res]
    # change the current caputre device
    # to the resulting resolution
    res_change(width, height)
    return width, height


cap = cv.VideoCapture(0)
dim = get_dims(cap, my_res)
video_type_cv = get_video_type(filename)
out = cv.VideoWriter(filename, video_type_cv, frames_per_second, dim)


def scale_win(frame, percent):
    width = int(frame.shape[1]*percent/100)
    height = int(frame.shape[0]*percent/100)
    dim = (width, height)
    return cv.resize(frame, dim, cv.INTER_AREA)


# res_change(1920, 1080)
while True:
    check, frame = cap.read()
   # frame = scale_win(frame, 80)
    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    out.write(frame)
    cv.imshow("Recording", frame)
    key = cv.waitKey(5)
    if key == ord('q'):
        break
cap.release()
cv.destroyAllWindows()
