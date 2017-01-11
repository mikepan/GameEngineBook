# #############################
# Video Texture Replacement Demo
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
from bge import texture

def createTexture(cont):
    """Create a new Dynamic Texture"""
    object = cont.owner

    # get the reference pointer (ID) of the texture
    ID = texture.materialID(object, 'IMoriginal.png')

    # create a texture object 
    dynamic_texture = texture.Texture(object, ID)

    # create a new source
    url = logic.expandPath("//media/newtexture.jpg")
    new_source = texture.ImageFFmpeg(url)

    # the texture has to be stored in a permanent Python object
    logic.dynamic_texture = dynamic_texture

    # update/replace the texture
    dynamic_texture.source = new_source
    dynamic_texture.refresh(False)

def removeTexture(cont):
    """Delete the Dynamic Texture, reversing back the final to its original state."""
    try:
        del logic.dynamic_texture
    except:
        pass
