# #############################
# Python Module Controller Demo
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

""" this script will be re-load every frame.
Remember to save the file after you change-it. """
def reload_me(controller):
#    controller = logic.getCurrentController()
    own = controller.owner

    # edit the speed value and you will see the rotation changing
    # (try with values from 0.01 to 0.05)
    speed = 0.025

    # now try to comment and uncomment the following lines 
    # adding or removing # from the begin of the line)
    own.applyRotation([0,0,speed],0)
#    own.applyRotation([speed,0,0],0)
