#########################################
#
#   Powertrain.py  Blender 2.6
#
#   tutorial can be found at
#
#   www.tutorialsforblender3d.com
#
#   Released under the Creative Commons Attribution 3.0 Unported License.   
#
#   If you use this code, please include this information header.
#
##########################################
# This script has been modified by "SuperGloop"
##########################################


import GameLogic
own = GameLogic.getCurrentController().owner

#The fastest the car can go (in BU)
maxSpeed = 50

#The farthest the wheels can turn
maxTurn = .75

#How quickly the wheels turn
tSpeed = 0.02

#how quickly the wheels return to normal position
reSpeed = 0.02

#The power going forward
power = 2000

#The power going in reverse
rPower = 500

#The brake, and EBrake forces
brakeForce = 40
EBrakeForce = 100



# Main Program
def main():
        
    # get the current controller
    controller = bge.logic.getCurrentController()
    
    # get vehicle constraint ID
    vehicleID = ConstraintID(controller)
    
    # brakes
    brakes = Brakes(vehicleID, controller)
        
    # gas & reverse
    Power( vehicleID, controller, brakes)
        
    # steering
    Steering(vehicleID, controller)
    

########################################################  Vehicle ID

# get vehicle constraint ID
def ConstraintID(controller):

    # get car the controller is attached to
    car = controller.owner
        
    # get saved vehicle Constraint ID
    vehicleID = car["vehicleID"]
    
    return vehicleID

########################################################  Brakes

def Brakes(vehicleID, controller):
    global brakeForce
    global EBrakeForce
    # set braking amount
    brakeAmount = brakeForce    # front and back brakes
    ebrakeAmount = EBrakeForce    # back brakes only  

    # get sensors
    reverse = controller.sensors["Reverse"]  # sensor named "Reverse"
    brake = controller.sensors["Brake"]      # sensor named "Brake
    emergency = controller.sensors["EBrake"]    # sensor named "EBrake"
    
    # emergency brakes    
    if emergency.positive == True:
        
        front_Brake = 0.0
        back_Brake = ebrakeAmount
        brakes = True
    
    # brake
    elif brake.positive == True and reverse.positive == False:
        
        front_Brake = brakeAmount
        back_Brake = brakeAmount
        brakes = True

    # no brakes
    else:
        
        front_Brake = 0.0
        back_Brake = 0.0
        brakes = False

    # brakes    
    vehicleID.applyBraking( front_Brake, 0)
    vehicleID.applyBraking( front_Brake, 1)
    vehicleID.applyBraking( back_Brake, 2)
    vehicleID.applyBraking( back_Brake, 3)

    return brakes

##########################################  Gas & Reverse 
    
# gas and reverse   
def Power( vehicleID, controller, brakes): 
    # set power amounts
    vely = own.getLinearVelocity(True)[1]
    drag = vely * 10
    global rPower
    global power
    reversePower = rPower
    gasPower = power
    own['speed'] = vely

    # get power sensors
    gas = controller.sensors["Gas"]          # sensor named "Gas"
    reverse = controller.sensors["Reverse"]  # sensor named "Reverse"
    
    # brakes
    if brakes == True:
        
        power = 0.0
                    
    # reverse
    elif reverse.positive == True:
        
        power = reversePower
    
    # gas pedal 
    elif gas.positive == True:
        power = -gasPower
    
    # no gas and no reverse
    else:
        
        power = 0.0

    # apply power
    vehicleID.applyEngineForce( power, 0)
    vehicleID.applyEngineForce( power, 1)
    vehicleID.applyEngineForce( power, 2)
    vehicleID.applyEngineForce( power, 3)                                      
        

##################################################  Steering 

def Steering( vehicleID, controller):
    vely = own.getLinearVelocity(True)[1]
    # set turn amount
    turn = 0.3
    

    # get steering sensors
    steerLeft = controller.sensors["Left"]    # sensor named "Left"
    steerRight = controller.sensors["Right"]    # sensor named "Right"
    turn = own['turn']  
    # turn left 
    if steerLeft.positive == True and turn < maxTurn:
        
        turn += tSpeed*2
        if turn > 0.01:
            turn -= reSpeed
    
    # turn right    
    elif steerRight.positive == True and turn > -maxTurn:
        
        turn -= tSpeed*2
        if turn < 0.01:
            turn += reSpeed
    
    # go straight   
    else:
        if turn < -0.01:
            turn += reSpeed
        elif turn > 0.01:
            turn -= reSpeed
    own['turn'] = turn
        
    # steer with front tires only
    vehicleID.setSteeringValue(turn,0)
    vehicleID.setSteeringValue(turn,1)
    grip = (maxSpeed - vely)
    vehicleID.setTyreFriction(grip + 1, 0)  # front driver's tire 
    vehicleID.setTyreFriction(grip + 1, 1)  # front passenger's tire 
    vehicleID.setTyreFriction(grip, 2)  # rear driver's tire
    vehicleID.setTyreFriction(grip, 3)  # rear passenger's tire

###############################################

#import bge
import bge

# run main program
main()
    