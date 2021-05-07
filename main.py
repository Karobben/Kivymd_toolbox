from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase
from kivy.core.window import WindowBase
from kivymd.icon_definitions import md_icons


from kivymd.app import MDApp

from libWidget.filechooser import ConfirmPopup

WindowBase.softinput_mode = "below_target"

# Function libs

def OPEN(file):
    return open(file).read()

class Tab(FloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''

class MainApp(MDApp):
    ConfirmPopup = ConfirmPopup()
    PATH = "."
    def change_text(self, Files):
        #self.the_time.text = str(Files)
        self.Button_test.text = Files[0]
        print("main screen", str(Files))

    def F_test(self, *args):
        print(123)

    def build(self):
        screen = Screen()
        screen.change_text = self.change_text
        # loading Navigation (left)
        self.Widget_navi = Builder.load_string(OPEN("Layout/Navigation_Draw.kv"))
        # loading navigation tags
        self.Widget_tabs = Builder.load_string(OPEN("Layout/Navigation_Tabs.kv"))
        #self.Widget_tabs.ids.tabs.on_ref_press = self.on_ref_press(*args)

        # loading The Function pages
        # Loading Sequencs function page

        screen.add_widget(self.Widget_tabs)
        screen.add_widget(self.Widget_navi)
        return screen

    # Functions for Navigation Ta
    def on_start(self):
        from lib.bio_seq import Bio as FunBioSeq
        Fun = FunBioSeq()
        print(Fun.List())

        def PP():
            print(Function_page.ids.seq_input.text)
            Function_page.ids.seq_result.text = Function_page.ids.seq_input.text.upper()
            Fun = FunBioSeq()

        List = {"Seq":{'icon':"Characters",'title':"Sequencs Tools"}}
        name_tab = "Bio"
        Tab1 = Tab(
                 text=f"[ref={name_tab}][color=#fa937f][font=font/heydings-icons-1]{'X'}[/font][/color][/ref]  {name_tab}")

        self.Button_test =  MDRectangleFlatButton(
                text="1234567890\nqwertyuiopasdfghjklzxcvbnm\nQWERTYUIOPASDFGHJKLZXCVBNM",
                pos_hint={"center_x": 0.5, "center_y": 0.5},
                font_name = "./font/icon-works-webfont-2",
                on_release = self.ConfirmPopup.popup_func)
        Tab1.add_widget(self.Button_test)
        self.Widget_tabs.ids.tabs.add_widget(Tab1)
        '''
        Navigation test
        '''
        Button_test =  MDRectangleFlatButton(
                text="篆体",
                pos_hint={"center_x": 0.5, "center_y": 0.5},
                font_name = "./font/JingDianFanJiaoZhuan-1.ttf",
                on_release = self.run_test)
        self.Widget_navi.ids.nav_button.add_widget(Button_test)


        '''
        for i in List.keys():
            tmp_tab = Tab(text=List[i]['icon'])
            #Function = Builder.load_string(OPEN("Layout/"+i+".kv"))
            from libWidget.Seq import FunctionWidget
            Fun = FunctionWidget()
            screen_tmp = Screen()
            screen_tmp.name = i
            screen_tmp.add_widget(Fun.main())
            tmp_tab.add_widget(screen_tmp)
            self.Widget_tabs.ids.tabs.add_widget(tmp_tab)
        '''
    def run_test(self, *args):
        self.add_tag()
        self.Widget_navi.ids.nav_drawer.set_state("close")
        print(iter(list(self.Widget_tabs.ids.tabs.get_tab_list())))#switch_tab("X 篆书")

    def add_tag(self, *args):
        name_tab = " 篆书"
        Tag_title =  f"[ref={name_tab}][font=font/heydings-icons-1][color=#fa937f]{'X'}[/color][/font][/ref][font=./font/JingDianFanJiaoZhuan-1]{name_tab}[/font]"

        tmp_tab =Tab( text = Tag_title)
        from libWidget.Seq import FunctionWidget
        Fun = FunctionWidget()
        screen_tmp = Screen()
        screen_tmp.name = "Test"
        screen_tmp.add_widget(Fun.main())
        tmp_tab.add_widget(screen_tmp)
        self.Widget_tabs.ids.tabs.add_widget(tmp_tab)
        self.Widget_tabs.ids.tabs.switch_tab(Tag_title)


    # Functions for Navigation Tab Switch
    def on_tab_switch(
        self, instance_tabs, instance_tab, instance_tab_label, tab_text):
        '''Called when switching tabs.
        :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
        :param instance_tab: <__main__.Tab object>;
        :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
        :param tab_text: text or name icon of tab;
        '''
        instance_tab.ids.label.text = tab_text
    def on_ref_press(
        self,
        instance_tabs,
        instance_tab_label,
        instance_tab,
        instance_tab_bar,
        instance_carousel,
    ):
        '''
        The method will be called when the ``on_ref_press`` event
        occurs when you, for example, use markup text for tabs.

        :param instance_tabs: <kivymd.uix.tab.MDTabs object>
        :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>
        :param instance_tab: <__main__.Tab object>
        :param instance_tab_bar: <kivymd.uix.tab.MDTabsBar object>
        :param instance_carousel: <kivymd.uix.tab.MDTabsCarousel object>
        '''

        # Removes a tab by clicking on the close icon on the left.
        for instance_tab in instance_carousel.slides:
            if instance_tab.text == instance_tab_label.text:
                instance_tabs.remove_widget(instance_tab_label)
                break
MainApp().run()
