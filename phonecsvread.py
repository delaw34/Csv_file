#to enable us access the file we import the os and sys modules

import os
import sys

#open the file
#kindly note if this open function on line 8 does not work then use line 9 
#myfiles = open('phone_list.txt', 'r')
myfiles = open(os.path.join(sys.path[0],'phone_name.csv'), 'r')


#read the file using the read function
read_file = myfiles.read()

print(read_file)

myfiles.close()

