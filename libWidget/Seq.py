#from kivy.lang import Builder
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.utils import platform
from kivy.uix.popup import Popup
import os, shutil
import webbrowser, time
from kivy.uix.button import Button
#from Bio import AlignIO
from collections import defaultdict #this will make your life simpler

# for android webview
from jnius import autoclass

from kivy.uix.modalview import ModalView
from kivy.uix.label import Label
from libWidget.menu import Menu


class LoadDialog_Seq(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

class FunctionWidget():
    Menu.Num = 3
    Menu = Menu()
    def main(self):
        Builder.unload_file("Layout/Seq.kv")
        Builder.unload_file("Layout/Seq.kv")
        self.Function_page = Builder.load_file("Layout/Seq.kv")
        self.Function_page.ids.button_load.on_release = self.show_load #show_load
        # Menu show_select
        self.Function_page.ids.button_select.on_release = self.Menu.pop
        self.Menu.menu.caller = self.Function_page.ids.button_select
        self.Menu_reflash()
        return self.Function_page

    def Menu_reflash(self):
        # Change the items in menu
        self.Font_list = {"Demo": "Demo", "Clustal":"Clustal","Last Result":""}
        for i in range(len(self.Font_list)):
            Name = " ".join([i for i in list(self.Font_list.keys())[i]])
            self.Menu.menu.items[i]['text'] = Name
            self.Menu.menu.items[i]['on_release'] = lambda x = list(self.Font_list.keys())[i]: self.menu_callback(x)
        self.Menu.menu.bind(on_release = self.menu_callback)

    def menu_callback(self, Text):
        print("instance_menu", Text)
        self.Function_page.ids.button_select.text =  Text
        self.Function_page.ids.seq_result.text =  time.ctime() +": Modual selected - " +Text + "\n"+ self.Function_page.ids.seq_result.text
        '''
        self.Function_page.ids.upper2.font_name = "./font/" + self.Font_list[Text]
        self.Seq_Menu.menu.dismiss()
        #self.test ="Page Chaged"
        '''
        if Text == "Demo":
            self.demo()
        elif Text == "Last Result":
            self.demo_last()
        self.Menu.menu.dismiss()

    def fasta_read(self, FA):
        fasta = {}
        with open(FA) as file_one:
            for line in file_one:
                line = line.strip()
                if not line:
                    continue
                if line.startswith(">"):
                    active_sequence_name = line[1:]
                    if active_sequence_name not in fasta:
                        fasta[active_sequence_name] = []
                    continue
                sequence = line
                fasta[active_sequence_name].append(sequence)
        return fasta

    def Seq_clean(self):
        FASTA = self.fasta_read("clusttmp/result.aln-fasta.fasta")

        Result = ""
        for i in FASTA.keys():
            Seq = self.MarkDown(FASTA[i])
            print(Seq)
            tmp = "".join(["<tr>","<td>", i, "</td>",
                               "<td>",self.MarkDown(Seq), "</td>","</tr>"])
            Result += tmp
        print(Result)
        Result = "".join(["<table><tr><th>title1</th><th>title2</th><tr>", Result, "</table>"])

        return Result

    def MarkDown(self, Text):
      Result = ""
      for i in list(Text):
          if i == "a" or i == "A":
              i = "<mark class='A'>A</mark>"
          if i == "t" or i == "T":
              i = "<mark class='T'>T</mark>"
          if i == "c" or i == "C":
              i = "<mark class='C'>C</mark>"
          if i == "g" or i == "G":
              i = "<mark class='G'>G</mark>"
          Result += i
      return  Result

    def align(self,  file):
        self.Function_page.ids.seq_result.text = "readining"
        self.browser = None
        PATH = os.path.abspath(__file__).replace("/libWidget/Seq.py","").replace("appc","app")
        print(PATH)
        Script_path = os.path.join(PATH,"libs/clustalo.py")
        print("PATH script= " , os.path.abspath(__file__))
        print("PATH= " , PATH)
        print("libs 1 ", os.listdir(PATH))
        print("libs?? ", os.listdir(os.path.join(PATH,"libs")))
        print("Script_path", Script_path)
        print("Script_path", Script_path)
        path = "clusttmp"
        shutil.rmtree(path, ignore_errors=True)
        os.mkdir(os.path.join(PATH,path))
        try:
            Script_tmp = open(Script_path,'r').read()
        except:
             Script_tmp = open(Script_path+"txt",'r').read()

        Script_tmp = Script_tmp.replace("123.fa",file)
        OUTFILE = os.path.join(PATH,path, "clustalo.py")
        F = open(OUTFILE,'w')
        F.write(Script_tmp)
        F.close()
        import clusttmp.clustalo
        self.Function_page.ids.seq_result.text = file + "Finished!"
        SAMPLE  = open("123.html",'r').read()
        Result = self.Seq_clean()
        SAMPLE = SAMPLE.replace("BODYISHERE", Result)
        F = open("clusttmp/123.html",'w')
        F.write(SAMPLE)
        F.close()
        try:
            webbrowser.open('clusttmp/123.html')
        except:
            pass
        if platform == "android":
            from libs.webview import WebView
            self.browser = WebView('file://'+PATH+'/clusttmp/123.html',
                                   enable_javascript = True,
                                   enable_downloads = True,
                                   enable_zoom = True)
        #lambda a: webbrowser.open('http://www.bild.de/')
    def demo(self):
        self.browser = None
        PATH = os.path.abspath(__file__).replace("/libWidget/Seq.py","").replace("appc","app")
        try:
            webbrowser.open('demo/clustal/123.html')
        except:
            pass
        if platform == "android":
            from libs.webview import WebView
            self.browser = WebView('file://'+PATH+'/demo/clustal/123.html',
                                   enable_javascript = True,
                                   enable_downloads = True,
                                   enable_zoom = True)

    def demo_last(self):
        self.browser = None
        PATH = os.path.abspath(__file__).replace("/libWidget/Seq.py","").replace("appc","app")
        try:
            open("clusttmp/123.html")
            try:
                webbrowser.open('clusttmp/123.html')
            except:
                pass
            if platform == "android":
                from libs.webview import WebView
                self.browser = WebView('file://'+PATH+'/clusttmp/123.html',
                           enable_javascript = True,
                           enable_downloads = True,
                           enable_zoom = True)

        except:
            self.Function_page.ids.seq_result.text =  time.ctime() +"[color=#eb0047]Error, Can't find the last result[/color], please switch Clustal and selecte a fasta file\n" + self.Function_page.ids.seq_result.text


    def show_load(self):
        content = LoadDialog_Seq(load=self.load, cancel=self.dismiss_popup)
        PATH = "."
        if platform == "android":
          from android.permissions import request_permissions, Permission
          request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
          app_folder = os.path.dirname(os.path.abspath(__file__))
          PATH = "/storage/emulated/0" #app_folder
        content.ids.filechooser2.path = PATH

        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()


    def load(self, path, filename):
        print("path = ",path)
        self.align(os.path.join(path, filename[0]))
        self.dismiss_popup()
    def dismiss_popup(self):
        self._popup.dismiss()
