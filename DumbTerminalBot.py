'''This program intends to integrate the fortune program and terminal like features in Google talk bot'''

import os
from PyGtalkRobot import GtalkRobot
from subprocess import Popen,PIPE
import shlex

pFile=open("password",'r')                    
password=(pFile.readline()).split()[0]    #retreiving password for google account from local file password


class DumbTerminalBot(GtalkRobot):
    terminalState=0               #determines whether the default handler will be working for getting terminal commands or in normal mode. 0=off, 1=on
    helpString = "Chat Bot v1.0\nAvailable commands:\n 1. terminal - to open the terminal"

    def command_001_help(self,user,message,args):
	'''(help)( +(.*))?$(?i)'''
	self.replyMessage(user, self.helpString)
                    
    #@Karthik: What is the diff between ''' and #.
    # ''' is used for multiline strings while # is use for giving comments
    # ''' is mostly ised for doc strings
     
    def command_100_default(self, user, message, args):   #The default handler also implements the functionality of terminal
        '''.*?(?s)(?m)'''
        
        if(message=='terminal'):
            self.replyMessage(user,"\nTerminal started\n")
            self.replyMessage(user,">")
            self.terminalState=1
            
        elif(self.terminalState==0):
	    self.replyMessage(user, self.helpString)
            
        
        elif(self.terminalState==1):         
            comList=shlex.split(message)
            
            if(comList[0]=='exit'):
                self.terminalState=0
                self.replyMessage(user,'Exiting from terminal')
                
           

            else:
                process=Popen(comList,stdout=PIPE, stdin=None, shell=False)
                output=process.communicate()
                self.replyMessage(user,'\n')
                self.replyMessage(user,output[0])
                if(output[0]!=None):
                    self.replyMessage(user,output[1])
            
            
              
if __name__=="__main__":
    bot = DumbTerminalBot()
    bot.setState('available', "Dumb terminal bot")
    bot.start("karthikshaastradistro@gmail.com", password)
        
    
