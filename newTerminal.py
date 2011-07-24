import pexpect

child=pexpect.spawn('/bin/bash')
#child.interact()
#size=len(child.readlines())
#size=40
while True:
    child.expect(pexpect.EOF)  #I even tried expecting for the prompt but the search takes place from the beginning.
    print child.before
    command=raw_input('enter hellooo ')
    #size=len(child.after)
    child.sendline(command)
    
    
    #print child.read(1)
    #print child.before
    #print child.after
