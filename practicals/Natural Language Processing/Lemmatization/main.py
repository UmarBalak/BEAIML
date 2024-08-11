import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

l = ["Programming", "programmer", "Programmable"]
for word in l:
  print(f"{word}: {lemmatizer.lemmatize(word)}")