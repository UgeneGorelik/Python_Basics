#importing os module
import os

#module for running commands in OS (windows / unix ...)
import  subprocess
from datetime import datetime

#help command helps us get docstring description on the module
print(help(os))

#get current directory
print(os.getcwd())
#list directories
print(os.listdir())
#see file status
print(os.stat('DataStoringModules.py'))
#get when file changed time
mod_time=os.stat('DataStoringModules.py').st_mtime
#change to date time format
print(datetime.fromtimestamp(mod_time))
#get enviorment variables
print(os.environ)

print(os.path.basename('tst.txt'))
print(os.path.dirname('tst.txt'))

#conactinate paths
base_dir = r'c:\bla\bing'
filename = r'data.txt'
fullpath=os.path.join(base_dir, filename)

print(fullpath)

#recursivly show file names and paths
for dirpath,dirnames,filenames in os.walk('/'):
    print(dirpath,dirnames,filenames)

#run command on OS
subprocess.call(['ls','-l'],shell=True)

#get results of the command run
display=subprocess.check_output(['ls'])

print(display)