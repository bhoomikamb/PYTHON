#Challenge-01
print("============================================================================")
print("------------------------- Basic logger -------------------------------------")
print("============================================================================")
import logging #imports logging
logging.basicConfig(level=logging.INFO) #configures logging at info level
logging.info("Program Started")
logging.info("User entered data")
logging.info("Program finished")
print("---------------------------------------------------------------------------")

#Challenge-02
print("============================================================================")
print("------------------------- Different Log Levels -----------------------------")
print("============================================================================")
battery=25   #Creating variable
logging.info("Robot is running") #INFO
logging.warning("Battery is getting low") #WARNING
logging.error("Motor error") #ERROR
print("----------------------------------------------------------------------------")

#Chaleenge-03
print("============================================================================")
print("------------------------- Save Robot Logs ----------------------------------")
print("============================================================================")
logging.basicConfig(filename="100-Days-Python/Day-33/robot.log",
                    level=logging.INFO,
                    force=True)
logging.info("Robot Started!")
logging.info("Sensor Checking..")
logging.warning("Onstacle detected!")
logging.info("Robot Stopped!!")
print("----------------------------------------------------------------------------")

#Challenge-04
print("============================================================================")
print("---------------------------- Sensor logger ---------------------------------")
print("============================================================================")
sensor_reading=[15,25,10,50,8]
for reading in sensor_reading:
    if reading<20:
        logging.info(f"Safe Distance:{reading}")
    else:
        logging.warning(f"Obstacle nearby:{reading}")
logging.info("Robot stopped!")
print("---------------------------------------------------------------------------")

#Bonus-Challenge
print("============================================================================")
print("------------------------- Robot Event logger -------------------------------")
print("============================================================================")
logging.basicConfig(filename="100-Days-Python/Day-33/robot_events.log",
                    level=logging.INFO,
                    force=True) #saving everything to robot_evnts.log file
logging.info("Robot initialised")
logging.info("Motor started")
logging.info("Sensor activated")
logging.warning("Obstacle detected!")
logging.info("Robot stopped!!")
logging.info("Robot shut down")
print("---------------------------------------------------------------------------")
print("--------------------- End of Day-33 Challenges ----------------------------")
print("---------------------------------------------------------------------------")