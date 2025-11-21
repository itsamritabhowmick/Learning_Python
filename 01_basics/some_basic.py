print("Amrita")

#some computational example
print(2*2)
print(3+5)
print("chai" * 4)

#some example of Variable
marks = 100
print(marks)

#example of undefined variables
#print(tea) # Here occurs a ----> NameError: name 'tea' is not defined

import os
print(os.getcwd()) # to see the directory / path


#to print each individual character of a whole word
for a in "amrita":
    print(a)


import sys
print(sys.platform)



import hello_chai
hello_chai.chai("Mint tea")


# when loading some contents after import python file
from importlib import reload
reload(hello_chai)
print(hello_chai.chai_three)