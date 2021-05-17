from kivy.app import App
from custom_camera.custom_camera import CameraWidget, CustomCamera

from kivy.base import Builder
from kivy.uix.floatlayout import FloatLayout



class FunctionWidget(FloatLayout):

    def main(self):
        self.Function_page = Builder.load_file("custom_camera/custom_camera.kv")
        camera = CameraWidget()
        self.Function_page.add_widget(camera)
        return self.Function_page
        #return camera
