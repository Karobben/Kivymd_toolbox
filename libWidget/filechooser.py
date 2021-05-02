from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivy.utils import platform
import os
from kivy.core.window import Window


class ConfirmPopup(BoxLayout):
    def __init__(self, **kwargs):
        Builder.unload_file("./Layout/filechooser.kv")
        Builder.load_file("./Layout/filechooser.kv")
        self.register_event_type('on_answer')
        self.register_event_type('on_cancel')
        super(ConfirmPopup, self).__init__(**kwargs)
        self.total_images = 0

    def on_answer(self, filename, MainPage):
        self.total_images = filename
        print(Window.size)
        if len(filename) >0:
            MainPage.change_text(self.total_images)
        else:
            MainPage.change_text("Please Select a File")

    def on_cancel(self, filename, MainPage):
        pass


    def popup_func(self, *args):
        content = ConfirmPopup()
        content.bind(on_answer = self._on_answer)
        content.bind(on_cancel = self._on_answer)
        PATH = "."
        if platform == "android":
          from android.permissions import request_permissions, Permission
          request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
          app_folder = os.path.dirname(os.path.abspath(__file__))
          PATH = "/storage/emulated/0/" #app_folder
        content.ids.filechooser.path = PATH
        #content.bind(Cancel    = self._on_answer)
        self.popup = Popup(title="Select mutiple files",
                           content=content,
                           size_hint=(None, None),
                           size = [int(i * .7 ) for i in Window.size],
                           auto_dismiss=True)
        self.popup.open()

    def _on_answer(self, instance, answer, obj):
        self.popup.dismiss()

    def dismiss(self):
        self.popup.dismiss()
