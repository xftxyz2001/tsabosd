from snownlp import SnowNLP
text = '''问君此去几时还来时莫徘徊'''
s = SnowNLP(text)
print(s.sentiments)