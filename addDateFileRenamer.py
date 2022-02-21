import os
import datetime
import re

# 무시할 문자열
# yyyy-mm-dd-식의 문자가있으면 무시하도록 정규표현식선언
finised_file_pattern = re.compile('\d\d\d\d-\d\d-\d\d-')
musi_pattern=re.compile('MUSHI')

# test="""
# 2020-02-00-가나다
# 랄랄랄ㄹ라
# 2020-22-44-ㅅㅎㅁㄷ
# 23ㄱㄷㅇㅁㅈㄷㄹ
# ㄻㅈㄷ2323-44-ㄻㄷㄻㄷㄹ
# """
# splited_list = test.split('\n')

# for s in splited_list:
#     if(pattern.match(s) != None):
#         continue
#     print(s)


# 파일 경로를 입력하세요.
file_path=r'D:\Github\Nega0619.github.io\_posts'

file_list = os.listdir(file_path)
for f in file_list:
    pass
    src = os.path.join(file_path, f)
    if (finised_file_pattern.match(f) != None): continue
    if (f.find('MUSHI')!=-1): continue
    file_time = os.path.getctime(src)
    fts = str(datetime.datetime.fromtimestamp(file_time))
    dst = fts[:10]+'-'+f
    print(dst)
    dst = os.path.join(file_path,dst)
    os.rename(src,dst)

