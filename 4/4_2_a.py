#programm to demonstrate the Function of os.path

from os import *
# chdir(r'C:\Users\JarviS\Desktop')
print(getcwd())

#join joins Two diff paths
file_path = path.join(getcwd(),'test.txt')
print(file_path)

#split
path_1 , file = path.split(file_path)
print(path_1, ':', file)

#exists
is_exist = path.exists(getcwd())
print(is_exist) #true

#with Fake Path
is_exist = path.exists(file_path)
print(is_exist)

#abs_path
abs_path = path.abspath('test.txt')
print(abs_path)

# Path
path_1 = r'C:\Users\..\..\..\Documents'

# normpath Normalize the specified path
norm_path = path.normpath(path_1)
print(norm_path)