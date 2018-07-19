#race condition

import os 

my_file = '/tmp/test.txt'
#Non-pythonic way

#if(os.access(my_file,os.R_OK)):
#    with open(my_file) as f:
#        print(f.read())
#else:
#    print("cant access the file")

try:
    f=open(my_file)
except IOError as e:
    print(e)
else:
    with f:
        print(f.read())
