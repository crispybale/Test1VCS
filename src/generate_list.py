import random
def generate_list()
    alist = [ x for x in range(random.randint(-10,10))]
    return alist
"""
print a generate list 
"""

def printIt()
    print(generate_list())

def main();
    printIt()
    
"""
IF this script file is call, it will run main() directly 
"""

if__name__ == '__main__':
    print ("Test PrintIt() :")
    main()
    