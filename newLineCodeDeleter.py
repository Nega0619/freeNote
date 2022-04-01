# pdf를 복붙하면 생기는 줄바꿈 문자를 다 삭제하는 것

import clipboard

# get texts
# test
f = open('text', 'r', encoding='UTF8')

result = ""
for line in f:
    # print(line)
    # print(line[-3:],',,')
    # print(ord(line[-1:]))
    # if(ord(line[-1:])==10):
    #     result+=" " + line[:-1]
    # else:
    #     result+=line
    if(line.endswith('.\n')):
        line = line + '\n\n'

    else:
        line = line[:-1] + " "
    result+=line

print(result)

clipboard.copy(result)
