# pip install clipboard
import clipboard

"""
lms에서 문자열을 복사한 후 주피터 노트북에 넣으면 `- `이거 문자가 무시되는데 그거 짜증나서 자동화 해버림
"""

multi_string = """
데이터의 중복 제거
NaN 결측치 제거
한국어 토크나이저로 토큰화
불용어(Stopwords) 제거
사전word_to_index 구성
텍스트 스트링을 사전 인덱스 스트링으로 변환
X_train, y_train, X_test, y_test, word_to_index 리턴
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