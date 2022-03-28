# pip install clipboard
import clipboard

"""
lms에서 문자열을 복사한 후 주피터 노트북에 넣으면 `- `이거 문자가 무시되는데 그거 짜증나서 자동화 해버림
"""

multi_string = """
Hi, my name is John. ("Hi," "my", ..., "John." 으로 분리됨) - 문장부호
First, open the first chapter. (First와 first를 다른 단어로 인식) - 대소문자
He is a ten-year-old boy. (ten-year-old를 한 단어로 인식) - 특수문자
"""

splited_str = multi_string.split('\n')

tobe_copy=""
for idx, line in enumerate(splited_str[1:-1]):
    pass
    temp=""
    # print(str)
    # enmerate하려다가 때려침 ㅎ_ㅎ
    # splited_str[idx] = '- '+str
    temp +=str(idx+1)+'. '+line+'\n'
    print(temp, end="")
    tobe_copy+=temp

clipboard.copy(tobe_copy+'\n')
# print(multi_string)

