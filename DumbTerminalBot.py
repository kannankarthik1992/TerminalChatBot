'''This program intends to integrate the fortune program and terminal like features in Google talk bot'''

import os
from PyGtalkRobot import GtalkRobot
from subprocess import Popen,PIPE
import shlex


class SampleRobotFortune(GtalkRobot):
    terminalState=0               #determines whether the default handler will be working for getting terminal commands or in normal mode. 0=off, 1=on
    
    def command_001_help(self,user,message,args):
	#TODO: May be you can make the below text as a function so that it can called whenever help is needed
	self.replyMessage(user, "Chat Bot v1.0\nAvailable commands:\n 1. terminal - to open the terminal");
                    
    #@Karthik: Use ''' comments to explain about a function. Remove this comment later.
    def command_100_default(self, user, message, args):   #The default handler also implements the functionality of terminal
        """.*?(?s)(?m)"""
        
        if(message=='terminal'):
            self.replyMessage(user,"\nTerminal started\n")
            self.replyMessage(user,">")
            self.terminalState=1
            
        elif(self.terminalState==0):
	    #TODO: print that the command doesn't exist and print the default help.
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
    bot.setState('available', "Dumb terminal bot")
    bot.start("karthikshaastradistro@gmail.com", "ROME1234")
        
    
