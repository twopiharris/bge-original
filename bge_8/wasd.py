#WASD.py

#attach to any object to give standard WASD FPS controls

#paste this code into blender text editor and modify as needed

#should be attached to an aways sensor (pulse mode)
#no keyboard sensor is needed

import bge

def main():

    #modify for different speeds
    SPEED = .1
    
    #get a name for the keyboard
    keyboard = bge.logic.keyboard
    
    cont = bge.logic.getCurrentController()
    own = cont.owner

    #this is a constant meaning the event was just triggered
    # use for a single pulse
    JUST_ACTIVATED = bge.logic.KX_INPUT_JUST_ACTIVATED

    #ACTIVE is more helpful most of the time
    # key is currently being pressed - continuous action 
    IS_ACTIVE = bge.logic.KX_INPUT_ACTIVE

    #look up keyboard constants in bge.events documentation
    #for comparison purposes, W and S use ACTIVE,
    # A and D use JUST_ACTIVATED
    if keyboard.events[bge.events.WKEY] == IS_ACTIVE:
        own.applyMovement([0, SPEED, 0], True)
    if keyboard.events[bge.events.SKEY] == IS_ACTIVE:
        own.applyMovement([0, -SPEED, 0], True)
    if keyboard.events[bge.events.AKEY] == IS_ACTIVE:
        own.applyMovement([-SPEED, 0, 0], True)
    if keyboard.events[bge.events.DKEY] == IS_ACTIVE:
        own.applyMovement([SPEED, 0, 0], True)
 
main()