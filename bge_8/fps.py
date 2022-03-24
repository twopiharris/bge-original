# fps.py
# -----------------------------------------------------------------------------
# Add this script to a camera
# with some other 'body' object as the parent
# Add an always sensor with pulse trigger on
# and a mouse sensor named "Mouse" (default name for a mouse sensor)

# mouse look adapted and commented by Andy Harris 2015
# keys by Andy Harris, 2016

#imports
import bge
from bge import render as r
import math


def mouse():
    # mouselook.py
    # adapted from
    # http://www.cgmasters.net/free-tutorials/fps-mouselook-script-plus-real-text/

    # get access to the bge compnents we'll need
    cont = bge.logic.getCurrentController()
    own = cont.owner
    parent = own.parent

    mouse = cont.sensors["Mouse"]
    # set speed for camera movement
    # larger # = more sensitive
    sensitivity = 0.05

    # set camera rotation limits
    high_limit = 180
    low_limit = 60

    #original script used w and h, and swapped them!

    # determine center of window
    cy = r.getWindowHeight()//2  
    cx = r.getWindowWidth()//2   

    # calculate dx and dy based on position
    # dx and dy are actually distance from center
    dx = (cx - mouse.position[0])*sensitivity
    dy = (cy - mouse.position[1])*sensitivity

    # reset mouse position so we'll get a RELATIVE position
    # this keeps mouse from leaving camera view and breaking

    r.setMousePosition(cx, cy)
    #convert rotation from matrix to euler form for ease of use
    rot = own.localOrientation.to_euler()
    # calculate new pitch (rotation around local X)
    pitch = abs(math.degrees(rot[0]))
    if high_limit > (pitch+dy) > low_limit:
        pitch += dy
    elif (pitch+dy) < low_limit:
        pitch = low_limit
    elif (pitch+dy) > high_limit:
        pitch = high_limit
    rot[0] = math.radians(pitch)
    # convert back to rotation matrix
    own.localOrientation = rot.to_matrix()

    # calculate new yaw (rotation around local Z) - apply yaw to PARENT
    parentRot = parent.localOrientation.to_euler()
    yaw = math.degrees(parentRot[2]) + dx
    parentRot[2] = math.radians(yaw)
    parent.localOrientation = parentRot.to_matrix()

def keys():
    #standard wasd keyboard
    
    # get access to the bge compnents we'll need
    cont = bge.logic.getCurrentController()
    own = cont.owner
    parent = own.parent
    
    #modify for different speeds
    SPEED = .1
    
    #get a name for the keyboard
    keyboard = bge.logic.keyboard
    
    #this is a constant meaning the event was just triggered
    # use for a single pulse like jump or gunfire
    JUST_ACTIVATED = bge.logic.KX_INPUT_JUST_ACTIVATED

    #ACTIVE is more helpful most of the time for motion
    # key is currently being pressed - continuous action 
    IS_ACTIVE = bge.logic.KX_INPUT_ACTIVE

    #standard WASD
    #add more keyboard input as needed for jumping, weapons, whatever
    if keyboard.events[bge.events.WKEY] == IS_ACTIVE:
        parent.applyMovement([0, SPEED, 0], True)
    if keyboard.events[bge.events.SKEY] == IS_ACTIVE:
        parent.applyMovement([0, -SPEED, 0], True)
    if keyboard.events[bge.events.AKEY] == IS_ACTIVE:
        parent.applyMovement([-SPEED, 0, 0], True)
    if keyboard.events[bge.events.DKEY] == IS_ACTIVE:
        parent.applyMovement([SPEED, 0, 0], True)

# run the two event handlers every frame
mouse()
keys()