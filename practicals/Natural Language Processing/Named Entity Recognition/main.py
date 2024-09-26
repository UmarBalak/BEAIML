import spacy

# Load English language model
nlp = spacy.load("en_core_web_sm")

# Input text
text = "Artificial intelligence is revolutionizing the way we live and work."

# Process the text
doc = nlp(text)

# Print token text and its part of speech
for entity in doc.ents:
    print(f"Entity: {entity.text}, Label: {entity.label_}")
