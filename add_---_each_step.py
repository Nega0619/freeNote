# pip install clipboard
import clipboard

"""
lms에서 문자열을 복사한 후 주피터 노트북에 넣으면 `- `이거 문자가 무시되는데 그거 짜증나서 자동화 해버림
"""

multi_string = """
Word2Vec
Word2Vec은 "단어를 벡터로 만든다"는 멋진 이름을 가지고 있습니다. 난 오늘 술을 한 잔 마셨어 라는 문장의 각 단어 즉, 동시에 등장하는 단어끼리는 연관성이 있다는 아이디어로 시작된 알고리즘입니다. 예문의 경우 다른 단어는 몰라도 술과 마셨어는 괜찮은 연관성을 캐치해낼 수 있겠네요.

Word2Vec에 대한 좋은 자료를 읽어보시고, 다시 얘기해보도록 하죠!
"""

splited_str = multi_string.split('\n')

tobe_copy=""
for line in (splited_str[1:-1]):
    pass
    if(line.lower().find('step')==0):
        tobe_copy+='\n\n'+line+'\n----\n'
    elif(line.find(')')==1):
        tobe_copy+='\n\n'+line+'\n----\n'
    elif(len(line)<20 and len(line)>3):
        tobe_copy+='\n\n'+line+'\n----\n'
    else:
        tobe_copy+=line

print(tobe_copy)

clipboard.copy(tobe_copy+'\n')
# print(multi_string)