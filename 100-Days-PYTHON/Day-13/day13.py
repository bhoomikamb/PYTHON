#=============================================================================
#-----------------------------ANIMAL SOUNDS-----------------------------------
#=============================================================================
class Animals:
    def sound(self):
        print("Animal Sounds")
class Dog(Animals):
    def sound(self):
        print("Dog barks!!")
class Cat(Animals):
    def sound(self):
        print("Cat meows!!")
dog=Dog()
cat=Cat()
dog.sound()
cat.sound()
print("--------------------------------------------------------------------")


#=============================================================================
#------------------------------ELECTRONICS DEVICES----------------------------
#=============================================================================
class Device:
    def start(self):
        print("Device is started!!")
class Arduino(Device):
    def start(self):
        print("Arduino is started!!")
class ESP32(Device):
    def start(self):
        print("ESP32 is started!!")
class RaspberryPi(Device):
    def start(self):
        print("RaspberryPi is started!!")
devices=[Arduino(),ESP32(),RaspberryPi()]
for device in devices:
    device.start()
print("--------------------------------------------------------------------")


#=========================================================================
#--------------------------PAYMENT METHOD---------------------------------
#=========================================================================
class payment:
    def pay(self,amount):
        print("Paid", amount)
class UPIPayment(payment):
    def pay(self,amount):
        print("Paid",amount,"using UPI")
class CardPayment(payment):
    def pay(self,amount):
        print("Paid",amount,"using Card")
class CashPayment(payment):
    def pay(self,amount):
        print("Paid",amount,"using Cash.")
money=input("Enter an amount:")
payment=[UPIPayment(),CardPayment(),CashPayment()]
for pay in payment:
    pay.pay(money)
print("--------------------------------------------------------------------")

#===========================================================================
#--------------------------------BONUS CHALLENGE----------------------------
#-----------------------------ROBOT CONTROL SYSTEM--------------------------
#===========================================================================
class Robot:
    def move(self):
        print("The Robot is moving.")
    def stop(self):
        print("The Robot has Stopped!!")
class LineFollowerBot(Robot):
    def move(self):
        print("The Bot is following the black line!")
    def stop(self):
        print("The Line Follower Bot is stopped!!")
class ObstacleAvoidingBot(Robot):
    def move(self):
        print("The Bot is moving while avoiding obstacles!!")
    def stop(self):
        print("The Obtacle Avoiding Bot is stopped!!")
class HumanFollowerBot(Robot):
    def move(self):
        print("The Bot is Following Human!")
    def stop(self):
        print("The Human Follower Bot is stopped!!")
bots=[LineFollowerBot(),ObstacleAvoidingBot(),HumanFollowerBot()]
for bot in bots:
    bot.move()
    bot.stop()
print("End of Day-13 Challenges Successfully!")