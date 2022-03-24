#keyboard handling template
#modified from documentation
#Andy Harris

#paste this code into blender text editor and modify as needed

#should be attached to an always sensor (pulse mode)
#no keyboard sensor is needed

import bge

def main():

    #get a name for the keyboard
    keyboard = bge.logic.keyboard
    
    #other useful objects to have
    cont = bge.logic.getCurrentController()
    own = cont.owner

    #this is a constant meaning the event was just triggered
    # use for a single pulse
    JUST_ACTIVATED = bge.logic.KX_INPUT_JUST_ACTIVATED

    #ACTIVE is more helpful most of the time
    # key is currently being pressed - continuous action 
    IS_ACTIVE = bge.logic.KX_INPUT_ACTIVE

    #look up keyboard constants i+n bge.events documentation
    #for comparison purposes, W and S use ACTIVE,
    # A and D use JUST_ACTIVATED
    if keyboard.events[bge.events.WKEY] == IS_ACTIVE:
            print("Activate Forward!")
    if keyboard.events[bge.events.SKEY] == IS_ACTIVE:
            print("Activate Backward!")
    if keyboard.events[bge.events.AKEY] == JUST_ACTIVATED:
            print("Activate Left!")
    if keyboard.events[bge.events.DKEY] == JUST_ACTIVATED:
            print("Activate Right!")
            
main()