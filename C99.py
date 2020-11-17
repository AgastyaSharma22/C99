import os
import shutil
#path='E:/coding/File.txt'
#root_ext=os.path.splittext(path)
#print("root part ",root_ext[0])
#print("ext part ",root_ext[1],"\n")
#os.mkdir("/folder_C")
path='/coding/folder_A/sample.txt'
path2='/coding/folder_A'
isExist=os.path.exists(path)
print(isExist)
root_ext=os.path.splitext(path)
print("root part ",root_ext[0])
print("ext part ",root_ext[1],"\n")
print("Before copying file:")
print(os.listdir(path2))
source="/coding/folder_A/sample.txt"
destination="/coding/folder_A/sample(copy).txt"
dest=shutil.copy(source,destination)
print("After copying file:")
print(os.listdir(path2))

path3='/coding/folder_B'
print("Before moving file:")
print(os.listdir(path3))
source1='/coding/folder_B/mp4'
destination1='/coding/folder_B/png'
dest1=shutil.move(source1,destination1)
print("after moving file:")
print(os.listdir(path3))