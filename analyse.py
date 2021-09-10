import os, sys
import torch
import torchaudio
import numpy as np
import matplotlib.pyplot as plt
import cv2
import subprocess
from moviepy.editor import *


folders =  ['CW', 'CW_MSAE', 'CW_MSAE_prune', 'Imperceptible', 'Imperceptible_MSAE', 'IPC', 'IPC_MSAE']

for folder in folders:
    for idx1, (fpath, dirname, fnames) in enumerate(os.walk('C:/Users/jzy/Desktop/MSAE_demo_website/'+folder)):
        count = 0
        for fname in fnames:
            rot_label = False
            if fname[-3:] == 'png' and 'noise' not in fname:
                adv_img = cv2.imread(fpath+'/'+fname)
                print(adv_img.shape)
                if adv_img.shape[0] != 112:
                    adv_img = np.reshape(adv_img,(-1,112,112,3))
                else:
                    rot_label = True
                    adv_img = adv_img.transpose((1,0,2))
                    adv_img = np.reshape(adv_img,(-1,112,112,3))
                    #adv_img = adv_img.transpose((0,2,1,3))
                    print(adv_img.shape)
                
                
                video_dir = fpath + '/' + fname[:-3] + 'avi'
                fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
                videowriter = cv2.VideoWriter(video_dir, fourcc, 24, (112,112))
                for frame in adv_img:
                    videowriter.write(cv2.flip(np.rot90(frame,3),1) if rot_label else frame)
                videowriter.release()
                
                adv_audio = AudioFileClip(video_dir[:-3]+'wav')

                video = VideoFileClip(video_dir)
                video = video.set_audio(adv_audio)
                video.write_videofile(video_dir[:-3]+'mp4')
                print(adv_img.shape)
                print(adv_img)


                