from xml.dom.xmlbuilder import DocumentLS
from stanza.models.common.doc import Document
import stanza

stanza.download("en") # download English model

nlp = stanza.Pipeline("en") # initialize English neural pipeline

sentences = """
    {"sentText": "But that spasm of irritation by a master intimidator was minor compared with what Bobby Fischer , the erratic former world chess champion , dished out in March at a news conference in Reykjavik , Iceland .", 
    "articleId": "/m/vinci8/data1/riedel/projects/relation/kb/nyt1/docstore/nyt-2005-2006.backup/1677367.xml.pb", 
    "relationMentions": [
        {"em1Text": "Bobby Fischer", "em2Text": "Iceland", "label": "/people/person/nationality"}, 
        {"em1Text": "Iceland", "em2Text": "Reykjavik", "label": "/location/country/capital"}, 
        {"em1Text": "Iceland", "em2Text": "Reykjavik", "label": "/location/location/contains"}, 
        {"em1Text": "Bobby Fischer", "em2Text": "Reykjavik", "label": "/people/deceased_person/place_of_death"}
    ], 
    "entityMentions": [
        {"start": 0, "label": "PERSON", "text": "Bobby Fischer"}, 
        {"start": 1, "label": "LOCATION", "text": "Reykjavik"}, 
        {"start": 2, "label": "LOCATION", "text": "Iceland"}], 
        "sentId": "1"}
    {"sentText": "But Schaap seems as comfortable in that role as Joe Buck , the Fox baseball and football sportscaster who so clearly benefited from learning beside his father , Jack Buck , the late voice of the St. Louis Cardinals . ''", 
    "articleId": "/m/vinci8/data1/riedel/projects/relation/kb/nyt1/docstore/nyt-2005-2006.backup/1677367.xml.pb", 
    "relationMentions": [
        {"em1Text": "Jack Buck", "em2Text": "Joe Buck", "label": "/people/person/children"}
        ], 
        "entityMentions": [
            {"start": 1, "label": "PERSON", "text": "Joe Buck"}, 
            {"start": 2, "label": "PERSON", "text": "Fox"}, 
            {"start": 3, "label": "PERSON", "text": "Jack Buck"}, 
            {"start": 4, "label": "ORGANIZATION", "text": "St. Louis Cardinals"}
        ], 
        "sentId": "2"}

    """

doc = nlp(sentences)

dicts = doc.to_dict()

for list in dicts:
    for word in list:
        if word.get("upos") == "VERB":
            print(word.get("text"))


# print("Entidades:")
# print(doc.entities)