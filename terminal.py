#Note: readline would not work on an unterminated process. Read the notes in
#processTerminal.py file.
from subprocess import Popen,PIPE
import shlex

#inp=open('input','w+')
out=open('ouput','w+')
err=open('error','w+')

process=Popen('bash',stdin=PIPE,stdout=out,stderr=err,shell=True)

while(True):
    command=raw_input("Enter command> ")
    #comList=shlex.split(command)
    
    if(command=='exit'):
        process.kill()
        break
        
    #inp.write(command)
    command=command+'\n'    
    print 'helllllllllllllllllooooooooo'
    #process.wait()
    
    process.stdin.write(command)
        
    print out.readline()
    print err.readline()
    #out.close()
    #out=open('ouput','w+')
    
    #output=process.communicate()
    print process.poll()
    #print output[0]

