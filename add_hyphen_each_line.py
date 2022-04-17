# pip install clipboard
import clipboard

"""
lms에서 문자열을 복사한 후 주피터 노트북에 넣으면 `- `이거 문자가 무시되는데 그거 짜증나서 자동화 해버림
"""

multi_string = """
영화 구분

synopsis_art.txt : 예술영화

synopsis_gen.txt : 일반영화(상업영화)

그 외는 독립영화 등으로 분류됩니다.

장르 구분

synopsis_SF.txt: SF

synopsis_가족.txt: 가족

synopsis_공연.txt: 공연

synopsis_공포(호러).txt: 공포(호러)

synopsis_기타.txt: 기타

synopsis_다큐멘터리.txt: 다큐멘터리

synopsis_드라마.txt: 드라마

synopsis_멜로로맨스.txt: 멜로로맨스

synopsis_뮤지컬.txt: 뮤지컬

synopsis_미스터리.txt: 미스터리

synopsis_범죄.txt: 범죄

synopsis_사극.txt: 사극

synopsis_서부극(웨스턴).txt: 서부극(웨스턴)

synopsis_성인물(에로).txt: 성인물(에로)


synopsis_스릴러.txt: 스릴러

synopsis_애니메이션.txt: 애니메이션

synopsis_액션.txt: 액션

synopsis_어드벤처.txt: 어드벤처

synopsis_전쟁.txt: 전쟁

synopsis_코미디.txt: 코미디

synopsis_판타지.txt: 판타지
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