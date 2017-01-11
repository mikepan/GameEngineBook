# #############################
# Video Texture Render To Texture Demo
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
from bge import texture as VT

def newScene(cont):
    """Store the new scene and the camera to use with ImageRender"""
    G.new_scene = G.getCurrentScene()

    # this is not the 'active' camera to avoid
    # an extra render that we don't really need
    G.camera = G.new_scene.objects['Camera']

def createTexture(cont):
    """Create a new Dynamic Texture"""
    obj = cont.owner

    # get the reference pointer (ID) of the texture
    ID = VT.materialID(obj, 'IMoriginal.png')

    # create a texture object 
    texture = VT.Texture(obj, ID)

    # create a new source
    url = G.expandPath("//media/newtexture.jpg")
    new_source = VT.ImageRender(G.new_scene, G.camera)
    new_source.background = (180, 90, 144, 255)

    # the texture has to be stored in a permanent Python object
    G.texture = texture

    # update/replace the texture
    texture.source = new_source
    texture.refresh(False)

def update(cont):
    """update the texture with the 'new scene' every frame"""
    if hasattr(G, 'texture'):
        G.texture.refresh(False)

def removeTexture(cont):
    """
    Delete the Dynamic Texture, reversing
    back the final to its original state."""
    try:
        del G.texture
    except:
        pass
