# -*- coding: utf-8 -*
import numpy as np
import cv2
from kivy.uix.boxlayout import BoxLayout

from PIL import Image
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.graphics.texture import Texture
from kivy.graphics import Rectangle


class FunctionWidget():

    def main(self):
        Builder.unload_file("Layout/CV_video_crop.kv")
        self.Function_page = Builder.load_file("Layout/CV_video_crop.kv")
        img = cv2.imread('logo.png')
        # 画像をグレイスケールに変換
        #gray_img = cv2.cvtColor(img,1)
        texture = Texture.create(size=(img.shape[1], img.shape[0]), colorfmt='bgr', bufferfmt='ubyte') # BGRモードで用意,ubyteはデフォルト引数なので指定なくてもよい
        texture.blit_buffer(img.tostring(),colorfmt='bgr', bufferfmt='ubyte')  # ★ここもBGRで指定しないとRGBになって色の表示がおかしくなる
        texture.flip_vertical()
        self.Function_page.show_pic  = texture
        print(self.Function_page.show_pic)
        return self.Function_page
