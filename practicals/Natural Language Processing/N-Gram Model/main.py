import nltk
from nltk.util import ngrams
nltk.download('punkt')

def extract_ngrams(text, num):
    n_grams = ngrams(nltk.word_tokenize(text), num)
    return [' '.join(grams) for grams in n_grams]

# English
text_en = "Learn something new every day"
print(f"2-grams: {extract_ngrams(text_en, 2)}")
print(f"3-grams: {extract_ngrams(text_en, 3)}")
print(f"4-grams: {extract_ngrams(text_en, 4)}")

# Hindi
text_hi = "हर दिन कुछ नया सीखो"
print(f"2-grams: {extract_ngrams(text_hi, 2)}")
print(f"3-grams: {extract_ngrams(text_hi, 3)}")
print(f"4-grams: {extract_ngrams(text_hi, 4)}")
