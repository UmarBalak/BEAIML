import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# English
text = "Learn something new every day"
tokenized_text = word_tokenize(text)
pos_tagged = nltk.pos_tag(tokenized_text)
print("POS Tagged (English):")
print(pos_tagged)

# Hindi
text_hi = "हर दिन कुछ नया सीखो"
tokenized_text = word_tokenize(text_hi)
pos_tagged = nltk.pos_tag(tokenized_text)
print("POS Tagged (Hindi):")
print(pos_tagged)