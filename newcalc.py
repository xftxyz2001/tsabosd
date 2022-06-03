import os
import jieba
from pprint import pprint

filewordsdict = {}
valuedict = {}

with open('worddictvalue.txt', 'r', encoding='utf-8') as f:
    for line in f:
        # line = line.strip()
        # print(line)
        word, value = line.split('\t')
        valuedict[word] = value[:-1]

# print('valuedict:')
# pprint(valuedict)

for dirpath, dirnames, filenames in os.walk('music'):
    for filename in filenames:
        with open(os.path.join(dirpath, filename), 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                seg_list = jieba.cut(line)
                for i in seg_list:
                    filewordsdict[filename] = filewordsdict.get(
                        filename, []) + [i]
# pprint(filewordsdict)
with open('new_result.csv', 'w', encoding='utf-8') as f:
    for k, v in filewordsdict.items():
        score = 0
        for sv in v:
            score += float(valuedict.get(sv, 0))
        avgscore = score / len(v)
        # f.write(k[:-4] + ',' + str(avgscore) + ',' +
        #         ('积极' if avgscore > 0.5 else '消极') + '\n')
        f.write(k[:-4] + ',' + str(avgscore) + '\n')
