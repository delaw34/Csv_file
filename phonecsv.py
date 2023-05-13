#convert a text file to csv file 
#to enable us access the file we import the os and sys modules
import os
import sys

#write a file 
phone_name = ['samsung \n', 'iphone \n', 'nokia \n', 'hawaii \n']
phone_name2 = ['motorolla \n', 'redmi\n', 'android \n']

#write a csv file 
with open(os.path.join(sys.path[0],'phone_name.csv'), 'w') as phone:
    phone_name_write = phone.writelines(phone_name)
    phone_name_write2 = phone.writelines(phone_name2)
    print('your csv file have written successfully')
    #check your folder a file has been created 
