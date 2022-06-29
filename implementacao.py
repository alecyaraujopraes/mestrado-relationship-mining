from xml.dom.xmlbuilder import DocumentLS
from stanza.models.common.doc import Document
import stanza

stanza.download("en") # download English model

nlp = stanza.Pipeline("en") # initialize English neural pipeline

sentences = """
    WASHINGTON — Stellar pitching kept the Mets afloat in the first half of last season despite their offensive woes. But they cannot produce an encore of their pennant-winning season if their lineup keeps floundering while their pitching is nicked, bruised and stretched thin.
    “We were going to ride our pitching,” Manager Terry Collins said before Wednesday’s game. “But we’re not riding it right now. We’ve got as many problems with our pitching as we do anything.”
    Wednesday’s 4-2 loss to the Washington Nationals was cruel for the already-limping Mets. Pitching in Steven Matz’s place, the spot starter Logan Verrett allowed two runs over five innings. But even that was too large a deficit for the Mets’ lineup to overcome against Max Scherzer, the Nationals’ starter.
    “We’re not even giving ourselves chances,” Collins said, adding later, “We just can’t give our pitchers any room to work.”
    """

# verbos: kept, 

# Read dataset New York Times articles
# with open("nytimes_news_articles.txt", "r") as f:
#     data = f.read()

# print(data)
# print(type(data))

doc = nlp(sentences)

dicts = doc.to_dict()

for list in dicts:
    for word in list:
        if word.get("upos") == "VERB":
            print(word.get("text"))


# print("Entidades:")
# print(doc.entities)