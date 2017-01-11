# #############################
# Blender Font Library Demo
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

# import game engine modules
from bge import render
from bge import logic
# import stand alone modules
import bgl
import blf

def init():
    """init function - runs once"""
    # create a new font object
    font_path = logic.expandPath('//fonts/Nunito.ttf')
    logic.font_id = blf.load(font_path)

    scene = logic.getCurrentScene()

    # object that contains the dynamic text
    logic.text = scene.objects["Scripts"]

    # set the font drawing routine to run   
    scene.post_draw=[write]

def write():
    """write on screen - it runs every frame"""
    width = render.getWindowWidth()
    height = render.getWindowHeight()

    # OpenGL setup
    bgl.glMatrixMode(bgl.GL_PROJECTION)
    bgl.glLoadIdentity()
    bgl.gluOrtho2D(0, width, 0, height)
    bgl.glMatrixMode(bgl.GL_MODELVIEW)
    bgl.glLoadIdentity()

    # BLF fun
    font_id = logic.font_id
    blf.position(font_id, (width*0.2), (height*0.3), 0)
    blf.size(font_id, 50, 72)
    blf.draw(font_id, logic.text["text"])
