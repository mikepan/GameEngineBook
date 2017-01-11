# #############################
# Simple Sensor, Controller and Actuator Demo
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
from bge import logic

cont = logic.getCurrentController()
owner = cont.owner

scene = logic.getCurrentScene()
objects = scene.objects
text_obj = objects["Text"]

sens = cont.sensors['my_sensor']
act = cont.actuators['my_actuator']

if sens.positive:
    cont.activate(act)
    text_obj.text = "CADABRA"
else:
    cont.deactivate(act)
    text_obj.text = "ABRA"

