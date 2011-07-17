'''This program intends to integrate the fortune program and terminal like features in Google talk bot'''

import os
from PyGtalkRobot import GtalkRobot
from subprocess import Popen,PIPE
import shlex


class SampleRobotFortune(GtalkRobot):
    terminalState=0               #determines whether the default handler will be working for getting terminal commands or in normal mode. 0=off, 1=on
    
    def command_001_fortune(self,user,message,args):
        '''fortune'''
        
        fortResult=Popen("fortune",stdout=PIPE)
        output=fortResult.communicate()
        print output[0]
        self.replyMessage(user,'\n')
        self.replyMessage(user,output[0])
        
                    
    def command_100_default(self, user, message, args):   #The default handler also implements the functionality of terminal
        """.*?(?s)(?m)"""
        
        if(message=='terminal'):
            self.replyMessage(user,"\nTerminal started\n")
            self.replyMessage(user,">")
            self.terminalState=1
            
        elif(self.terminalState==0):
            self.replyMessage(user,'The command \'%s\' does not exist'%message)  
            
        elif(self.terminalState==1):            
            comList=shlex.split(message)
            
            if(comList[0]=='exit'):
                self.terminalState=0
                self.replyMessage(user,'Exiting from terminal')

            else:
                process=Popen(comList,stdout=PIPE)                
                output=process.communicate()
                self.replyMessage(user,'\n')
                self.replyMessage(user,output[0])
                if(output[0]!=None):
                    self.replyMessage(user,output[1])
            
            
              
if __name__=="__main__":
    bot = SampleRobotFortune()
    bot.setState('available', "Simple Gtalk Robot")
    bot.start("karthikshaastradistro@gmail.com", "ROME1234")
        
    
