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
from bge import render as R

# showing the mouse cursor
R.showMouse(True)

# storing the current scene in a variable
scene = G.getCurrentScene()

# define a class to store all group elements and the click object
class Group():
    def __init__(self, name):
        self.name = name
        self.click = None
        self.objects = []

# create new element groups
cube_group   = Group("cubes")
sphere_group = Group("sphere")

# add all objects with an "ui" property to the created element
for obj in scene.objects:
    if "cube" in obj:
        cube_group.objects.append(obj)
    elif "sphere" in obj:
        sphere_group.objects.append(obj)
    elif "click" in obj:
        exec("%s_group.click = obj" % (obj["click"]))
        # note exec here is replacing:
        # if obj["click"] == "cube":
        #     cube_group.click = obj
        # elif obj["click"] == "sphere":
        #     sphere_group.click = obj

G.groups = {"cube":cube_group, "sphere":sphere_group}
