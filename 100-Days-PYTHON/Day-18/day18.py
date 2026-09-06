print("==============================================================================================")
print("---------------------------------NUMBER DICTIONARY--------------------------------------------")
print("==============================================================================================")
numbers=[1,2,3,4,5,6,7,8,9,10]
squares={x:x*x for x in numbers}
print("Number and it's Square:",squares)
print("----------------------------------------------------------------------------------------------")

print("==============================================================================================")
print("-------------------------------STUDENT RESULTS------------------------------------------------")
print("==============================================================================================")
marks={"Bhoomi":92,
       "Akshu":76,
       "Sacchi":84,
       "Abhii":49,
       "Suma":35}
a={name:mark 
   for name,mark in marks.items()
   if mark>=40}
print("Dictionary with students scored above 40:",a)
b={name:"Pass" if mark>=40 else "Fail"
   for name,mark in marks.items()}
print("Result of every Students",b)
print("----------------------------------------------------------------------------------------")

print("================================================================================================")
print("-----------------------------------SENSOR STATUS------------------------------------------------")
print("================================================================================================")
sensor_values={"Ultrasonic":15,
               "IR":0,
               "Temperature":35,
               "LDR":1}
activity={name:"Inactive" if value==0 else "Active"
          for name,value in sensor_values.items()}
print("Activity Status:",activity)
print("-----------------------------------------------------------------------------------------")

print("================================================================================================")
print("-----------------------------------BONUS CHALLENGE----------------------------------------------")
print("-----------------------------SMART ROBOT DATA PROCESSOR-----------------------------------------")
print("================================================================================================")
robots={
    "LineBot":80,
    "ObstacleBot":120,
    "FollowBot":100,
    "MazeBot":60
}
speed={name:speed
       for name,speed in robots.items()
       if speed>=100}
print("Dictionary with Robot's speed>=100",speed)
category={name:"Fast" if speed>=100 else "slow"
          for name,speed in robots.items()}
print("Speed Category to which robot belong:",category)
new_robots={name:int(speed+((speed*20)/100))
                 for name,speed in robots.items()
                }
print("Dictionary with increased speed by 20%",new_robots)
print("------------------------------------------------------------------------------------------")
print("------------------------End of Day-18 Python Challenges-----------------------------------")
print("------------------------------------------------------------------------------------------")
