# #############################
# GameKeys Script Demo
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
from bge import events as GK

cont = G.getCurrentController()
owner = cont.owner
sensor = cont.sensors["s_keyboard"]

if sensor.positive:

    keylist = sensor.events

    # get only the first pressed key
    event = keylist[0]

    pressed_key = event[0]
    status = event[1]

    text = "the key number is: %d\n" % pressed_key
    text += "the key value is: %s\n" % GK.EventToString(pressed_key)
    text += "the character is: %s\n" % GK.EventToCharacter(pressed_key, 0) # (key_code, captalize_flag)

    # optionally you can see the key status too if you want (just activated, 
    # text += "the status is: %d\n" % status

    # press space to reset the initial text
    if pressed_key == GK.SPACEKEY:
        text = "Please, press any key."

    owner["Text"] = text
