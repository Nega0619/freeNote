"""
https://github.com/Nega0619/korquad.github.io
https://korquad.github.io/KorQuad%201.0/
https://hayjo.tistory.com/75
"""


import json

with open('korquad2.1_train_00.json', 'r',encoding="UTF-8")  as fp:
    after = json.load(fp)

print(after)

with open('train00.json', 'a+', encoding="UTF-8") as fp:
    json.dump(after, fp, ensure_ascii=False)