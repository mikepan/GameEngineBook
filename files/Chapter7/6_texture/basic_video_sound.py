# #############################
# Video Texture Sound Demo
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

# #############################
# Video Texture Sound Demo
# Derived from Benoit Bolsee's original demo file
# #############################

from bge import logic as G
from bge import texture as VT

def initWorld(cont):
    obj = cont.owner

    matID = VT.materialID(obj, 'MAvideo')
    G.video = VT.Texture(obj, matID)

    url = G.expandPath("//media/trailer_400p.ogg")
    video_source = VT.VideoFFmpeg(url)

    video_source.repeat = -1
    video_source.scale = False

    G.video.source = video_source
    G.video.source.play()

    # SOUND
    sound = cont.actuators["a_sound"]
    cont.activate(sound)

    G.sound = sound

def update():
    G.video.refresh(True, G.sound.time)
