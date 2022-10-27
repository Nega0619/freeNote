import os

target_path = '/home/hwi/github/data/VQIS_PoC/skin_s'

file_list = os.listdir(target_path)
for f in file_list:
    # print(f)
    src = os.path.join(target_path, f)
    print(f)
    print(src)
    new_file_name = src.replace('skin_s_', '')
    os.rename(src,new_file_name)