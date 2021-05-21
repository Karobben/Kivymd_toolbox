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
    def run(self, Back_progress, Progres_bar):
        Video = File
        cap=cv2.VideoCapture(Video)
        ret,frame0 = cap.read()
        frames_Total=cap.get(7)

        fps_c = cap.get(cv2.CAP_PROP_FPS)
        Video_h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        Video_w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

        fps = fps_c
        size = (Video_w,Video_h)
        #fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        videowriter = cv2.VideoWriter(OUTPUT+".mp4",fourcc,fps,size)



        Result = []
        fps_all = cap.get(cv2.CAP_PROP_FRAME_COUNT)
        Num = 0
        print(fps_all)
        while Num +1 < fps_all:
          Num += 1
          ret,frame=cap.read()
          if Num > 0:
            Diff = self.Diff_img(frame0, frame)
            Result += [Diff]
            frame0 = frame
            if Diff > Thre:
              videowriter.write(frame0)
          Back_progress.text =  str(round(Num /frames_Total * 100, 3))+"%"
          Progres_bar.value = Num
          #print("here", Back_progress.text)# = str(round(Num /frames_Total * 100, 3))+"%"
          self.progress_bar(round(Num /frames_Total * 100, 3))

        videowriter.release()
        Back_progress.text = "processing is down"
