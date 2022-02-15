# https://enkoding.tistory.com/27
import os
import unicodedata

file_path=r"D:\GitHub\Aiffel_nodes_fd_1-20"
file_list = os.listdir(file_path)

for f in file_list:
    if(f.endswith('.ipynb')):
        # print(f)
        # print(type(f))D:\GitHub\Aiffel_nodes_fd_1-20
        src=os.path.join(file_path,f)
        uni1 = unicodedata.normalize('NFD', f)
        # print(uni1)

        uni2 = unicodedata.normalize('NFC', uni1)
        print(uni2)
        dst = os.path.join(file_path, uni2)
        os.rename(src,dst)