#from kivy.lang import Builder
from kivy.lang import Builder
from kivy.uix.popup import Popup

from libWidget.filechooser import ConfirmPopup as Filerchooser_seq
from libWidget.menu import Menu as Seq_Menu
from pypinyin import lazy_pinyin as pinyin
import opencc

class FunctionWidget():
    Seq_Menu = Seq_Menu()
    def on_Seq_answer(self, filename, MainPage):
        if len(filename) >0:
            MainPage.change_text2(filename)
        else:
            MainPage.change_text2("Please Select a File")


    Filerchooser_seq = Filerchooser_seq()
    Filerchooser_seq.on_answer = on_Seq_answer

    def OPEN(self, file):
        return open(file).read()

    def change_text2(self, Files):
        self.Button_test.text = Files[0]
        self.Function_page.ids.seq_result.text = Files[0]
        print(str(Files))

    def PP(self):
        self.Function_page.ids.seq_result.text = self.Function_page.ids.seq_input.text.upper()

    def main(self):
        self.popup = Popup(title="Select .zip file",
                           content=None,
                           size_hint=(None, None),
                           size=(500, 500),
                           auto_dismiss=True)

        self.Function_page = Builder.load_string(self.OPEN("Layout/Seq.kv"))
        self.Function_page.ids.upper.on_release = self.PP
        # bind the menu
        self.Function_page.ids.upper2.on_release = self.Seq_Menu.pop
        self.Seq_Menu.menu.caller = self.Function_page.ids.upper2
        # Change the items in menu
        self.Font_list = {"繁体": "FangZhengHeiTiFanTi-1.ttf", "拼音":"FangZhengKaiTiPinYinZiKu-1.ttf", "新篆":"HuaKangXinZhuanTi-1.ttf", "角篆":"JingDianFanJiaoZhuan-1.ttf"}
        for i in range(len(self.Font_list)):
            Name = " ".join([i for i in pinyin(list(self.Font_list.keys())[i])])
            self.Seq_Menu.menu.items[i]['text'] = Name
            self.Seq_Menu.menu.items[i]['on_release'] = lambda x=list(self.Font_list.keys())[i]: self.menu_callback(x)
            self.Seq_Menu.menu.items[i]['font_name'] = "./font/" + self.Font_list[list(self.Font_list.keys())[i]]
        self.Seq_Menu.menu.bind(on_release = self.menu_callback)
        #self.Seq_Menu.menu.test = "I am Changed"
        return self.Function_page

    def menu_callback(self, Text):
        print("instance_menu", Text)
        if Text == "新篆":
            cc = opencc.OpenCC('s2t')
            self.Function_page.ids.seq_result.text = cc.convert(self.Function_page.ids.seq_result.text)
        else:
            cc = opencc.OpenCC('t2s')
            self.Function_page.ids.seq_result.text = cc.convert(self.Function_page.ids.seq_result.text)

        self.Function_page.ids.seq_result.font_name = "./font/" + self.Font_list[Text]
        self.Function_page.ids.upper2.text =  Text
        self.Function_page.ids.upper2.font_name = "./font/" + self.Font_list[Text]
        self.Seq_Menu.menu.dismiss()
        #self.test ="Page Chaged"
        #print(self.test)
