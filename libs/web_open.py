import webbrowser, os
from kivy.utils import platform

def Web_open(HTML):
    PATH = os.path.abspath(__file__).split("/libs/")[0].replace("appc","app")
    try:
        webbrowser.open(HTML)
    except:
        pass
    if platform == "android":
        from libs.webview import WebView
        browser = WebView('file://'+PATH+'/' +HTML,
                               enable_javascript = True,
                               enable_downloads = True,
                               enable_zoom = True)
