import spacy

nlp = spacy.load("en_core_web_lg")

phrase = input("Please give me a sentence: ")
result = nlp(phrase)
print(result.vector)