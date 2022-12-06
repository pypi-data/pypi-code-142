import RobotArm
from RobotArm import network
import math
import time

class Robot:
    

    def __init__(self):
        self.ip = "169.254.126.87"
        network.call(self.ip)
        self.jointdata = [90,90,90,90,90,110]

    def __str__(self):
        return self.jointdata
    
    def sayNet(self):
        for i in range(0,6):
            network.say("{0},{1}".format(i,self.jointdata[i]))
            print("{0},{1}".format(i,self.jointdata[i]))
        return True
        
    def interpolate(self,newData,steps,timego):
        increment = [0,0,0,0,0,0]

        for pos in range(0,6):
            temp = newData[pos]-self.jointdata[pos]
            increment[pos] = round(temp/steps,2)
        print("increment",increment)
        for t in range(0,steps):
            for pos in range(0,6):
                self.jointdata[pos] = round(self.jointdata[pos] + increment[pos],2)
            self.sayNet()

            time.sleep(timego/steps)
        for pos in range(0,6):
            self.jointdata[pos] = newData[pos]
        self.sayNet()    
        return True

    def go(self):
        network.say("8,1")
        return True

    def stop(self):
        network.say("8,0")
        return True

    def runArray(self,array,time):
        for i in range(0,len(array)-1):
            while not self.interpolate(array[i],(time*5)+5,time):
                time.sleep(1)
        return True


    