import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download necessary data
nltk.download('punkt')
nltk.download('stopwords')

# Input text
text = "Hey devs, hope your code is bug-free and your models are learning fast!"
print(f"Input text: \n{text}")
print(f"Length of text: {len(text)}")

# Tokenization
tokens = word_tokenize(text)
print(f"Tokens: \n{tokens}")
print(f"Length of tokens: {len(tokens)}")

# Stopword removal
filtered_tokens = [word for word in tokens if word.lower() not in stopwords.words('english')]
print(f"Filtered tokens: \n{filtered_tokens}")
print(f"Length of filtered tokens: {len(filtered_tokens)}")
