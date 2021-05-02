from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from menu import Menu as Seq_Menu
from kivymd.uix.button import MDRectangleFlatButton
# import this script

class MainApp(MDApp):
    def build(self):
        screen = Screen()
        self.Seq_Menu = Seq_Menu()
        self.Button = MDRectangleFlatButton(
            text="Hello, World",
            pos_hint={"center_x": 0.5, "center_y": 0.5})
        self.Button.on_release = self.Seq_Menu.pop
        self.Seq_Menu.menu.caller = self.Button
        self.Seq_Menu.menu.bind(on_release = self.menu_callback)

        for i in range(len(self.Seq_Menu.menu.items)):
            self.Seq_Menu.menu.items[i]['text'] = "A" + str(i)
            self.Seq_Menu.menu.items[i]['on_release'] = lambda x=str(i)+": test": self.menu_callback(x)
        screen.add_widget(self.Button)

        return screen

    def menu_callback(self, Text):
        print(123, Text)
        self.Button.text = "Choosed: "+Text
        self.Seq_Menu.menu.dismiss()


MainApp().run()
