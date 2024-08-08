from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()
words = ["program", "programs", "programmer", "programming", "programmers"]

for w in words:
	print(w, " : ", ps.stem(w))
