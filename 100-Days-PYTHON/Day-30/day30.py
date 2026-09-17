#Challenge-1
print("===========================================================================")
print("---------------------------- Traffic Light --------------------------------")
print("===========================================================================")
from enum import Enum
class TrafficLight(Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3
light=TrafficLight.RED
if light==TrafficLight.RED:
    print("Stop the Vehicle")
print("Light Colour:",TrafficLight.RED.name)
print("Light Value:",TrafficLight.RED.value)
print("--------------------------------------------------------------------------")

#Challenge-2
print("===========================================================================")
print("---------------------------- Day of Week ----------------------------------")
print("===========================================================================")
from enum import Enum,auto
class Day(Enum):
    MONDAY = auto()
    TUESDAY = auto()
    WEDNESDAY = auto()
    THURSDAY = auto()
    FRIDAY = auto()
    SATURDAY = auto()
    SUNDAY = auto()
for day in Day:
    print(day.name,day.value)
print("--------------------------------------------------------------------------")

#Challenge-3
print("===========================================================================")
print("---------------------------- Robot Status ---------------------------------")
print("===========================================================================")
class RobotState:
    IDLE=1
    MOVING=2
    STOPPED=3
    ERROR=4
state=RobotState.MOVING
if state==RobotState.MOVING:
    print("Robot is moving")
print("--------------------------------------------------------------------------")

#Challenge-4
print("===========================================================================")
print("---------------------------- Sensor Status --------------------------------")
print("===========================================================================")
class SensorStatus(Enum):
    ACTIVE =1
    INACTIVE=2
    ERROR=3
status=SensorStatus.ACTIVE
if status==SensorStatus.ACTIVE:
    print("Sensor is Active")
elif status==SensorStatus.INACTIVE:
    print("Sensor is Inactive") 
else:
    print("Sensor is in Error State")
print("--------------------------------------------------------------------------")

#Bonus Challenge
print("===========================================================================")
print("----------------------------- Bonus Challenge -----------------------------")
print("----------------------------- Robot Direction -----------------------------")
print("===========================================================================")
class Direction(Enum):
    FORWARD=1
    BACKWARD=2
    LEFT=3
    RIGHT=4
    STOP=5
dir=Direction.BACKWARD
if dir==Direction.FORWARD:
    print("Robot is moving Forward")
elif dir==Direction.BACKWARD:
    print("Robot is moving Backward")
elif dir==Direction.LEFT:
    print("Robot is moving Left")
elif dir==Direction.RIGHT:
    print("Robot is moving Right")
else:
    print("Robot is Stopped")
print("--------------------------------------------------------------------------")
print("---------------------- End of Day-30 Challenges --------------------------")
print("--------------------------------------------------------------------------")