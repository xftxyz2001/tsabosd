from snownlp import SnowNLP

with open('worddict.txt', 'r', encoding='utf-8') as fin:
    with open('worddictvalue.txt', 'w', encoding='utf-8') as fout:
        for line in fin:
            s = SnowNLP(line)
            fout.write(line.strip() + '\t' + str(s.sentiments) + '\n')
