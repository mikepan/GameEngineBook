# #############################
# Video Texture Mirror Demo
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

from bge import logic as G
from bge import texture as VT

def initWorld(cont):
    obj = cont.owner
    scene = G.getCurrentScene()

    matID = VT.materialID(obj, 'MAvideo')
    G.video = VT.Texture(obj, matID)

    video_source = VT.ImageMirror(scene,scene.active_camera,obj,matID)
    video_source.background = (68,68,68,255)

    G.video.source = video_source
    G.video.refresh(False)

def update():
    G.video.refresh(False)
