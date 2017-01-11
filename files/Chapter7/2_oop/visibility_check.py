# #############################
# Oriented Object Programming Demo
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

import bge
from bge import logic as G

# defines a function to hide/turn visible all the objects passed as argument
def change_visibility(objects, on_off):
    for obj in objects:
        obj.visible = on_off

# retrieve the stored groups to local variables
cube_group   = G.groups["cube"]
sphere_group = G.groups["sphere"]

# read the current value of the "on_off" property in the cube/sphere
cube_visible   = cube_group.click["on_off"]
sphere_visible = sphere_group.click["on_off"]

# calls the function into the group object with the visibility flag
change_visibility(cube_group.objects, cube_visible)
change_visibility(sphere_group.objects, sphere_visible)
