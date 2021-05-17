from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.utils import platform
import os
import webbrowser, time
import threading

class FunctionWidget():

    def main(self):
        Builder.unload_file("Layout/Blog.kv")
        self.Function_page = Builder.load_file("Layout/Blog.kv")
        self.Function_page.ids.buton_start.on_release = self.open_blog
        self.Function_page.ids.buton_close.on_release = self.close_blog
        return self.Function_page

    def run_sever(self):
        import http.server
        import socketserver
        PORT = 5500
        Handler = http.server.SimpleHTTPRequestHandler
        with socketserver.TCPServer(("", PORT), Handler) as self.httpd:
            print("serving at port", PORT)
            self.httpd.serve_forever()

    def close_blog(self):
        PATH = os.path.abspath(__file__).split("libWidget")[0].replace("appc","app")
        print(PATH)

        try:
            self.httpd.shutdown()
            os.chdir(PATH)
        except:
            os.chdir(PATH)



    def open_blog(self, *args):
        if platform == "android":
            from libs.webview import WebView
        os.chdir("Blog")
        PATH = os.path.abspath(__file__).split("libWidget")[0].replace("appc","app")
        URL = 'file://'+PATH+'/demo/clustal/123.html',
        URL = 'http://127.0.0.1:5500/'
        print("URL = ", URL)
        x = threading.Thread(target=self.run_sever, args=())
        x.start()
        print("Started, test")
        if platform == "android":
            self.browser = None
            self.browser = WebView(URL,
                                   enable_javascript = True,
                                   enable_downloads = True,
                                   enable_zoom = True)
        else:
            try:
                webbrowser.open('http://127.0.0.1:5500/')
            except:
                pass
