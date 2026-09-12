print("=======================================================")
print("------------------- Use @wraps ------------------------")
print("=======================================================")
from functools import wraps
def decorator(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
        return function(*args,**kwargs)
    return wrapper
@decorator
def calculate(a,b):
    return a+b
print("Function name:",calculate.__name__)
print("-------------------------------------------------------")

print("=======================================================")
print("-------------- Logging Decorator ----------------------")
print("=======================================================")
def logger(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
        print("Calling Function..")
        return function(*args,**kwargs)
    return wrapper
@logger
def add(a,b):
    return a+b
print("Addition on 2 inputs:",add(10,17))
print("-------------------------------------------------------")

print("=======================================================")
print("------------------- Result logger ---------------------")
print("=======================================================")
def decor(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
        print("Function Called!...")
        return function(*args,**kwargs)
    return wrapper
@decor
def multiply(a,b):
    return a*b
print("Result:",multiply(10,2))
print("-------------------------------------------------------")

print("=======================================================")
print("------------------ Bonus Challenge --------------------")
print("---------------- Robot Command Logger -----------------")
print("=======================================================")
def robot_logger(function):
    @wraps(function)
    def wrapper(*args):
        print("Robot command started!")
        return function(*args)
    return wrapper
@robot_logger
def move_robot(direction):
    print("Robot moving ",direction,"!")
    print("Robot command completed!!")
move_robot("backward")
print("-------------------------------------------------------")
print("---------------- End of Day-25 Challenge --------------")
print("-------------------------------------------------------")