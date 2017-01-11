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
from bge import logic
from bge import events

cont = logic.getCurrentController()
owner = cont.owner
sensor = cont.sensors["s_keyboard"]

active_events = logic.keyboard.active_events
if len(active_events):

    text = ""
    # get only the first pressed key
    for key,status in active_events.items():

        text += "the key number is: %d\n" % key
        text += "the key value is: %s\n" % events.EventToString(key)
        text += "the character is: %s\n" % events.EventToCharacter(key, 0) # (key_code, captalize_flag)

        # optionally you can see the key status too if you want (just activated, 
        text += "the status is: %d\n" % status

        # press space to reset the initial text
        if key == events.SPACEKEY:
            text = "Please, press any key."
            break

    owner["Text"] = text
