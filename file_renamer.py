import os

target_path = '/home/hwi/Downloads/VQIS-POC Image data/VQIS/VQIS_POR_TEST'

file_list = os.listdir(target_path)
for f in file_list:
    
    aft = os.path.join(target_path, f.replace('JPG', 'jpg'))
    pre = os.path.join(target_path, f)
    # print(pre)
    # print(aft)
    # break
    os.rename(pre,aft)
    