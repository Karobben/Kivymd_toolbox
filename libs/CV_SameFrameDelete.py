#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/17
# @Author  : Karobben
# @Site    : China
# @File    : CV_SameFrameDelete.py
# @Software: Atom

# for animation
import sys
import cv2
import time

class Main():
    File = None
    OUTPUT = None
    Thre = None
    Back_progress = None
    Format = "mp4"
    def progress_bar(self, i):
        '''
        A sample function for making an progress-bar
        '''
        print("\r", end="")
        print("Progress: {}%: \t".format(i, '.3f'), "▋" * (int(i) // 2), end="")
        sys.stdout.flush()
        time.sleep(0.05)

    def Diff_img(self,img0, img):
      '''
      This function is designed for calculating the difference between two
      images. The images are convert it to an grey image and be resized to reduce the unnecessary calculating.
      '''
      # Grey and resize
      img0 =  cv2.cvtColor(img0, cv2.COLOR_RGB2GRAY)
      img =  cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
      img0 = cv2.resize(img0, (320,200), interpolation = cv2.INTER_AREA)
      img = cv2.resize(img, (320,200), interpolation = cv2.INTER_AREA)
      # Calculate
      Result = (abs(img - img0)).sum()
      return Result

    # Acquiring the basic args of the video
    def run(self, Back_progress, Progres_bar, Min, Max):
        self.Back_progress = Back_progress
        self.Progres_bar = Progres_bar
        self.Video = File
        cap=cv2.VideoCapture(self.Video)
        ret,self.frame0 = cap.read()
        frames_Total=cap.get(7)

        fps_c = cap.get(cv2.CAP_PROP_FPS)
        Video_h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        Video_w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

        fps = fps_c
        print("fps =", fps)
        size = (Video_w,Video_h)
        print(Format)
        if Format == 'mp4':
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            OUTPUT = File + ".mp4"
        elif Format == 'avi':
            fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
            OUTPUT = File + ".avi"

        self.videowriter = cv2.VideoWriter(OUTPUT,fourcc,fps,size)
        self.Result = []
        self.fps_all = cap.get(cv2.CAP_PROP_FRAME_COUNT)
        Num = 0
        print(self.fps_all)
        self.cap=cv2.VideoCapture(self.Video)


        #self.Processing_whole()
        print("\n"*3,"video slice here: ",Max, Min)
        if Min == "" and Max == "":
            self.Processing_whole()
        else:
            if Min == "":
                Min = 0
            if Max == "":
                Max = self.fps_all
            print("from to:", Min, Max)
            self.Processing_slice(Min, Max)


    def Processing_whole(self):
        '''
        while function is much faster than for loop
        '''
        Num = 0
        while Num +1 < self.fps_all:
          Num += 1
          ret,frame=self.cap.read()
          if Num > 0:
            Diff = self.Diff_img(self.frame0, frame)
            self.Result += [Diff]
            self.frame0 = frame
            if Diff > Thre:
              self.videowriter.write(self.frame0)
          Progress_Num = round(Num /self.fps_all * 100, 3)
          self.Back_progress.text =  "".join([str(Progress_Num), "%\n",
                "[b][color=#3697ce]I[/color][/b]"* int(Progress_Num/5),
                "[b][color=#ce4c36]I[/color][/b]"* (20-int(Progress_Num/5))])
          self.Progres_bar.value = Num
          self.progress_bar(round(Num /self.fps_all * 100, 3))
        self.videowriter.release()
        self.Back_progress.text = "processing is down"

    def Processing_slice(self, Min, Max):
        '''
        For loop could save your time for slicing
        But it runs slower about 1/5 than while loop
        '''
        Min = int(Min)
        Max = int(Max)
        Num = 0
        for i in range(Min,Max):
          self.cap.set(cv2.CAP_PROP_POS_FRAMES, i)
          ret,frame=self.cap.read()
          Diff = self.Diff_img(self.frame0, frame)
          self.Result += [Diff]
          self.frame0 = frame
          if Diff > Thre:
            self.videowriter.write(self.frame0)
          Progress_Num = round(Num /(Max - Min) * 100, 3)
          self.Back_progress.text =  "".join([str(Progress_Num), "%\n",
               "[b][color=#3697ce]I[/color][/b]"* int(Progress_Num/5),
            "[b][color=#ce4c36]I[/color][/b]"* (20-int(Progress_Num/5))])
          self.Progres_bar.value = Num
          self.progress_bar(round(Num /(Max - Min) * 100, 3))
          Num += 1

        self.videowriter.release()
        self.Back_progress.text = "processing is down"
