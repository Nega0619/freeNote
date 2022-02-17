# pip install clipboard
import clipboard

"""
lms에서 문자열을 복사한 후 주피터 노트북에 넣으면 `- `이거 문자가 무시되는데 그거 짜증나서 자동화 해버림
"""

multi_string = """
ARIMA 모델 빌드와 훈련
모델 테스트 및 플로팅
최종 예측 모델 정확도 측정(MAPE)
"""

splited_str = multi_string.split('\n')

tobe_copy=""
for str in (splited_str[1:-1]):
    pass
    # print(str)
    # enmerate하려다가 때려침 ㅎ_ㅎ
    # splited_str[idx] = '- '+str
    print('- '+str+'\n',end="")
    tobe_copy+='- '+str+'\n'

clipboard.copy(tobe_copy+'\n')
# print(multi_string)