import sys
import os
cwd = os.getcwd() #current Working Directory

sys.path.append(cwd) #print(sys.path)

#test the module : generate_list
from generate_list import printIt
printIt()
