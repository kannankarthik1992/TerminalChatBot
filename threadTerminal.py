from subprocess import Popen,PIPE
import shlex
import threading
from Queue import Queue


class MyThread(threading.Thread):
    def __init__(self,func,args):
        threading.Thread.__init__(self)
        self.func=func
        self.args=args
        
    def run(self):
        apply(self.func,self.args)
        
        

def bash(command,output):
    #commandList=shlex.split('python test.py')   
    process=Popen('bash',stdout=PIPE,stdin=PIPE,shell=True)
    print 'hello'
    #print process.stdout.read(1)
    print 'karthik'
    while (process.poll()==None):
        #commandList=shlex.split(command.get(1))
        print 'bash'
        process.stdin.write(command.get(1))
        process.stdin.flush()
        print 'deepak'
        output.put(process.stdout.readlines(),1)
        print 'mummy'
        process.stdout.flush()
        
        

def communicate(command,output):
    while True:
        command.put(raw_input('enter command>'))
        print 'communicate'
        print output.get(1)
        
        
  
funcs=[bash,communicate]
nfuncs=len(funcs)    
            
def main():
    
    command=Queue(1)
    output=Queue(1)
    threads=[]
    
    for i in range(nfuncs):
        t=MyThread(funcs[i],(command,output))
        threads.append(t)
        
    for i in range(nfuncs):
        threads[i].start()
        
    for i in range(nfuncs):
        threads[i].join()
        
    print 'successful'       
        
if __name__=='__main__':
    main()






    
