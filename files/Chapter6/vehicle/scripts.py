# #############################
# Vehicle Physics Demo
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

## First, we import all the python module
from bge import constraints
from bge import logic
from bge import events
from bge import render

import math

## Set specific vehicle characteristics ##
wheelRadius = 0.5
wheelBaseWide = 1.0
wheelFrontOffset = 0.7
wheelBackOffset = -1.8
AttachHeightLocal = 0.2
suspensionLength = 0.8
influence = 0.02
stiffness = 20.0
damping = 2.0
compression = 4.0
friction = 10.0
Stability = 0.05

## This is called from the car object
## is run once at the start of the game
def carInit():

	## setup aliases for Blender API access ##
	cont = logic.getCurrentController()
	logic.scene = logic.getCurrentScene()
	logic.car  = cont.owner

	## setup general vehicle characteristics ##
	wheelAttachDirLocal = [0,0,-1]
	wheelAxleLocal = [-1,0,0]

	## setup vehicle physics ##
	vehicle = constraints.createConstraint(logic.car.getPhysicsId(),0,11)
	logic.car["cid"] = vehicle.getConstraintId()
	vehicle = constraints.getVehicleConstraint(logic.car["cid"])

	## initialize temporary variables ##
	logic.car["dS"] = 0.0

	## attached wheel based on actuator name ##
	wheel0 = logic.scene.objects["Wheel0"]
	wheelAttachPosLocal = [wheelBaseWide ,wheelFrontOffset, AttachHeightLocal]
	vehicle.addWheel(wheel0,wheelAttachPosLocal,wheelAttachDirLocal,wheelAxleLocal,suspensionLength,wheelRadius,1)

	wheel1 = logic.scene.objects["Wheel1"]
	wheelAttachPosLocal = [-wheelBaseWide ,wheelFrontOffset, AttachHeightLocal]
	vehicle.addWheel(wheel1,wheelAttachPosLocal,wheelAttachDirLocal,wheelAxleLocal,suspensionLength,wheelRadius,1)

	wheel2 = logic.scene.objects["Wheel2"]
	wheelAttachPosLocal = [wheelBaseWide ,wheelBackOffset, AttachHeightLocal]
	vehicle.addWheel(wheel2,wheelAttachPosLocal,wheelAttachDirLocal,wheelAxleLocal,suspensionLength,wheelRadius,0)

	wheel3 = logic.scene.objects["Wheel3"]
	wheelAttachPosLocal = [-wheelBaseWide ,wheelBackOffset, AttachHeightLocal]
	vehicle.addWheel(wheel3,wheelAttachPosLocal,wheelAttachDirLocal,wheelAxleLocal,suspensionLength,wheelRadius,0)

	## set vehicle roll tendency ##
	vehicle.setRollInfluence(influence,0)
	vehicle.setRollInfluence(influence,1)
	vehicle.setRollInfluence(influence,2)
	vehicle.setRollInfluence(influence,3)

	## set vehicle suspension hardness ##
	vehicle.setSuspensionStiffness(stiffness,0)
	vehicle.setSuspensionStiffness(stiffness,1)
	vehicle.setSuspensionStiffness(stiffness,2)
	vehicle.setSuspensionStiffness(stiffness,3)

	## set vehicle suspension dampness ##
	vehicle.setSuspensionDamping(damping,0)
	vehicle.setSuspensionDamping(damping,1)
	vehicle.setSuspensionDamping(damping,2)
	vehicle.setSuspensionDamping(damping,3)

	## set vehicle suspension compression ratio ##
	vehicle.setSuspensionCompression(compression,0)
	vehicle.setSuspensionCompression(compression,1)
	vehicle.setSuspensionCompression(compression,2)
	vehicle.setSuspensionCompression(compression,3)

	## set vehicle tire friction ##
	vehicle.setTyreFriction(friction,0)
	vehicle.setTyreFriction(friction,1)
	vehicle.setTyreFriction(friction,2)
	vehicle.setTyreFriction(friction,3)


## called from main car object
## is run once at the start of the game
def carHandler():
	vehicle = constraints.getVehicleConstraint(logic.car["cid"])

	## calculate speed by using the back wheel rotation speed ##
	S = vehicle.getWheelRotation(2)+vehicle.getWheelRotation(3)
	logic.car["speed"] = (S - logic.car["dS"])*10.0

	## apply engine force ##
	vehicle.applyEngineForce(logic.car["force"],0)
	vehicle.applyEngineForce(logic.car["force"],1)
	vehicle.applyEngineForce(logic.car["force"],2)
	vehicle.applyEngineForce(logic.car["force"],3)

	## calculate steering with varying sensitivity ##
	if math.fabs(logic.car["speed"])<15.0: s = 2.0
	elif math.fabs(logic.car["speed"])<28.0: s=1.5
	elif math.fabs(logic.car["speed"])<40.0: s=1.0
	else: s=0.5

	## steer front wheels
	vehicle.setSteeringValue(logic.car["steer"]*s,0)
	vehicle.setSteeringValue(logic.car["steer"]*s,1)

	## slowly ease off gas and center steering ##
	logic.car["steer"] *= 0.6
	logic.car["force"] *= 0.9

	## align car to Z axis to prevent flipping ##
	logic.car.alignAxisToVect([0.0,0.0,1.0], 2, Stability)
	
	## store old values ##
	logic.car["dS"] = S



## called from main car object
def keyHandler():
	cont = logic.getCurrentController()
	keys = cont.sensors["key"].events
	for key in keys:
		## up arrow
		if   key[0] == events.UPARROWKEY:
			logic.car["force"]  = -15.0
		## down arrow
		elif key[0] == events.DOWNARROWKEY:
			logic.car["force"]  = 10.0
		## right arrow
		elif key[0] == events.RIGHTARROWKEY:
			logic.car["steer"] -= 0.05
		## left arrow
		elif key[0] == events.LEFTARROWKEY:
			logic.car["steer"] += 0.05
		## Reverse
		elif key[0] == events.RKEY:
			if key[1] == 1:
				# re-orient car
				if logic.car["jump"] > 2.0:
					pos = logic.car.worldPosition
					logic.car.position = (pos[0], pos[1], pos[2]+3.0)
					logic.car.alignAxisToVect([0.0,0.0,1.0], 2, 1.0)
					logic.car.setLinearVelocity([0.0,0.0,0.0],1)
					logic.car.setAngularVelocity([0.0,0.0,0.0],1)
					logic.car["jump"] = 0
		## Spacebar
		elif key[0] == events.SPACEKEY:
			# hackish Brake
			if logic.car["speed"] > 2.0:
				logic.car["force"]  = 15.0
			if logic.car["speed"] < -2.0:
				logic.car["force"]  = -15.0


## called from shadow lamp
def shadow():
	cont = logic.getCurrentController()
	ownpos = [-5.0,0.0,8.0]
	pos = logic.car.worldPosition
	cont.owner.worldPosition = [pos[0]+ownpos[0], pos[1]+ownpos[1], pos[2]+ownpos[2]]

