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
        Builder.unload_file("Layout/test.kv")
        self.Function_page = Builder.load_file("Layout/test.kv")
        self.Function_page.ids.button_load.on_release= self.run
        return self.Function_page

    def run(self, *args):
        img = cv2.imread('logo.png')
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        # 画像をグレイスケールに変換
        #gray_img = cv2.cvtColor(img,1)
        texture = Texture.create(size=(img.shape[1], img.shape[0]), colorfmt='rgb', bufferfmt='ubyte') # BGRモードで用意,ubyteはデフォルト引数なので指定なくてもよい
        texture.blit_buffer(img.tostring(),colorfmt='rgb', bufferfmt='ubyte')  # ★ここもBGRで指定しないとRGBになって色の表示がおかしくなる
        texture.flip_vertical()
        self.Function_page.show_pic  = texture
