import spacy

nlp = spacy.load("en_core_web_sm")

# Process whole documents
text = ("The Fluminense Federal University is a public higher education institution located mainly in Niterói.")
doc = nlp(text)

# Analyze syntax
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)

    