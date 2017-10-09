import os
from shutil import copyfile
from PIL import Image
base_dir = 'C:/Users/Abhishek/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets'
dest_dir = 'C:/Users/Abhishek/Desktop/Spotlight'
directory = os.fsencode(base_dir)
list_of_files = os.listdir(directory)
for each in list_of_files:
    if os.stat(base_dir + "/" + each.decode()).st_size > 400000:
        copyfile(base_dir + "/" + each.decode(), dest_dir + "/" + each.decode() + ".jpg" )
 
directory = os.fsencode(dest_dir)
list_of_images = os.listdir(directory)
for each in list_of_images:
    img = Image.open(dest_dir + "/" + each.decode())
    if img.size != (1920, 1080):
        img.close()
        os.remove(dest_dir + "/" + each.decode())

            
        
