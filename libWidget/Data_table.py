#from kivy.lang import Builder
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.utils import platform
from kivy.uix.popup import Popup
import os, shutil
import webbrowser, time
from kivy.uix.button import Button
from xmltramp2 import xmltramp
#from Bio import AlignIO
from collections import defaultdict #this will make your life simpler

# for android webview
from jnius import autoclass

from kivy.uix.modalview import ModalView
from kivy.uix.label import Label
from libWidget.menu import Menu



class FunctionWidget():
    def main(self):
        self.Function_page = Builder.load_file("Layout/Data_table.kv")
        # Menu show_select
        self.Function_page.ids.button_select.on_release = self.demo
        return self.Function_page

    def demo(self):
        self.browser = None
        from libs.web_open import Web_open
        Web_open("demo/echart/index.html")
        '''
        PATH = os.path.abspath(__file__).split("/libWidget/")[0].replace("appc","app")
        HTML = "demo/echart/index.html"
        try:
            webbrowser.open(HTML)
        except:
            pass
        if platform == "android":
            from libs.webview import WebView
            self.browser = WebView('file://'+PATH+'/' +HTML,
                                   enable_javascript = True,
                                   enable_downloads = True,
                                   enable_zoom = True)
        '''
