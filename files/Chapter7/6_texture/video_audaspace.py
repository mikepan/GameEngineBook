# #############################
# Video Texture + Audaspace Demo
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

from bge import logic
from bge import texture

def initWorld(cont):
    object = cont.owner

    matID = texture.materialID(object, 'MAvideo')
    logic.video = texture.Texture(object, matID)

    url = logic.expandPath("//media/trailer_400p.ogg")
    video_source = texture.VideoFFmpeg(url)

    video_source.repeat = -1
    video_source.scale = True

    logic.video.source = video_source
    logic.video.source.play()

    # SOUND
    import aud
    device = aud.device()
    factory = aud.Factory(url)
    handle = device.play(factory)

    logic.sound = handle

def update():
    # note we are using position and not time here
    logic.video.refresh(True, logic.sound.position)
