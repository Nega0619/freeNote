import os

target_path = '/home/hwi/github/data/VQIS_PoC/test/normal'

file_list = os.listdir(target_path)
for f in file_list:
    # print(f)
    src = os.path.join(target_path, f)
    new_file_name = target_path+'/normal_'+f
    os.rename(src,new_file_name)