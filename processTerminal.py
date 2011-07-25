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
    process=Popen('bash',stdout=PIPE,stdin=PIPE,stderr=PIPE,shell=True)

    #Note1: readlines will not work because it expects EOF in the end.
    #readline() also doesn't work, and I don't know why.
    #print process.stdout.readlines()

    while (process.poll()==None):
        #commandList=shlex.split(command.get(1))

        #Note2: I got two methods, the first one works for the first time, but
        #will not work for the second time because communicate expects the
        #process to terminate and hence it blocks the flow!

        #Note3:
        #After experimenting, I think I know why readlines/readline do not work.
        #The reason may be that the process is not terminated and hence it may
        #still write to the file and hence the lock on the file would not be
        #freed until it is terminated. So, readline/readlines would not be able
        #open the file because it is currently used by the shell. If the shell
        #terminated, then the files might be free to read.
        #Check: 
        #http://docs.python.org/library/subprocess.html#subprocess.Popen.communicate

        #1
        output.put(''.join(process.communicate(command.get(1))), 1)

        #2
        #process.stdin.write(command.get(1))
        #process.stdin.flush()
        #output.put(process.stdout.readline(),1)
        #process.stdout.flush()

        
        

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

