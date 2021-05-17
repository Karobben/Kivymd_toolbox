from kivy.app import App
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.clock import Clock
import numpy as np
import cv2, os
from kivy.utils import platform


_PATH = "./"
if platform == "android":
    os.environ["IMAGEIO_FFMPEG_EXE"] = "/storage/emulated/0/0/ffmpeg"
    _PATH = "/storage/emulated/0/Music/"

'''
from moviepy.editor import VideoFileClip
print("Started to convert mp4")


video_path = 'test.mp4'   #视频地址
audio_path = _PATH + 'my_audio.mp3'   #提取音频保存位置
video = VideoFileClip(video_path)
video.audio.write_audiofile(audio_path)

print("convert completed" )
print("saved at")
'''

Builder.unload_file('Layout/CV_test.kv')
Builder.load_file('Layout/CV_test.kv')

class AndroidCamera(Camera):
    camera_resolution = (640, 480)
    cam_ratio = camera_resolution[0] / camera_resolution[1]

class MyLayout(BoxLayout):
    pass


class FunctionWidget():

    def main(self):
        return MyLayout()

    def on_start(self):
        Clock.schedule_once(self.get_frame, 5)

    def get_frame(self, dt):
        cam = self.root.ids.a_cam
        image_object = cam.export_as_image(scale=round((400 / int(cam.height)), 2))
        w, h = image_object._texture.size
        frame = np.frombuffer(image_object._texture.pixels, 'uint8').reshape(h, w, 4)
        gray = cv2.cvtColor(frame, cv2.COLOR_RGBA2GRAY)
        self.root.ids.frame_counter.text = f'frame: {self.counter}'
        self.counter += 1
        Clock.schedule_once(self.get_frame, 0.25)
