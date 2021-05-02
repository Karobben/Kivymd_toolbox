from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivy.lang import Builder
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase

from kivymd.app import MDApp


# Function libs

def OPEN(file):
    return open(file).read()

class Tab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''

class MainApp(MDApp):
    def F_test(self, *args):
        print(123)

    def build(self):
        screen = Screen()
        # loading Navigation (left)
        Widget_navi = Builder.load_string(OPEN("Layout/Navigation_Draw.kv"))
        # loading navigation tags
        Widget_tabs = Builder.load_string(OPEN("Layout/Navigation_Tabs.kv"))
        self.Widget_tabs = Widget_tabs
        # loading The Function pages
        # Loading Sequencs function page

        screen.add_widget(Widget_tabs)
        screen.add_widget(Widget_navi)
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

        List = {"Seq":{'icon':"dna",'title':"Sequencs Tools"}}

        Tab1 = Tab(text="Bio")
        Tab1.add_widget(
            MDRectangleFlatButton(
                text="Hello, World",
                pos_hint={"center_x": 0.5, "center_y": 0.5},))
        self.Widget_tabs.ids.tabs.add_widget(Tab1)
        for i in List.keys():
            tmp_tab = Tab(text=List[i]['icon'])
            #Function = Builder.load_string(OPEN("Layout/"+i+".kv"))
            from libWidget.Seq import FunctionWidget
            Fun = FunctionWidget()
            tmp_tab.add_widget(Fun.main())
            self.Widget_tabs.ids.tabs.add_widget(tmp_tab)



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

MainApp().run()
