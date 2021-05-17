# Kivymd_toolbox
This is an android toolbox write by kivy. I'll keep updateing...

---

Introduction:
This app is contributed by four main directores: `libs`, `libWidget`, `Layout`, and `config`.
- `libs` if for storing some function scripts.
- `libWidget` is the GUI logic of each "Tabs" with paired `kv` file in `Layout`. Finally,
- `config` is holding some data for initializing the App

Functions:
- [x] [Chinese Font Switch](#user-content-font)
- [x] [Dynamic Tabs manager](#user-content-dynamic-tabs-manager)
- [x] [Editor](#user-content-editor)
- [x] [Web Server](#user-content-web-server)



# Font

This is a test function. You can change the font of the text you typed in with a menu button.

# Dynamic Tabs manager

[Dynamic Tbas manager](https://karobben.github.io/2021/05/07/Python/kivy-inaction-tb-4/)
[Home page config](https://karobben.github.io/2021/05/08/Python/kivy-inaction-tb-6/)
I moved the dictionary for tabs-initialize into `Navi.json` in `config` directory. So, the `main.py` looks much tidy know. You can open and close tabs free. But you may counter some bug if you opened tow or more same tabs.

# Editor

[Details for editor](https://karobben.github.io/2021/05/08/Python/kivy-inaction-tb-5/)
This Tap makes you create/change files much easier than using other android since it reading files wiht python. You can read all text files with ignoring the suffix of the them. For example, '\*.md', "\*.fasta", "\*.css"

# Web Server

[Details for Web server](https://karobben.github.io/2021/05/10/Python/kivy-inaction-tb-7/)

This is sample http sever  

# OpenCV camera

[More Details](https://karobben.github.io/2021/05/15/Python/kivy-inaction-tb-8/)
