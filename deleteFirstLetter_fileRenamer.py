import os

file_path="D:\\Github\\tistoryPostings\\artificial Intelligence\\AIFFEL\\posted"
file_list = os.listdir(file_path)

for f in file_list:
    if(f.startswith('ㅎ')):
        # print(f)
        # print(type(f))
        src=os.path.join(file_path,f)
        f = f[1:]
        print(f)
        dst = os.path.join(file_path, f)
        os.rename(src,dst)