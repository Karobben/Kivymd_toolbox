from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.app import MDApp

#KV = '''
'''
Screen:

    MDRaisedButton:
        id: button
        text: "PRESS ME"
        pos_hint: {"center_x": .5, "center_y": .5}
        on_release: app.menu.open()
'''


class Menu(MDFloatLayout):
    #menu = MDDropdownMenu()
    Num = 4
    def __init__(self, **kwargs):
        #super().__init__(**kwargs)
        self.menu_items = [{"text": f"Item {i}",
                       "viewclass": "OneLineListItem",
                       'font_name': "./font/FangZhengHeiTiJianTi-1",
                        "on_release": lambda x=f"Item {i}": self.menu_callback(x)} for i in range(self.Num)]
        self.menu = MDDropdownMenu(
            #caller=self.screen.ids.button,
            caller= None,
            items=self.menu_items,
            width_mult=4,
        )
        self.menu.bind(on_release=self.menu_callback)
        print(123)
        #return self.menu
    #
    def menu_callback(self,  instance_menu_item):
        print("instance_menu", instance_menu_item)
        #self.page_callback()
        self.test ="Change Page"
        print(self.test)

        self.menu.dismiss()

    def page_callback(self):
        self.test ="Change Page"
        print(self.test)

    # let's start
    def pop(self):
        self.menu.open()
