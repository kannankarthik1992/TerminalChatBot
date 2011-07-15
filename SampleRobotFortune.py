'''This program intends to integrate the fortune program in Google talk bot'''

import os
from PyGtalkRobot import GtalkRobot
from subprocess import Popen,PIPE

class SampleRobotFortune(GtalkRobot):
    
    def command_001_fortune(self,user,message,args):
        '''fortune'''
        
        fortResult=Popen("fortune",stdout=PIPE)
        output=fortResult.communicate()
        print output[0]
        self.replyMessage(user,'\n')
        self.replyMessage(user,output[0])
        
              
if __name__=="__main__":
    bot = SampleRobotFortune()
    bot.setState('available', "Simple Gtalk Robot")
    bot.start("karthikshaastradistro@gmail.com", "ROME1234")
        
    
