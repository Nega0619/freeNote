# pip install clipboard
import clipboard

"""
lms에서 문자열을 복사한 후 주피터 노트북에 넣으면 `- `이거 문자가 무시되는데 그거 짜증나서 자동화 해버림
"""

multi_string = """
들어가며
기계가 읽을 수 있나요?
어떤 과정으로 읽을까요?
딥러닝 문자인식의 시작
사진 속 문자 찾아내기 - detection
사진 속 문자 읽어내기 - recognition
keras-ocr 써보기
테서랙트 써보기
프로젝트 : 다양한 OCR 모델 비교하기
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

