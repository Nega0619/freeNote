# pip install clipboard
import clipboard

"""
lms에서 문자열을 복사한 후 주피터 노트북에 넣으면 `- `이거 문자가 무시되는데 그거 짜증나서 자동화 해버림
"""

multi_string = """
HTML 문서의 개념에 대해서 이해한다.
태그의 형식에 대해서 이해한다.
크롤링을 위한 패키지인 BeautifulSoup4의 사용법을 이해한다.
머신 러닝 분류 방법인 나이브 베이즈 분류기의 사용법을 익힌다.
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

