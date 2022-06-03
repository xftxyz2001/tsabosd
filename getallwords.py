import os
import jieba

seg_result = []
for dirpath, dirnames, filenames in os.walk('music'):
    for filename in filenames:
        with open(os.path.join(dirpath, filename), 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                seg_list = jieba.cut(line)
                for i in seg_list:
                    seg_result.append(i)
seg_result = list(set(seg_result))
with open('worddict.txt', 'w', encoding='utf-8') as f:
    for i in seg_result:
        f.write(i + '\n')
