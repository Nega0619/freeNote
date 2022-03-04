import clipboard

content_string ="""
- 기계는 어떤 방식으로 글을 읽을까?
  - 딥러닝 문자 인식의 시작
- 사진 속 문자 찾아내기 - detection
- 사진 속 문자 읽어내기 - recognition
- keras-ocr 써보기
- 테서랙트 써보기
- 프로젝트 : 다양한 OCR 모델 비교하기
"""

result = ""
for s in content_string.split('\n')[1:-1]:
    # print(s)
    # print("--")
    if(s.startswith("-")):
        s = s[:5].replace("-", "#") + s[5:] +"\n\n\n\n"
        result+=s
        # print(s)
    elif(s.startswith("  -")):
        s = s[:5].replace("  -", "##") + s[5:]+"\n\n\n\n"
        result+=s
        # print(s)
    else:
        print("notworking")

print(result)
clipboard.copy(result)
