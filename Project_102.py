import os
import shutil

from_dir = "C:/Users/vivaa/Downloads"
to_dir_1 = "C:/Users/vivaa/Downloads/Document_Folder"
to_dir_2 = "C:/Users/vivaa/Downloads/Image_Folder"

list_of_files = os.listdir(from_dir)
print(list_of_files)

length = len(list_of_files)
print(length)

extensions_1 = [".pdf",".txt",".zip",".exe"]
extensions_2 = [".wav",".png",".jpg",".jpeg",".gif",".webp",".mp3"]

for i in range(0,length,1):
    ext = os.path.splitext(list_of_files[i])
    if ext[1] == extensions_1:
        src = "C:/Users/vivaa/Downloads/"+list_of_files[i]
        dest = "C:/Users/vivaa/Downloads/Document_Folder/"+list_of_files[i]
        shutil.copyfile(src,dest)
        print(src,dest)
    elif ext[1] == extensions_2:
        src = "C:/Users/vivaa/Downloads/"+list_of_files[i]
        dest = "C:/Users/vivaa/Downloads/Image_Folder/"+list_of_files[i]
        shutil.copyfile(src,dest)
        print(src,dest)

