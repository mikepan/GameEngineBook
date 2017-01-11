# #############################
# Video Texture Webcam Demo
# #############################
# This file is part of the book:
# "Game Development with Blender"
# by Dalai Felinto and Mike Pan
#
# Published by "CENGAGE Learning" in 2013
#
# You are free to use-it, modify it and redistribute
# as long as you keep the original credits when pertinent.
#
# File tested with Blender 2.66
#
# Copyright - February 2013
# This work is licensed under the Creative Commons
# Attribution-Share Alike 3.0 Unported License
# #############################
#
# Linux and Windows only.
# (webcam not support in OSX at the moment)
#
# Camera Resolution hardcoded in the code: 640,480
# If this resolution is not supported by the webcam,
# it will not work.
#
# ##############################

from bge import logic as G
from bge import texture as VT

import sys

def initWorld(cont):
    obj = cont.owner

    matID = VT.materialID(obj, 'MAvideo')
    G.video = VT.Texture(obj, matID)

    if sys.platform == 'darwin':
        print('webcam grabbing for FFMmpeg not supported on OSX at the moment (the backend for video texture)')
        return
    elif sys.platform == 'win32':
        video_source = VT.VideoFFmpeg('cam',0,20.0,640,480)
    else: # linux
        video_source = VT.VideoFFmpeg('/dev/video0',0, 20.0,640,480)

    G.video.source = video_source
    G.video.source.play()

def update():
    G.video.refresh(True)
