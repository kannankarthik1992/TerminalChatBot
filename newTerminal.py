import pexpect

child=pexpect.spawn('/bin/bash')
#child.interact()
#size=len(child.readlines())
#size=40
while True:
    #Note: You can't expect EOF! Because the file is not closed. If the process
    #closes the file, then the end will be defined. When something is alive,
    #how can you say that it is dead?

    #child.expect(pexpect.EOF)  #I even tried expecting for the prompt but the search takes place from the beginning.

    child.expect('\$')  #I even tried expecting for the prompt but the search takes place from the beginning.
    print child.before,
    command=raw_input('%%')
    #size=len(child.after)
    child.sendline(command)
    
    #print child.read(1)
    #print child.before
    #print child.after
