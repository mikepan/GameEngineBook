# #############################
# Video Texture Player Demo
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
from bge import render as R
import VideoTexture as VT

def init_world():
    cont = G.getCurrentController()
    owner = cont.owner

    scene   = G.getCurrentScene()
    objects = scene.objects

    buttons = {}
    buttons["play"]     = objects["UI_PLAY"]
    buttons["pause"]    = objects["UI_PAUSE"]
    buttons["stop"]     = objects["UI_STOP"]
    buttons["sound"]    = objects["UI_SOUND"]
    buttons["mute"]     = objects["UI_MUTE"]
    G.buttons = buttons

    G.buttons["pause"].visible = 0
    G.buttons["mute"].visible = 0

    G.sound_mute = 1
    G.play_pause = 0

    G.sound = owner.actuators["a_sound"]
    G.sound_volume = G.sound.volume

    R.showMouse(True)
    init_video(objects["VIDEO_SCREEN"], objects["VIDEO_BLANK"])

def click():
    cont= G.getCurrentController()
    camera = cont.owner

    m_over= cont.sensors["s_mouseover"]
    m_click= cont.sensors["s_mouseclick"]

    if (m_over.positive and m_click.positive):

        # advanced screen space routines to handle clicking
        # Mouse sensor could be used instead
        # This way free us from adding logic bricks in every single button
        hit_point = m_over.hitPosition
        hit_screen_position = camera.getScreenPosition(hit_point)
        hit_object = camera.getScreenRay(hit_screen_position[0],hit_screen_position[1], 100, "button")

        if hit_object:
            name = hit_object["button"]
            if name == "play_pause":
                if G.play_pause == 0:
                    video_play()
                    G.buttons["play"].visible    = 0
                    G.buttons["pause"].visible    = 1
                    G.play_pause = 1
                else:
                    video_pause()
                    G.buttons["play"].visible    = 1
                    G.buttons["pause"].visible    = 0
                    G.play_pause = 0

            elif name == "stop":
                video_stop()
                G.buttons["play"].visible    = 1
                G.buttons["pause"].visible    = 0
                G.play_pause = 0

            elif name == "sound_mute":
                if G.sound_mute == 0:
                    video_volume()
                    G.buttons["sound"].visible    = 1
                    G.buttons["mute"].visible    = 0
                    G.sound_mute = 1
                else:
                    video_mute()

            elif name == "sound_increase":
                if G.sound_mute:
                    video_volume(0.1)
            elif name == "sound_decrease":
                if G.sound_mute:
                    video_volume(-0.1)

def init_video(video_obj, blank_obj):
    matID = VT.materialID(video_obj, 'MAvideo')

    G.video = VT.Texture(video_obj, matID)

    url = G.expandPath("//media/trailer_400p.ogg")
    video_source = VT.VideoFFmpeg(url)
    video_source.repeat = -1
    video_source.scale = True
    video_source.flip = True

    G.video.source = video_source

    G.video_screen    = video_obj
    G.video_blank    = blank_obj

    G.video_screen.visible    = False
#    G.video_blank.visible    = True

def video_play():
    G.video.source.play()
    G.sound.startSound()

    G.video_screen.visible    = True
    G.video_blank.visible    = False

def video_pause():
    G.video.source.pause()
    G.sound.pauseSound()

def video_stop():
    G.video.source.stop()
    G.sound.volume = 1.0
    G.sound.stopSound()

    G.video_screen.visible    = False
    G.video_blank.visible    = True

def video_volume(volume=0):
    TOP_VOLUME = 2.0
    BOT_VOLUME = 0.1

    if volume == 0:
        # unmute
        G.sound.volume = G.sound_volume

    else:
        # increase / decrease
        volume_tot = G.sound.volume + volume

        if volume_tot > TOP_VOLUME:        volume_tot = TOP_VOLUME
        elif volume_tot < BOT_VOLUME:
            mute()
            return
            # volume_tot = BOT_VOLUME

        G.sound.volume = volume_tot

def video_mute():
    G.sound_volume = G.sound.volume
    G.sound.volume = 0.0

    G.buttons["sound"].visible    = 0
    G.buttons["mute"].visible    = 1
    G.sound_mute = 0

def video_update():
    if G.play_pause:
        G.video.refresh(True, G.sound.time)

#        if G.sound_mute:
#            G.video.refresh(True, G.sound.time)
#
#        else:
#            G.video.refresh(True)
