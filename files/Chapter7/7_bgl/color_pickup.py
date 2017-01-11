# #############################
# Blender OpenGL Wrapper Demo
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
import bgl

cont = G.getCurrentController()
lamp   = cont.owner
sensor = cont.sensors["s_mouse_click"]

if sensor.positive:

    width = R.getWindowWidth()
    height = R.getWindowHeight()

    viewport = bgl.Buffer(bgl.GL_INT, 4)
    bgl.glGetIntegerv(bgl.GL_VIEWPORT, viewport);

    x = viewport[0] + sensor.position[0]
    y = viewport[1] + (height - sensor.position[1])

    pixels = bgl.Buffer(bgl.GL_FLOAT, [4])

    # Reads one pixel from the screen, using the mouse position
    bgl.glReadPixels(x, y, 1, 1, bgl.GL_RGBA, bgl.GL_FLOAT, pixels)

    # Change the Light colour
    lamp.color = [pixels[0], pixels[1], pixels[2]]
