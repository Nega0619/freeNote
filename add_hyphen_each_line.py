# pip install clipboard
import clipboard

"""
lms에서 문자열을 복사한 후 주피터 노트북에 넣으면 `- `이거 문자가 무시되는데 그거 짜증나서 자동화 해버림
"""

multi_string = """
텍스트 데이터를 머신러닝 입출력용 수치데이터로 변환하는 과정을 이해한다.
RNN의 특징을 이해하고 시퀀셜한 데이터를 다루는 방법을 이해한다.
1-D CNN으로도 텍스트를 처리할 수 있음을 이해한다.
IMDB와 네이버 영화리뷰 데이터셋을 이용한 영화리뷰 감성 분류 실습을 진행한다.
"""


splited_str = multi_string.split('\n')

tobe_copy=""
for str in (splited_str[1:-1]):
    pass
    if(str==""):
        tobe_copy+='\n\n'
        continue
    # print(str)
    # enmerate하려다가 때려침 ㅎ_ㅎ
    # splited_str[idx] = '- '+str
    print('- '+str+'\n',end="")
    tobe_copy+='- '+str+'\n'

clipboard.copy(tobe_copy+'\n')
# print(multi_string)