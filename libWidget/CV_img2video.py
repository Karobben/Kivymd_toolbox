# -*- coding: utf-8 -*
import numpy as np
import cv2
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.core.window import Window

from kivy.uix.floatlayout import FloatLayout
from PIL import Image
from kivy.utils import platform
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.graphics.texture import Texture
from kivy.graphics import Rectangle
from kivy.properties import ObjectProperty
from kivy.clock import Clock


# My functions for cropping
from libs import img2video as Image2Video
import threading, time, os


class FunctionWidget():
    Image2Video = Image2Video.Main()
    Num = 0
    cap = None
    def main(self):
        Builder.unload_file("Layout/CV_img2video.kv")
        self.Function_page = Builder.load_file("Layout/CV_img2video.kv")
        img = cv2.imread('logo.png')
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (460, 320))
        #cap=cv2.VideoCapture("test.mp4")
        #ret,img=cap.read()
        # 画像をグレイスケールに変換
        #gray_img = cv2.cvtColor(img,1)
        self.texture = Texture.create(size=(460, 320), colorfmt='rgb', bufferfmt='ubyte') # BGRモードで用意,ubyteはデフォルト引数なので指定なくてもよい
        self.texture.blit_buffer(img.tostring(),colorfmt='rgb', bufferfmt='ubyte')  # ★ここもBGRで指定しないとRGBになって色の表示がおかしくなる
        self.texture.flip_vertical()
        #self.Function_page.ids.can_box.canvas.add(Rectangle(texture=self.texture ))
        #self.Function_page.ids.can_box.canvas.add(Rectangle(texture=self.texture , size=self.Function_page.ids.can_box.size))

        self.Function_page.show_pic  = self.texture
        # Connect to the load popup
        self.Function_page.ids.button_load.on_release = self.show_load
        self.Function_page.ids.button_start.on_release = self.processing
        self.Function_page.ids.slid_font.bind( on_touch_move = self.CV_play)
        Clock.schedule_interval(self.CV_play, 1)
        return self.Function_page


    def CV_play(self, *arg):
        '''
        This function is for show the frame with the slide.
        the value of the slide would be the frame of the video
        '''
        try:
            Num = self.Function_page.ids.slid_font.value-1
            print(os.listdir(self.PATH)[int(Num)])
            img_file = os.listdir(self.PATH)[int(Num)]
            img = cv2.imread(os.path.join(self.PATH,img_file ))
            img = cv2.resize(img, (460, 320))
            self.texture.blit_buffer(img.tobytes(),colorfmt='bgr', bufferfmt='ubyte')  # ★ここもBGRで指定しないとRGBになって色の表示がおかしくなる
            print(img_file)
            self.texture.flip_vertical()
        except:
            print("Failed Try")

    def processing(self, *arg):
        '''
        Main functon for the video cropping
        '''
        INPUT_file = os.path.join(self.path, self.filename[0])
        # FPS:
        FPS = self.Function_page.ids.FPS.text
        SIZE = self.Function_page.ids.window_size.text
        #Out put format config:
        if self.Function_page.ids.format_gif.active == True:
            FORMAT = 'gif'
        else:
            FORMAT = 'avi'

        # Starting processing the video. function try&except here is for avioding repeated procedures.
        ARGS_progress = (INPUT_file, FPS, SIZE, FORMAT, self.Function_page.ids.slid_font,
        self.Function_page.ids.label)
        #self.Image2Video.run(INPUT_file, FPS, SIZE, FORMAT)
        try:
            print("Check Here", self.Processin.is_alive())
            if self.Processin.is_alive() != True:
                print("second time")
                self.Processin = threading.Thread(target=self.Image2Video.run,
                    args=ARGS_progress)
                self.Processin.start()

        except:
            print("first time")
            self.Processin = threading.Thread(target=self.Image2Video.run,
                args = ARGS_progress)
            self.Processin.start()

    def show_load(self):
        content = img2video_LoadDialog(load=self.load, cancel=self.dismiss_popup)
        PATH = "."
        if platform == "android":
          from android.permissions import request_permissions, Permission
          request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
          app_folder = os.path.dirname(os.path.abspath(__file__))
          PATH = "/storage/emulated/0" #app_folder
        content.ids.filechooser.path = PATH

        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()
        print("WindowSize=",Window.height)

    def load(self, path, filename):
        print("\n"*10, self.Function_page.ids.can_box.size)
        if platform == "android":
            path = ""
        #path  = ""
        #filename = ["test.mp4"]
        self.filename = filename
        self.path = path
        self.PATH = os.path.join(path, filename[0])
        print("file load: ", self.PATH)
        try:
            img = cv2.imread(os.path.join(self.PATH, os.listdir(self.PATH)[0]))
            img = cv2.resize(img, (460, 320))
            # loading the first frame of the video
            self.texture = Texture.create(size=(460, 320), colorfmt='bgr', bufferfmt='ubyte')
            self.texture.blit_buffer(img.tobytes(),colorfmt='bgr', bufferfmt='ubyte')
            self.Function_page.show_pic  = self.texture
            self.texture.flip_vertical()
            # getther infor from the video
            self.Function_page.ids.slid_font.max = len(os.listdir(self.PATH))
            self.Function_page.ids.label.text = filename[0]
        except:
            print("file load faild.")
            self.Function_page.ids.label.text = filename[0]+"\nload failed"
        self.dismiss_popup()

    def dismiss_popup(self):
        self._popup.dismiss()


class img2video_LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)
