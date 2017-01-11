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
# Code written originally by Mitchell Stokes
# Adapted by Dalai Felinto
# #############################

# import game engine modules
from bge import render
from bge import logic
from bge import types
# import stand alone modules
import bgl
import blf

def init():
    """init function - runs once"""
    # create a new font object
    font_path = logic.expandPath('//fonts/CabinSketch.ttf')
    logic.font_id = blf.load(font_path)

    # set the font drawing routine to run   
    scene = logic.getCurrentScene()
    scene.post_draw=[draw_names]

# Far distance
FAR = 100
# The point size of the font for an object directly in front of the camera
FONT_SIZE = 50

# The drawing callback
def draw_names():
    # Get font id to use
    font_id = logic.font_id

    # Collect viewport information
    width= render.getWindowWidth()
    height= render.getWindowHeight()

    # Setup the OpenGL matrices
    bgl.glMatrixMode(bgl.GL_PROJECTION)
    bgl.glPushMatrix()
    bgl.glLoadIdentity()
    bgl.gluOrtho2D(0, width, 0, height)

    bgl.glMatrixMode(bgl.GL_MODELVIEW)
    bgl.glPushMatrix()
    bgl.glLoadIdentity()

    # Get the camera
    scene = logic.getCurrentScene()
    camera = scene.active_camera


    # draw the name only for objects (not for lamps or camera)
    for object in [i for i in scene.objects if i.__class__ == types.KX_GameObject]:
        # Calculate x and y
        screen_coord = camera.getScreenPosition(object)
        x = screen_coord[0] * render.getWindowWidth()
        y = render.getWindowHeight() - (screen_coord[1] * render.getWindowHeight())

        # Center the x
        text_width, text_height = blf.dimensions(0, object.name)
        x -= text_width / 2

        # Calculate the amount to scale the font
        distance = camera.getDistanceTo(object)

        if FAR - distance > 0:
          scale = (FAR - distance) / FAR
        else:
          scale = 0

        # Only draw if we'll be able to see it
        if scale:
            blf.size(font_id, int(FONT_SIZE*scale), 72)
            blf.position(font_id, x, y, 0)
            blf.draw(font_id, object.name)

    # Reset the matrices
    bgl.glPopMatrix()
    bgl.glMatrixMode(bgl.GL_PROJECTION)
    bgl.glPopMatrix()

