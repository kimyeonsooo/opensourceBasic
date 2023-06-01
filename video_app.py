import tkinter as tk
import cv2
import datetime
from PIL import Image, ImageTk
from save_snapshot import save_snapshot

class VideoApp:
    #비디오 소스 및 gui 요소 초기화
    def __init__(self, window, window_title, video_source=0, face_net=None, age_net=None, gender_net=None):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source
        self.vid = cv2.VideoCapture(video_source)
        self.window.protocol('WM_DELETE_WINDOW', self.destroy)

        self.canvas = tk.Canvas(window, width=self.vid.get(
            cv2.CAP_PROP_FRAME_WIDTH), height=self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.canvas.pack()

        self.btn_snapshot = tk.Button(window, text="캡처", width=50, command=self.capture_snapshot, relief="flat")
        self.btn_snapshot.pack(anchor=tk.CENTER, expand=True)

        self.btn_csv = tk.Button(window, text="CSV 저장", width=50, command=self.save_csv, relief="flat")
        self.btn_csv.pack(anchor=tk.CENTER, expand=True)

        self.btn_record = tk.Button(window, text="비디오 녹화", width=50, command=self.record_video, relief="flat")
        self.btn_record.pack(anchor=tk.CENTER, expand=True)

        self.delay = 15
        self.delay = 15
        self.face_net = face_net
        self.age_net = age_net
        self.gender_net = gender_net
        self.update()

        self.window.mainloop()

    #스냅샷 버튼을 클릭 시, 현재 프레임에서 얼굴 분석 수행
    def snapshot(self):
        
    #비디오 프레임을 업데이트하고 GUI 창에 표시
    def update(self):
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.date_label.config(text=current_time)

        ret, frame = self.vid.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, (640, 480))
            image = Image.fromarray(frame)
            photo = ImageTk.PhotoImage(image=image)
            self.canvas.create_image(0, 0, image=photo, anchor=tk.NW)
            self.canvas.photo = photo  # 새로운 줄: photo 객체를 유지하기 위해 참조

        self.window.after(self.delay, self.update)

    #앱 종료 시 호출되는 함수
    def destroy(self):
        self.vid.release()
        self.window.destroy()

def start_gui(video_source):
    VideoApp(tk.Tk(), "Tkinter and OpenCV", video_source=video_source)

def main_loop(video_source):
    start_gui(video_source)