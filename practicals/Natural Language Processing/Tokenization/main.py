import nltk
nltk.download('punkt')

text = "Code is like humor. When you have to explain it, it's bad."

split_tokens = text.split()
print(f"split tokens:\n{split_tokens}")
print(f"length of split tokens: {len(split_tokens)}\n")

nltk_tokens = nltk.word_tokenize(text)
print(f"nltk tokens:\n{nltk_tokens}")
print(f"length of nltk tokens: {len(nltk_tokens)}")