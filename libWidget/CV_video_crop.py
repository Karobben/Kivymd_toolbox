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


# My functions for cropping
from libs import CV_SameFrameDelete as CV_SFD
import threading, time, os


class FunctionWidget():
    Num = 0
    cap = None
    def main(self):
        Builder.unload_file("Layout/CV_video_crop.kv")
        self.Function_page = Builder.load_file("Layout/CV_video_crop.kv")
        img = cv2.imread('logo.png')
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        #cap=cv2.VideoCapture("test.mp4")
        #ret,img=cap.read()
        # 画像をグレイスケールに変換
        #gray_img = cv2.cvtColor(img,1)
        self.texture = Texture.create(size=(img.shape[1], img.shape[0]), colorfmt='rgb', bufferfmt='ubyte') # BGRモードで用意,ubyteはデフォルト引数なので指定なくてもよい
        self.texture.blit_buffer(img.tostring(),colorfmt='rgb', bufferfmt='ubyte')  # ★ここもBGRで指定しないとRGBになって色の表示がおかしくなる
        self.texture.flip_vertical()
        self.Function_page.show_pic  = self.texture
        # Connect to the load popup
        self.Function_page.ids.button_load.on_release = self.show_load
        self.Function_page.ids.button_start.on_release = self.processing
        self.Function_page.ids.slid_font.bind( on_touch_move = self.CV_play, on_touch_up = self.CV_play)
        return self.Function_page

    def play(self):
        x = threading.Thread(target=self.CV_play, args=())
        x.start()
        x.join()

    def CV_play(self, *arg):
        print(self.Function_page.ids.slid_font.value )
        #cap=cv2.VideoCapture("test.mp4")
        try:
            self.cap.set(cv2.CAP_PROP_POS_FRAMES,self.Function_page.ids.slid_font.value )
            a, img=self.cap.read()
            self.texture = Texture.create(size=(img.shape[1], img.shape[0]), colorfmt='bgr', bufferfmt='ubyte') # BGRモードで用意,ubyteはデフォルト引数なので指定なくてもよい
            self.texture.blit_buffer(img.tostring(),colorfmt='bgr', bufferfmt='ubyte')  # ★ここもBGRで指定しないとRGBになって色の表示がおかしくなる
            self.texture.flip_vertical()
            self.Function_page.show_pic  = self.texture
        except:
            pass

    def processing(self, *arg):
        INPUT_file = os.path.join(self.path, self.filename[0])
        CV_SFD.File = INPUT_file
        CV_SFD.OUTPUT = INPUT_file+".avi"
        CV_SFD.Thre = 20000
        CV_SFD.Back_progress = self.Function_page.ids.label
        #print(CV_SFD.Back_progress)
        #def test():
        CV_SFD.Back_progress.text = "Changed"
        CV_SFDel = CV_SFD.Main()
        #CV_SFDel.run()
        x = threading.Thread(target=CV_SFDel.run, args=(self.Function_page.ids.label, self.Function_page.ids.slid_font))
        x.start()
    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
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
        if platform == "android":
            path = ""
        #path  = ""
        #filename = ["test.mp4"]
        self.filename = filename
        self.path = path
        print("file load: ",os.path.join(path, filename[0]))
        try:
            #self.cap =cv2.VideoCapture(os.path.join(path, filename[0]))
            self.cap =cv2.VideoCapture(os.path.join(path, filename[0]))
            fps_c = self.cap.get(cv2.CAP_PROP_FRAME_COUNT)
            self.Function_page.ids.slid_font.max = fps_c
            print("path exist:", os.path.exists(os.path.join(path,filename[0])),"total fps:", fps_c,sep="\n")
            self.dismiss_popup()
            self.Function_page.ids.label.text = filename[0]
        except:
            print("file load faild.")
            self.Function_page.ids.label.text = filename[0]+"\nload failed"

    def dismiss_popup(self):
        self._popup.dismiss()


class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)
