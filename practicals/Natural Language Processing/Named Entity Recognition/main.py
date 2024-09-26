import spacy

# Load English language model
nlp = spacy.load("en_core_web_sm")

# Input text
text = "Apple Inc. is planning to invest in artificial intelligence startups in California."

# Process the text
doc = nlp(text)

# Print token text and its part of speech
for entity in doc.ents:
    print(f"Entity: {entity.text}, Label: {entity.label_}")
