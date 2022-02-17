# pip install clipboard
import clipboard

"""
lms에서 문자열을 복사한 후 주피터 노트북에 넣으면 `- `이거 문자가 무시되는데 그거 짜증나서 자동화 해버림
"""

multi_string = """
새로운 입력 문장에 대해서는 훈련 때와 동일한 전처리를 거친다.
입력 문장을 토크나이징하고, START_TOKEN과 END_TOKEN을 추가한다.
패딩 마스킹과 룩 어헤드 마스킹을 계산한다.
디코더는 입력 시퀀스로부터 다음 단어를 예측한다.
디코더는 예측된 다음 단어를 기존의 입력 시퀀스에 추가하여 새로운 입력으로 사용한다.
END_TOKEN이 예측되거나 문장의 최대 길이에 도달하면 디코더는 동작을 멈춘다.
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