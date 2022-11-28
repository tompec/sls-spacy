import spacy

def hello(event, context):
    nlp = spacy.load("en_core_web_sm")

    test = "John works at Google."

    doc = nlp(test)

    output = [(x, x.label_) for x in doc.ents]

    return output
