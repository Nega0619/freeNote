import os
import datetime
import re

# 무시할 문자열
# yyyy-mm-dd-식의 문자가있으면 무시하도록 정규표현식선언
finised_file_pattern = re.compile('\d\d\d\d-\d\d-\d\d-')
musi_pattern=re.compile('MUSHI')

# 파일 경로를 입력하세요.
file_path=r'D:\Github\path-finding-rl\새 폴더'


file_list = os.listdir(file_path)
for f in file_list:
    pass
    src = os.path.join(file_path, f)
    if (finised_file_pattern.match(f) != None): continue
    if (f.find('MUSHI')!=-1): continue
    file_time = os.path.getctime(src)
    fts = str(datetime.datetime.fromtimestamp(file_time))
    # dst = fts[:10]+'-'+f
    dst = f+r'.ipynb'
    print(dst)
    dst = os.path.join(file_path,dst)
    os.rename(src,dst)