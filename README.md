# Kivymd_toolbox
This is an android toolbox write by kivy. I'll keep updating...

---

Introduction:
This app is contributed by four main directories: `libs`, `libWidget`, `Layout`, and `config`.
- `libs` if for storing some function scripts.
- `libWidget` is the GUI logic of each "Tabs" with paired `kv` file in `Layout`. Finally,
- `config` is holding some data for initializing the App

Functions:
- [x] [Chinese Font Switch](#user-content-font)
- [x] [Dynamic Tabs manager](#user-content-dynamic-tabs-manager)
- [x] [Editor](#user-content-editor)
- [x] [Web Server](#user-content-web-server)
- [X] [Opencv and Camera](#user-content-opencv-camera)
- [X] [Video Crop](#user-content-video-crop)
  - [x] Set a thresholds
  - [x] different format for output
  - [x] Slice

# Font

This is a test function. You can change the font of the text you typed in with a menu button.

# Dynamic Tabs manager

[Dynamic Tbas manager](https://karobben.github.io/2021/05/07/Python/kivy-inaction-tb-4/)
[Home page config](https://karobben.github.io/2021/05/08/Python/kivy-inaction-tb-6/)
I moved the dictionary for tabs-initialize into `Navi.json` in `config` directory. So, the `main.py` looks much tidy now. You can open and close tabs free. But you may counter some bug if you opened two or more same tabs.

# Editor

[Details for editor](https://karobben.github.io/2021/05/08/Python/kivy-inaction-tb-5/)
This Tap makes you create/change files much easier than using other android apps since it reading files with python. You can read all text files by ignoring the suffix of the files. For example, '\*.md', "\*.fasta", "\*.css"
# Web Server

[Details for Web server](https://karobben.github.io/2021/05/10/Python/kivy-inaction-tb-7/)

This is a sample http server which achieved by `http.server` and `socketserver`. It was run in the background with the help of `threading`


You can either open the default browser or using the android webbrowser server to start it. The code of android webbrowser was written by [RobertFlatt](https://github.com/RobertFlatt) and published in [ RobertFlatt /Android-for-Python ](https://github.com/RobertFlatt/Android-for-Python/tree/main/webview). He also contributed lots of other awesome functions and examples of widgets.


# OpenCV camera

[More Details](https://karobben.github.io/2021/05/15/Python/kivy-inaction-tb-8/)

# Video Crop
This is a Widget for deleting the same frames. It works as:
$Video =  \sum_{i=0}^{n} frame_n$
$New\ Video = \sum_{i=0}^{n}frame_ {n-1}((frame_n - frame_{n-1})> Thresholds)$
