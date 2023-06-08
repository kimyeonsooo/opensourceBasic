import tkinter as tk
import cv2
from PIL import Image, ImageTk
from face_detection import process_frame
from save_snapshot import save_snapshot


class VideoApp:
    def __init__(self, window, window_title, video_source=0, face_net=None, age_net=None, gender_net=None):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source
        self.vid = cv2.VideoCapture(video_source)
        self.window.protocol('WM_DELETE_WINDOW', self.destroy)

        self.canvas = tk.Canvas(window, width=self.vid.get(
            cv2.CAP_PROP_FRAME_WIDTH), height=self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.canvas.pack()

        self.btn_snapshot = tk.Button(
            window, text="Snapshot", width=50, command=self.snapshot)
        self.btn_snapshot.pack(anchor=tk.CENTER, expand=True)

        self.delay = 15
        self.face_net = face_net
        self.age_net = age_net
        self.gender_net = gender_net
        self.update()

        self.window.mainloop()

    def snapshot(self):
        ret, frame = self.vid.read()
        if ret:
            result_img, data = process_frame(
                self.face_net, self.age_net, self.gender_net, frame)
            save_snapshot(result_img, data)

    def update(self):
        ret, frame = self.vid.read()
        if ret:
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(
                process_frame(self.face_net, self.age_net, self.gender_net, frame)[0]))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
        self.window.after(self.delay, self.update)

    def destroy(self):
        self.vid.release()
        self.window.destroy()
