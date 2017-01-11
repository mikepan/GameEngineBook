# ###############################################################################
# Navigation System - Example Script
#
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

# ###############################################################################
# Import all the needed python modules
# ###############################################################################
from bge import logic as G
from bge import render as R
from bge import events as GK
import mathutils as M
import math as m

# ###############################################################################
# Script to initialize the world.  This script is run once on startup
# ###############################################################################

def init_world():
    G.scenes = {"main":G.getCurrentScene()}
    objects = G.scenes["main"].objects

    # ############################################################################
    #    Initializing the Camera elements
    # ############################################################################
    # Setting the cursor
    R.showMouse(False)
    set_mouse_position()

    G.cameras = {}
    # orbit camera
    camera = objects["CAM_Orbit"]
    pivot = objects["ORB_PIVOT"]
    G.cameras["ORB"] = [camera, {"orientation":pivot.worldOrientation}, pivot]
    # fly/walk camera
    camera = objects["CAM_Move"]
    pivot = objects["MOVE_PIVOT"]

    G.cameras["MOVE"] = [camera, {"orientation":pivot.worldOrientation, "position":pivot.worldPosition}, pivot]

    # ############################################################################
    #    Camera Orbit
    # ############################################################################

    # angle restriction in degrees
    left    = -220.0
    right    = 220.0
    top        = 70.0
    bottom    = 10.0

    # convert all of them to radians
    left = m.radians(left)
    right = m.radians(right)
    top = m.radians(top)
    bottom = m.radians(bottom)

    # store them globally
    G.orb_limits = {"left":left, "right":right, "top":top, "bottom":bottom}

    # ############################################################################
    #    Mouse Look
    # ############################################################################

    # angle restriction
    top        = 45.0
    bottom= -15.0

    # convert them to radians
    top        = m.radians(top)
    bottom= m.radians(bottom)

    G.look_limits = {"top":top, "bottom":bottom}
    G.look_SENS = 1.5

    # ############################################################################
    #    Different Cameras
    # ############################################################################

    # list the cameras with their name in the 3DWorld CAM_name e.g. CAM_front will be front in the list
    available_cameras = ["front", "back", "side", "top"]
    G.views = {}
    for i in available_cameras:
        G.views[i] = objects["CAM_%s" % (i)]

    # ############################################################################
    #    Variables that change during the game
    # ############################################################################
    G.cameras["CAM"] = "ORB" # the current camera
    G.cameras["OLD_CAM"] = G.cameras["CAM"]
    G.walk_fly = "walk"
    G.nav_mode = "orbit"

# ###############################################################################
#     Keyboard Management
# ###############################################################################

def keyboard(cont):
    owner = cont.owner
    sensor = cont.sensors["s_keyboard"]

    if sensor.positive:
        keylist = sensor.events

        for key in keylist:
            value = key[0]

            if G.cameras["CAM"] == "MOVE":
                if value == GK.WKEY:
                    # Move Forward
                    move_camera(0)
                elif value == GK.SKEY:
                    # Move Backward
                    move_camera(1)
                elif value == GK.AKEY:
                    # Move Left
                    move_camera(2)
                elif value == GK.DKEY:
                    # Move Right
                    move_camera(3)

            # CAMERA SWITCHING
            if value == GK.ONEKEY:
                change_view("orbit", "orbit")
            elif value == GK.TWOKEY:
                change_view("front")
            elif value == GK.THREEKEY:
                change_view("top", "fly")
            elif value == GK.FOURKEY:
                change_view("side")
            elif value == GK.FIVEKEY:
                change_view("back", "fly")

        if G.nav_mode == "walk" and G.walk_fly == "walk":
            stick_to_ground()

# ###############################################################################
#     1/2 - Changing Cameras.
# ###############################################################################

def change_view(view, mode="walk"):
    cont = G.getCurrentController()
    act_camera = cont.actuators["a_changecam"]

    # set the orientation and position of selected view
    if mode == "orbit":
        dict = G.cameras["ORB"]

        pivot = dict[2]
        pivot.orientation = dict[1]["orientation"]

        G.nav_mode = mode # orbit
        G.cameras["CAM"] = "ORB"

    else:
        # mode == walk/fly
        dict = G.cameras["MOVE"]
        camera = dict[0]
        pivot = dict[2]

        pivot.worldPosition = G.views[view].position
        pivot.worldOrientation = G.views[view].orientation
        camera.localOrientation = [[1,0,0],[0,1,0],[0,0,1]]

        G.nav_mode = mode
        G.walk_fly = mode
        G.cameras["CAM"] = "MOVE"

        if G.walk_fly == "walk":
            fly_to_walk()

    # change the camera
    act_camera.camera = dict[0]
    cont.activate(act_camera)

    set_mouse_position()

# ###############################################################################
#     2 / 2 - Changing Cameras.
# ###############################################################################
""" we want the pivot to have a vertical rotation of 90deg. and the camera to rotate """
def fly_to_walk():
    camera    = G.cameras["MOVE"][0]
    pivot    = G.cameras["MOVE"][2]

    view_orientation = camera.worldOrientation
    euler = view_orientation.to_euler()
    angle = euler[0] - (m.pi/2)

    pivot.applyRotation([-angle,0,0],1)
    camera.applyRotation([angle,0,0],1)

def set_mouse_position():
    #screen_width  =R.getWindowWidth()
    #screen_height =R.getWindowHeight()

    #R.setMousePosition(screen_width//2, screen_height//2)
    G.mouse.position = 0.5,0.5

# ###############################################################################
#     Mouse Movement
# ###############################################################################
def mouse_move(cont):
    owner = cont.owner
    sensor = cont.sensors["s_movement"]

    if sensor.positive:
        if G.cameras["CAM"] == "ORB":
            orbit_camera(sensor)
        else:
            look_camera(sensor)

# ###############################################################################
#     Orbit Camera
# ###############################################################################
def orbit_camera(sensor):
    # ############################################################################
    #    Calculating Clamp and Mouse coordinate
    # ############################################################################

    screen_width  =R.getWindowWidth()
    screen_height =R.getWindowHeight()

    win_x, win_y = sensor.position

    # G.orb_clamp is in radians
    orb_limits        = G.orb_limits
    left_limit        = orb_limits["left"]
    right_limit        = orb_limits["right"]
    bottom_limit    = orb_limits["bottom"]
    top_limit        = orb_limits["top"]

    # normalizying x to run from left to right limits
    x = win_x / screen_width
    x = left_limit + (x * (right_limit - left_limit))

    # normalize y to run from top to bottom limits
    y = win_y / screen_height
    y = top_limit + (y * (bottom_limit - top_limit))

    # flip the vertical movement
    y = m.pi/2 - y

    # ############################################################################
    #    Calculate the new orientation matrix
    # ############################################################################
    mat_ori = G.cameras["ORB"][1]["orientation"]

    mat_x = M.Matrix.Rotation(x, 3, 'Z')
    mat_y = M.Matrix.Rotation(y, 3, 'X')

    ori = mat_x * mat_y

    pivot = G.cameras["ORB"][2]
    pivot.orientation = ori


# ###############################################################################
#     Mouse Look Camera
# ###############################################################################
def look_camera(sensor):

    # ############################################################################
    #    Calculating Clamp and Mouse coordinate
    # ############################################################################

    screen_width  =R.getWindowWidth()
    screen_height =R.getWindowHeight()

    # make sure the screen dimencions are even
    screen_width -= screen_width %2
    screen_height -= screen_height %2

    win_x, win_y = sensor.position

    camera_dict = G.cameras["MOVE"]

    top_limit    = G.look_limits["top"]
    bottom_limit= G.look_limits["bottom"]

    SENS = G.look_SENS

    # normalize to run from -0.5 to 0.5
    x = (win_x / screen_width) - 0.5
    y = (win_y / screen_height) - 0.5

    # change sensibility
    x *= SENS
    y *= -SENS

    camera    = camera_dict[0]
    pivot    = camera_dict[2]

    # limit top - bottom angles
    if G.walk_fly == "walk":
        angle = camera.localOrientation[2][1]
        angle = m.asin(angle)

        # if it's too high go down. if it's too low go high
        if (angle + y) > top_limit: y = top_limit - angle
        elif (angle + y) < bottom_limit: y = bottom_limit - angle

    # ############################################################################
    #    Rotate the View
    # ############################################################################
    if G.walk_fly == "walk":
        # Look Up rotation
        camera.applyRotation([y,0,0], 1)

        # Look Side rotation
        pivot.applyRotation([0, -x, 0], 1)

    # the order here matter a lot:
    else: # G.walk_fly == "fly"
        # Look Side rotation
        pivot.applyRotation([0, 0, -x], 0)

        # Look Up rotation
        pivot.applyRotation([y, 0, 0], 1)

    # return mouse pointer to the origin (X and Y wise)
    set_mouse_position()

# ###############################################################################
#     Move the Camera
# ###############################################################################

def move_camera(direction):

    if not G.cameras["CAM"] == "MOVE": return
    MOVE = 0.25 #speed

    if direction == 0: # Forward
        vector = M.Vector([0, 0, -MOVE])

    elif direction == 1: # Backward
        vector = M.Vector([0, 0, MOVE])

    elif direction == 2: # Left
        vector = M.Vector([-MOVE,0,0])

    elif direction == 3: # Right
        vector = M.Vector([MOVE, 0, 0])

    # if there is any obstacle reset the vector
    vector = collision_check(vector, direction)

    # now that we calculated the vector we can move the pivot
    pivot = G.cameras["MOVE"][2]
    pivot.applyMovement(vector, True)

# ###############################################################################
#     Collision 1/2 - ground check
# ###############################################################################

def stick_to_ground():
    CAMERA_HEIGHT = 1.68
    property = "ground"

    DIST = 50.0
    pivot = G.cameras["MOVE"][2]
    position = pivot.position
    to_pos = position.copy()
    to_pos[2] -= DIST

    # rayCast(objto, objfrom, dist, prop, face, xray, poly)
    #@ (object,hitpoint,hitnormal)
    ray = pivot.rayCast(to_pos, pivot, DIST, property, 0, 1, 0)
    if ray[0]:
        distance = position[2] - ray[1][2]
        vertical_off = distance - CAMERA_HEIGHT
        pivot.applyMovement([0,0,-vertical_off], False)

    else:
        # try to cast a ray upward .:. YOU WILL GET STUCK IF YOU ARE IN THE PLANE
        to_pos[2] += 2 * DIST
        ray = pivot.rayCast(to_pos, pivot, DIST, property, 0, 1, 0)
        if ray[0]:
            distance = ray[1][2] - position[2]
            vertical_off = CAMERA_HEIGHT + distance
            pivot.applyMovement([0,0, vertical_off], False)
        else:
            return

# ###############################################################################
#     Collision 2/2 - move check
# ###############################################################################
def collision_check(vector, direction):

    DISTANCE = 0.5
    RADAR_ANGLE = m.radians(30.0)
    RAYS = 5
    property = "ground"

    camera    = G.cameras["MOVE"][0]
    pivot    = G.cameras["MOVE"][2]

    # walk mode - ray is forward
    if G.nav_mode == "walk":
        from_obj = pivot
    else:
        from_obj = camera

    # Vector assignment:
    if direction == 0: # Forward
        dir_vector = from_obj.getAxisVect([0,0,-1])
    elif direction == 1: # Backward
        dir_vector = from_obj.getAxisVect([0,0,1])
    elif direction == 2: # Left
        dir_vector = from_obj.getAxisVect([-1,0,0])
    elif direction == 3: # Right
        dir_vector = from_obj.getAxisVect([1,0,0])
    else:
        return

    from_pos = from_obj.position

    # cast multiple RAYS covering the RADAR_ANGLE with DISTANCE 
    for i in range(RAYS):
        x_off = -(RADAR_ANGLE/2) + (RADAR_ANGLE * (i / (RAYS-1)))

        # to_vec = pivot.getAxisVect([0,m.sin(i),-m.cos(i)])
        to_vec = dir_vector.copy()
        to_vec[0] += m.sin(i)
        to_vec[1] -= m.cos(i)

        to_vec = from_pos + to_vec
        ray = pivot.rayCast(to_vec, from_obj, DISTANCE)#, property)

        if ray[0]:
            # obstacle found, reset the direction vector
            vector = [0,0,0]
            return vector

    return vector
