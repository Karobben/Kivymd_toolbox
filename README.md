# Kivymd_toolbox
This is an android toolbox write by kivy. I'll keep updateing...
<<<<<<< HEAD
=======

Introduction:
This app is contributed by four main directores: `libs`, `libWidget`, `Layout`, and `config`.
- `libs` if for storing some function scripts.
- `libWidget` is the GUI logic of each "Tabs" with paired `kv` file in `Layout`. Finally,
- `config` is holding some data for initializing the App

Functions:
- [x] [Chinese Font Switch](#read_font)
- [x] [Dynamic Tabs manager]()
- [x] [Editor]()



# <a id="read_font">Font</a>

This is a test function. You can change the font of the text you typed in with a menu button.

# Dynamic Tabs manager

I moved the dictionary for tabs-initialize into `Navi.json` in `config` directory. So, the `main.py` looks much tidy know. You can open and close tabs free. But you may counter some bug if you opened tow or more same tabs.

# Editor

This Tap makes you create/change files much easier than using other android since it reading files wiht python. You can read all text files with ignoring the suffix of the them. For example, '\*.md', "\*.fasta", "\*.css"
