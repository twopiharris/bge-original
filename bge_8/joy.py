""" Joystick controller - Blender 2.7
    Expects an always sensor with pulse set
    and a motion controller called "Motion"
    Default version moves object with left 
    stick, rotates with right stick.
    Adjust TRANS_SENS to change translation
    sensitivity, and ROT_SENS to change rotation
    SENSITIVITY
    
    Andy Harris - 2/16/15
"""

import bge

def main():

    cont = bge.logic.getCurrentController()
    own = cont.owner
    motion = cont.actuators["Motion"]
    
    # sensitivity constants for translation
    # and rotation. Adjust for feel
    TRANS_SENS = 1
    ROT_SENS = .1
    
    joy = bge.logic.joysticks[0]
    leftX = joy.axisValues[0]
    leftY = joy.axisValues[1]
    rightX = joy.axisValues[2]
    rightY = joy.axisValues[3]
    buttons = joy.activeButtons

    """ DEBUGGING INFO
    print("left: {} {}".format(leftX, leftY))
    print("right: {} {}".format(rightX, rightY))
    print("buttons: {}".format(buttons))
    print()
    """

    #set up a center threshold
    if leftX < .05:
      if leftX > -.05:
          leftX = 0
          
    if leftY < .05:
        if leftY > -.05:
            leftY = 0
    
    if rightX < .05:
      if rightX > -.05:
          rightX = 0
          
    if rightY < .05:
        if rightY > -.05:
            rightY = 0
    
    #invert leftY
    leftY *= -1

    #apply translation sensitivity to left stick
    leftX *= TRANS_SENS
    leftY *= TRANS_SENS

    #apply rotation sens to right stick
    rightX *= ROT_SENS
    rightY *= ROT_SENS
    
    #set motion actuator to joy inputs    
    motion.dLoc = [leftX, leftY, 0]
    motion.dRot = [rightY, rightX, 0]
      
    #go with global rotations and locations
    motion.useLocalDLoc = False
    motion.useLocalDRot = False

    #read button zero
    if 0 in buttons:
        print("button zero pressed")
        own["counter"] += 1
    
    #set actuator to true
    cont.activate(motion)
         



main()
