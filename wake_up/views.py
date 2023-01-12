from urllib import request
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"

#------------------video---------

import cv2
from django.http import StreamingHttpResponse
from django.shortcuts import render
from django.views import View
import time
import cv2
import dlib
from imutils import face_utils
from scipy.spatial import distance
from playsound import playsound

# ストリーミング画像・映像を表示するview
class VideoView(View):
    def get(self, request):
        return render(request, 'video.html', {})

# ストリーミング画像を定期的に返却するview
def video_feed_view():
    return lambda _: StreamingHttpResponse(generate_frame(), content_type='multipart/x-mixed-replace; boundary=frame')

# フレーム生成・返却する処理
Xml_path = "C:/tutorial/Mypython/termproject/haarcascade_frontalface_alt2.xml"
Dat_path = "C:/tutorial/Mypython/termproject/shape_predictor_68_face_landmarks.dat"

<<<<<<< HEAD
""" Xml_path = "/Volumes/USB DISK/iwai_lab/term_project/wake_up/material/haarcascade_frontalface_alt2.xml"
Dat_path = "/Volumes/USB DISK/iwai_lab/term_project/wake_up/material/shape_predictor_68_face_landmarks.dat" """
Sound_path = "C:/tutorial/Mypython/term_project_3/term_project/wake_up/material/soundb.wav"
=======
Xml_path = "/Volumes/USB DISK/iwai_lab/term_project/wake_up/material/haarcascade_frontalface_alt2.xml"
Dat_path = "/Volumes/USB DISK/iwai_lab/term_project/wake_up/material/shape_predictor_68_face_landmarks.dat"
Sound_path = "/Volumes/USB DISK/iwai_lab/term_project/wake_up/material/soundb.wav"
>>>>>>> 0f91716d2a917c872bc257f77603a47bdac0faeb


def generate_frame():
    face_1 = cv2.CascadeClassifier(Xml_path)
    face_parts_1 = dlib.shape_predictor(Dat_path)
    t1 = 0.0
    close_eye = 0.0
    
    capture = cv2.VideoCapture(0)  # USBカメラから
    
    while True:
        if not capture.isOpened():
            print("Capture is not opened.")
            break
        # カメラからフレーム画像を取得
        ret, frame = capture.read()
        if not ret:
            print("Failed to read frame.")
            break
        
        gray = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
        faces = face_1.detectMultiScale(gray, scaleFactor=1.11, minNeighbors=3, minSize=(100, 100))

        if len(faces) == 1:
            x,y,w,h = faces[0]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            
            face_gray = gray[y :(y + h), x :(x + w)]
            scale = 480 / h
            face_gray_resized = cv2.resize(face_gray, dsize=None, fx=scale, fy=scale)
            face = dlib.rectangle(0, 0, face_gray_resized.shape[1], face_gray_resized.shape[0])
            face_parts = face_parts_1(face_gray_resized, face)
            face_parts = face_utils.shape_to_np(face_parts)
            
            left = face_parts[42:48]
            left_ear = calc_ear(left)
            
            right = face_parts[36:42]
            right_ear = calc_ear(right)
            
            if (left_ear + right_ear) < 0.55:
                if t1 == 0.0:
                    t1 = time.time()
                else:
                    close_eye += time.time()-t1
                    t1 = time.time()
                cv2.putText(frame,str(round(close_eye)), (10,40), cv2.FONT_HERSHEY_PLAIN, 3, (0,0,255), 3, 1)  
                if close_eye > 3.0:
                    cv2.putText(frame,"Sleepy eyes. Wake up!", (10,80), cv2.FONT_HERSHEY_PLAIN, 2, (0,0,255), 3, 1)
                    playsound(Sound_path) 
            else:
                close_eye = 0.0
                t1 = 0.0

        # フレーム画像バイナリに変換
        ret, jpeg = cv2.imencode('.jpg', frame)
        byte_frame = jpeg.tobytes()
        # フレーム画像のバイナリデータをユーザーに送付する
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + byte_frame + b'\r\n\r\n')
    capture.release()

def calc_ear(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    eye_ear = (A + B) / (2.0 * C)
    return round(eye_ear, 3)

##------------video finish