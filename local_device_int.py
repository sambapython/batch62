'''
import os
#cmd="mkdir local2"
#cmd="rm -rf local2"
cmd="ls -l"
resp = os.system(cmd)
print("response:",resp)
'''
'''
from subprocess import check_output
resp = check_output(["ls","-l"])
print("response:",resp)
'''
'''
import os
cmd="cp content.odt local/"
os.system(cmd)
'''