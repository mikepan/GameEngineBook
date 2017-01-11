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

from bge import logic
import bgl
import math

def line_width():
    width = abs(math.sin(logic.timer["timer"]) * 11.0)
    bgl.glLineWidth(width)

scene = logic.getCurrentScene()

logic.timer = scene.objects["Cube"]

if line_width not in scene.pre_draw:
    scene.pre_draw.append(line_width)
