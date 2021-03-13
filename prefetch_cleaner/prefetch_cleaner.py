import os
import shutil

dir_list=[]
file_list=[]
os.chdir(r"C:\Windows\Prefetch")
prefetch=os.listdir(r"C:\Windows\Prefetch")

for x in range(len(prefetch)):
    if len(prefetch[x].split("."))==1:
        dir_list.append(prefetch[x])
    elif len(prefetch[x].split("."))!=1:
        file_list.append(prefetch[x])
        
def del_directory(name):
    shutil.rmtree(k)
    print (k+ " Deleted")

def del_file(name):
    os.remove(i)
    print (i+ " Deleted")
        
for k in dir_list:
    del_directory(k)

for i in file_list:
    del_file(i)
 
print ("Cleaning Complete ")